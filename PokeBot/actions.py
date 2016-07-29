import time
import logging
from abc import ABC, abstractmethod

from colorama import Fore

from PokeApi.time import is_time_expired
from PokeApi.data import DataPokemon
from PokeApi.helper import print_items_awarded, print_capture_award
from PokeBot.tasks import Tasks
# FortPokestopAction
from POGOProtos.Inventory_pb2 import ItemId
from POGOProtos.Networking.Responses_pb2 import FortSearchResponse
# CatchPokemonAction
from POGOProtos.Enums_pb2 import PokemonId
from POGOProtos.Networking.Responses_pb2 import EncounterResponse, CatchPokemonResponse


class Action(ABC):
    """
    Base Action class for handling actions
    """

    def __init__(self, pokebot, data):
        self.logger = logging.getLogger(__name__)
        self.pokebot = pokebot
        self.data = data
        self.pokeapi = self.pokebot.pokeapi
        self.loc = self.pokeapi.location_manager
        self.map_cell_data = None

    def do_action(self):
        """
        Do action if check_action() return True
        """
        if self.check_action():
            self._make_action()

    @abstractmethod
    def is_active(self):
        """
        Check if this item is active
        """

    @abstractmethod
    def check_action(self):
        """
        Check action if is possible to execute before execution
        """

    @abstractmethod
    def _make_action(self):
        """
        action exetution method
        """


class FortPokestopAction(Action):
    """
    Action for spining the pokestop
    """
    def __init__(self, pokebot, data):
        super().__init__(pokebot, data)

    def is_active(self):
        """
        Check if pokestop is enabled and is not on cooldown
        """
        if self.data.cooldown_complete_timestamp_ms:
            fort_cooldown = self.data.cooldown_complete_timestamp_ms / 1000.0
            # if diif is less than 0 means that fort is on cooldown
            if not is_time_expired(fort_cooldown):
                return False
        
        if self.data.enabled:
            return True
        return False

    def check_action(self):
        """
        if pokestop is acvtive and distance is less than 40
        """
        if self.is_active() and self.map_cell_data.distance <= 40:
            return True
        return False

    def _fort_info(self):
        self.pokeapi.fort_details(fort_id=self.data.id,
                                  latitude=self.data.latitude,
                                  longitude=self.data.longitude)
        response = self.pokeapi.send_requests()
        return response.name

    def _make_action(self):
        fort_name = self._fort_info()
        self.logger.info(Fore.YELLOW + 'Spining pokestop (%s) at position (%0.7f,%0.7f)', 
                         fort_name,
                         self.data.latitude,
                         self.data.longitude)
        self.pokeapi.fort_search(fort_id=self.data.id, 
                                 player_latitude=self.loc.get_latitude(), 
                                 player_longitude=self.loc.get_longitude(), 
                                 fort_latitude=self.data.latitude, 
                                 fort_longitude=self.data.longitude)
        resp = self.pokeapi.send_requests()
        # result is not success (1) or inventory full (4)
        if resp.result not in [1, 4]:
            self.logger.info(Fore.RED + 'Coudnt spin pokestop (%s) at (%0.7f, %0.7f), response code %s', 
                             self.data.id,
                             self.data.latitude,
                             self.data.longitude,
                             FortSearchResponse.Result.Name(resp.result))
            return False
        # if inventory full
        elif resp.result == 4:
            # TODO do something if invetory is full
            self.logger.info(Fore.RED + 'Inventory is full aborting pokestops')
            return False

        #self.logger.info('Finished spining fort (%s)', self.data.id)
        self._reward_log(resp)
        return True

    def _reward_log(self, resp):
        self.logger.info(Fore.CYAN + 'Loot:')
        self.logger.info(Fore.CYAN + '%s xp', resp.experience_awarded)
        print_items_awarded(self.logger, self.pokebot.inventory, resp.items_awarded)


