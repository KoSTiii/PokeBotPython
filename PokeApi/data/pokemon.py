from colorama import Fore

from PokeApi.data import basedata
import POGOProtos.Enums_pb2 as Enums_pb2
from POGOProtos.Data_pb2 import PokemonData
from POGOProtos.Networking.Responses_pb2 import ReleasePokemonResponse, EvolvePokemonResponse


class DataPokemon(basedata.BaseData):
    """
    """
    
    def __init__(self, api, pokemon_data):
        """
        """
        basedata.BaseData.__init__(self, api, pokemon_data)

    def __str__(self):
        """
        """
        return str(self.data)

    def is_egg(self):
        return self.data.is_egg

    def get_pokemon_name(self):
        """
        """
        return Enums_pb2.PokemonId.Name(self.data.pokemon_id)

    def get_cp(self):
        """
        returns pokemons combat power
        """
        return self.data.cp

    def get_iv(self):
        """
        return pokemons individual stats
        """
        return (self.data.individual_attack, self.data.individual_defense, self.data.individual_stamina)

    def get_iv_percentage(self):
        iv = self.get_iv()
        total_IV = iv[0] + iv[1] + iv[2]
        return round((total_IV / 45.0), 2)

    def get_pokemon_id_family_id(self):
        return self.data.pokemon_id

    def action_evolve_pokemon(self):
        """
        try evolve pokemon
        """
        self.logger.info(Fore.GREEN + 'Evolving pokemon: %s [CP %s][IV %s/%s/%s][Potencial: %s]',
                         self.get_pokemon_name(), self.get_cp(), *self.get_iv(), self.get_iv_percentage())
        
        self.api.evolve_pokemon(pokemon_id=self.data.id)
        response = self.api.send_requests()

        # response is other than success
        if response.result != 1:
            self.logger.error(Fore.RED + 'Cound not evolve pokemon %s, Returned status %s',
                              self.get_pokemon_name(), EvolvePokemonResponse.Result.Name(response.result))
            return None

        self.logger.info(Fore.CYAN + 'Evolve succeded pokemon %s.',
                         self.get_pokemon_name())
        self.logger.info(Fore.CYAN + '%sx exp', response.experience_awarded)
        self.logger.info(Fore.CYAN + '%sx candy awarded', response.candy_awarded)
        self.data.CopyFrom(response.evolved_pokemon_data)
        return response

    def action_transfer_pokemon(self):
        """
        try transfer pokemon
        """
        self.logger.info(Fore.GREEN + 'Transfering pokemon: %s [CP %s][IV %s/%s/%s][Potencial: %s]',
                         self.get_pokemon_name(), self.get_cp(), *self.get_iv(), self.get_iv_percentage())

        self.api.release_pokemon(pokemon_id=self.data.id)
        response = self.api.send_requests()

        # response is other than success
        if response.result != 1:
            self.logger.error(Fore.RED + 'Cound not transfer pokemon %s, Returned status %s',
                              self.get_pokemon_name(), ReleasePokemonResponse.Result.Name(response.result))
            return None

        self.logger.info(Fore.CYAN + 'Transfer succeded pokemon %s. Was awarded %s candy',
                         self.get_pokemon_name(), response.candy_awarded)
        return response
