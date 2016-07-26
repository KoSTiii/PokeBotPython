"""
"""

from PokeApi.data import basedata
from POGOProtos.Inventory_pb2 import ItemId
from POGOProtos.Networking.Responses_pb2 import FortSearchResponse


class DataFort(basedata.BaseData):
    """
    """
    
    def __init__(self, api, fort_data):
        """
        """
        basedata.BaseData.__init__(self, api, fort_data)
        self.loc = self.api.location_manager

    def __str__(self):
        """
        """
        return str(self.data)
    
    def update(self, fort=None):
        """
        """
        if fort:
            self.data = fort
        else:
            pass

    def spin_fort(self):
        self.logger.info('Spining fort at position (%s,%s), my position (%s,%s)', 
                         self.data.latitude,
                         self.data.longitude,
                         self.api.lo.latitude,
                         self.loc.longitude)
        self.api.fort_search(fort_id=self.data.id, 
                                 player_latitude=self.loc.get_latitude(), 
                                 player_longitude=self.loc.get_longitude(), 
                                 fort_latitude=self.data.latitude, 
                                 fort_longitude=self.data.longitude)
        resp = self.api.send_requests()
        if resp.result != 1:
            self.logger.error('Coudnt spin pokestop at (%s, %s), response code %s', 
                              self.data.latitude,
                              self.data.longitude,
                              FortSearchResponse.Result.Name(resp.result))
            return False

        self.logger.info('Finished spining fort, Loot:')
        self.logger.info('%s xp', resp.experience_awarded)
        for item in resp.items_awarded:
            self.logger.info('%sx %s',
                             item.item_count,
                             ItemId.Name(item.item_id))
        return True