class CatchPokemonAction(Action):
    """
    catch pokemon action for catching
    """

    def __init__(self, pokebot, data):
        super().__init__(pokebot, data)
        self.catch_try = 0
        self.last_used_pokeball = 1

    @abstractmethod
    def _get_pokemon_id(self):
        """
        return pokemon id
        """
    
    def is_active(self):
        """
        Check if pokestop is enabled and is not on cooldown
        this is abstract class. always return False
        """
        return True

    def check_action(self):
        """
        if pokemon is active and distance is less than 50
        """
        if self.is_active() and self.map_cell_data.distance <= 50:
            return True
        return False

    def _make_encounter(self):
        self.pokeapi.encounter(encounter_id=self.data.encounter_id,
                               spawnpoint_id=self.data.spawnpoint_id,
                               player_latitude=self.loc.get_latitude(),
                               player_longitude=self.loc.get_longitude())
        return self.pokeapi.send_requests()

    def _choose_pokeball(self, catch_rate):
        pokeballs_count = self.pokebot.inventory.get_pokeball_stock()
        pokeballs_count[self.last_used_pokeball] -= self.catch_try
        pokeball = 0

        for i in range(3):
            if pokeballs_count[i] > 0:
                pokeball = i + 1
                break
        if pokeball == 0:
            # we are out of pokeballs
            self.logger.info(Fore.RED + 'Out of pokeballs :(')
            raise ValueError('Out of pokeballs')
        self.logger.info('Using Pokeball... (Total: %s)', pokeballs_count[pokeball-1])
        return pokeball

    def _make_action(self):
        pokemon_id = self._get_pokemon_id()

        self.logger.info(Fore.YELLOW + 'Trying to catch (%s) at position (%0.7f,%0.7f)', 
                         PokemonId.Name(pokemon_id),
                         self.data.latitude,
                         self.data.longitude)
        
        # do the encounter request
        encounter_response = self._make_encounter()
        if encounter_response.status not in [EncounterResponse.ENCOUNTER_SUCCESS,
                                             EncounterResponse.POKEMON_INVENTORY_FULL]:
            self.logger.info(Fore.RED + 'Encounter failed with reason %s', 
                             EncounterResponse.Status.Name(encounter_response.status))
            return False
        # check if we have inventory full
        elif encounter_response.status == EncounterResponse.POKEMON_INVENTORY_FULL:
            self.logger.info(Fore.RED + 'Pokemon inventory is full')
            return False

        catch_rate = encounter_response.capture_probability
        wpokemon = encounter_response.wild_pokemon

        # try to catch pokemon
        self.catch_try = 0
        while True:
            try:
                pokeball = self._choose_pokeball(catch_rate)
            except ValueError:
                return False
            
            # make catch pokemon request
            self.pokeapi.catch_pokemon(encounter_id=wpokemon.encounter_id,
                                       pokeball=pokeball,
                                       normalized_reticle_size=1.950,
                                       spawn_point_guid=wpokemon.spawnpoint_id,
                                       hit_pokemon=True,
                                       spin_modifier=1,
                                       NormalizedHitPosition=1)
            catch_pokemon_response = self.pokeapi.send_requests()

            # handle response
            if catch_pokemon_response.status == CatchPokemonResponse.CATCH_ERROR:
                self.logger.info(Fore.RED + 'Coudnt catch pokemon (%s) at (%0.7f, %0.7f), response code %s', 
                                  PokemonId.Name(wpokemon.pokemon_data.pokemon_id),
                                  wpokemon.latitude,
                                  wpokemon.longitude,
                                  CatchPokemonResponse.CatchStatus.Name(catch_pokemon_response.result))
                return False
            elif catch_pokemon_response.status == CatchPokemonResponse.CATCH_ESCAPE:
                self.logger.info(Fore.RED + 'Pokemon %s escaped', PokemonId.Name(wpokemon.pokemon_data.pokemon_id))
            elif catch_pokemon_response.status == CatchPokemonResponse.CATCH_FLEE:
                self.logger.info(Fore.RED + 'Pokemon %s fleed', PokemonId.Name(wpokemon.pokemon_data.pokemon_id))
            elif catch_pokemon_response.status == CatchPokemonResponse.CATCH_MISSED:
                self.logger.info('Missed pokeball, retrying...')
                self.catch_try += 1
                continue
            elif catch_pokemon_response.status == CatchPokemonResponse.CATCH_SUCCESS:
                # we sucessfuly catched pokemon
                cap_pok = DataPokemon(self.pokeapi, wpokemon.pokemon_data)
                self.logger.info(Fore.YELLOW + 'Captured pokemon (%s) [CP %s][IV %s/%s/%s][Potencial %s]', 
                                 PokemonId.Name(wpokemon.pokemon_data.pokemon_id),
                                 cap_pok.get_cp(),
                                 *cap_pok.get_iv(),
                                 cap_pok.get_iv_percentage())
                self.logger.info(Fore.CYAN + 'Capture award:')
                print_capture_award(self.logger, catch_pokemon_response.capture_award)
                Tasks(self.pokebot).task_transfer_pokemon(cap_pok)
                return True
            return False


class MapPokemonCatchAction(CatchPokemonAction):

    def _get_pokemon_id(self):
        """
        return pokemon id
        """
        return self.data.pokemon_id


class WildPokemonCatchAction(CatchPokemonAction):

    def _get_pokemon_id(self):
        """
        return pokemon id
        """
        return self.data.pokemon_data.pokemon_id

    def check_action(self):
        """
        Check action if is possible to execute before execution
        """
        return False

    def is_active(self):
        """
        wild pokemon is only for lookup
        """
        return False