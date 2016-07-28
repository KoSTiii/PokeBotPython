from PokeApi.data import basedata
import POGOProtos.Enums_pb2 as Enums_pb2
from POGOProtos.Data_pb2 import PokemonData
from POGOProtos.Networking.Responses_pb2 import ReleasePokemonResponse


class DataPokemon(basedata.BaseData):
    """
    """
    
    def __init__(self, api, pokemon_data):
        """
        """
        basedata.BaseData.__init__(self, api)
        self.pokemon = pokemon_data

    def __str__(self):
        """
        """
        return str(self.pokemon)

    def get_pokemon_name(self):
        """
        """
        return Enums_pb2.PokemonId.Name(self.pokemon.pokemon_id)

    def get_cp(self):
        """
        returns pokemons combat power
        """
        return self.pokemon.cp

    def get_iv(self):
        """
        return pokemons individual stats
        """
        return (self.pokemon.individual_attack, self.pokemon.individual_defense, self.pokemon.individual_stamina)

    def action_evolve_pokemon(self):
        """
        try evolve pokemon
        """
        pass

    def action_transfer_pokemon(self):
        """
        try transfer pokemon
        """
        self.logger.info('Start transfering pokemon: {} [CP {}, IV {}]'
                         .format(self.get_pokemon_name(), self.get_cp(), str(self.get_iv())))

        self.api.release_pokemon(pokemon_id=self.pokemon.pokemon_id)
        response = self.api.send_reaquests()

        # response is other than success
        if response.result != 1:
            self.logger.error('Coundnt transfer pokemon {}, Returned status {}'
                              .format(self.get_pokemon_name(), ReleasePokemonResponse.Result.Name(response.result)))  

        self.logger.info('Succesfuly transfered pokemon {}. Was awarded {} candy'
                         .format(self.get_pokemon_name(), response.candy_awarded))
        return response
