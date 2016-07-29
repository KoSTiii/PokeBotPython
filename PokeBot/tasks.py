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
    
    def task_delete_items(self):
        """
        delete all items that are not in config or excecd this number
        """
        items = self.pokebot.inventory.get_item_storage()
        pause = False

        for item in items:
            if pause:
                time.sleep(1)

            item_config = self.config.item_config.get_item_config(item)
            if item_config:
                # we specified maximum items to keep in inventory
                if item_config.max_keep_items:
                    item_del_count = item.count - item_config.max_keep_items

                    # if we have more items than specifiedl then delete it
                    if item_del_count > 0:
                        self.pokebot.inventory.action_delete_item(item, item_del_count)
                        pause = True
                # if not max_keep_items then delete all        
                elif item.count > 0:
                    self.pokebot.inventory.action_delete_item(item, item.count)
                    pause = True

        