import PokeApi.data.basedata as basedata
from POGOProtos.Inventory_pb2 import InventoryDelta


"""
"""
class Inventory(basedata.BaseData):
    
    def __init__(self, api, inventory_delta):
        basedata.BaseData.__init__(api)
        if not isinstance(inventory_delta, InventoryDelta):
            raise ValueError('inventory_delta is not type of InventoryDelata')
        self.inventory = inventory_delta

    def __str__(self):
        return str(self.inventory)
    
    def update_inventory(self):
        # TODO implement update inventory
        raise NotImplementedError