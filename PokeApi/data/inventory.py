"""
"""

from PokeApi.data import basedata

from POGOProtos import Inventory_pb2
from POGOProtos.Inventory_pb2 import ItemId


class DataInventory(basedata.BaseData):
    """
    """
    
    def __init__(self, api, inventory_delta):
        """
        """
        basedata.BaseData.__init__(self, api, inventory_delta)

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
        