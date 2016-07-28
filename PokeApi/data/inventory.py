"""
"""
from enum import Enum

from colorama import Fore

from PokeApi.helper import print_items_awarded
from PokeApi.data import basedata
from POGOProtos import Inventory_pb2
from POGOProtos.Inventory_pb2 import ItemId

class InventoryType(Enum):
    PLAYER_STATS = 'player_stats'
    POKEMON_DATA = 'pokemon_data'
    POKEMON_FAMILY = 'pokemon_family'
    POKEDEX_ENTRY = 'pokedex_entry'
    ITEM = 'item'


class DataInventory(basedata.BaseData):
    """
    """
    
    def __init__(self, api, inventory_delta):
        """
        """
        basedata.BaseData.__init__(self, api, inventory_delta)
        self._last_level = self.get_player_stats().level
        self.action_level_up_rewards()

    def __str__(self):
        """
        """
        return str(self.data)
    
    def update(self, inv=None):
        """
        """
        if inv:
            self.data = inv
        else:
            self.api.get_inventory()
            resp = self.api.send_requests()
            self.data = resp.inventory_delta
        
        # check if we leveled up
        if self._last_level != self.get_player_stats().level:
            self._last_level = self.get_player_stats().level
            self.action_level_up_rewards()

    def get_player_stats(self):
        """
        get player level
        """
        player_stats = self.get_inventory_items(InventoryType.PLAYER_STATS)
        return player_stats[0]

    def get_item_storage(self):
        items = self.get_inventory_items(InventoryType.ITEM)
        count = 0
        for item in items:
            count += item.count
        return count
    
    def get_pokemon_storage(self):
        pokemons = self.get_inventory_items(InventoryType.POKEMON_DATA)
        poke_witout_eggs = [poke for poke in pokemons if not poke.is_egg]
        return len(poke_witout_eggs)

    def get_inventory_items(self, inventory_type):
        """
        retrun list of items in invetory which are type of InventoryType
        """
        values = []
        for inv_item in self.data.inventory_items:
            if inv_item.inventory_item_data.HasField(inventory_type.value):
                values.append(getattr(inv_item.inventory_item_data, inventory_type.value))
        return values

    def get_items_count(self, item_id):
        for inv in self.data.inventory_items:
            if inv.inventory_item_data:
                if inv.inventory_item_data.item:
                    # return this item count
                    if inv.inventory_item_data.item.item_id == item_id:
                        return inv.inventory_item_data.item.count
        return 0

    def get_pokeball_stock(self):
        """
        return tuple of pokeball stock (pokeball, greatball, ultraball)
        """
        pokeball = self.get_items_count(Inventory_pb2.ITEM_POKE_BALL)
        greatball = self.get_items_count(Inventory_pb2.ITEM_GREAT_BALL)
        ultraball = self.get_items_count(Inventory_pb2.ITEM_ULTRA_BALL)
        return [pokeball, greatball, ultraball]

    def action_level_up_rewards(self):
        self.api.level_up_rewards(level=self._last_level)
        resp = self.api.send_requests()
        
        if resp.result == 1:
            self.logger.info(Fore.GREEN + 'Level Up Rewards: ')
            print_items_awarded(self.logger, self, resp.items_awarded)

    def action_delete_item(self, item_id, count):
        pass
