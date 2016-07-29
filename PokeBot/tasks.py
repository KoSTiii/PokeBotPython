import time, logging

from PokeApi.data import DataPokemon
from POGOProtos.Enums_pb2 import PokemonId


class Tasks(object):

    def __init__(self, pokebot):
        self.pokebot = pokebot
        self.pokeapi = pokebot.pokeapi
        self.config = pokebot.config
        self.logger = logging.getLogger(__name__)

    def task_transfer_pokemons(self):
        """
        release pokemon if all conditions are met specified in config file
        """
        #self.logger.debug('Started transfering pokemon')
        pause = False
        poke_storage = self.pokebot.inventory.get_pokemon_storage()
        for pokemon in poke_storage:
            data_pokemon = DataPokemon(self.pokeapi, pokemon)

            release_pokemon_config = self.config.pokemon_config.get_pokemon_config(
                data_pokemon.get_pokemon_name())

            cp = data_pokemon.get_cp()
            iv = data_pokemon.get_iv_percentage()

            # if we have any config file available
            if release_pokemon_config:
                if pause:
                    # sleep for one second for second transfer
                    time.sleep(1)
                
                # release pokemon if it met the conditions
                func = release_pokemon_config.get_logic_function()
                if func(cp < release_pokemon_config.release_under_cp,
                        iv < release_pokemon_config.release_under_iv):
                    data_pokemon.action_transfer_pokemon()
                    pause = True

        