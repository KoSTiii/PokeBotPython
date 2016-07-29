from POGOProtos.Enums_pb2 import PokemonId


class Tasks(object):

    def __init__(self, pokebot):
        self.pokebot = pokebot
        self.pokeapi = pokebot.pokeapi
        self.config = pokebot.config

    def task_transfer_pokemon(self, data_pokemon):
        """
        release pokemon if all conditions are met specified in config file
        """
        release_pokemon_config = self.config.pokemon_config.get_pokemon_config(
            data_pokemon.get_pokemon_name())

        cp = data_pokemon.get_cp()
        iv = data_pokemon.get_iv_percentage()

        # if we have any config file available
        if release_pokemon_config:
            func = release_pokemon_config.get_logic_function()
            if func(cp < release_pokemon_config.release_under_cp,
                    iv < release_pokemon_config.release_under_iv):
                data_pokemon.action_transfer_pokemon()

        