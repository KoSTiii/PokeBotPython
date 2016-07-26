"""
"""

from PokeApi.data import basedata
from POGOProtos.Inventory_pb2 import InventoryDelta


class DataInventory(basedata.BaseData):
    """
    """
    
    def __init__(self, api, inventory_delta):
        """
        """
        basedata.BaseData.__init__(self, api)
        if not isinstance(inventory_delta, InventoryDelta):
            raise ValueError('inventory_delta is not type of InventoryDelata')
        self.inventory = inventory_delta

    def __str__(self):
        """
        """
        return str(self.inventory)
    
    def update(self, inv=None):
        """
        """
        if inv:
            self.inventory = inv
        else:
            self.api.get_inventory()
            resp = self.api.send_requests()
            self.inventory = resp.inventory_delta