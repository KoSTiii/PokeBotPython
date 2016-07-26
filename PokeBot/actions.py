import logging

from POGOProtos.Inventory_pb2 import ItemId
from POGOProtos.Networking.Responses_pb2 import FortSearchResponse


class Action(object):
    """
    Base Action class for handling actions
    """

    def __init__(self, pokebot, data):
        self.logger = logging.getLogger(__name__)
        self.pokebot = pokebot
        self.data = data
        self.pokeapi = self.pokebot.pokeapi
        self.loc = self.pokeapi.location_manager

    def make_action(self):
        raise NotImplementedError


class FortPokestopAction(Action):
    """
    Action for spining the pokestop
    """

    def __init__(self, pokebot, data):
        Action.__init__(self, pokebot, data)

    def make_action(self):
        self.logger.info('Spining fort at position (%s,%s), my position (%s,%s)', 
                         self.data.latitude,
                         self.data.longitude,
                         self.loc.latitude,
                         self.loc.longitude)
        self.pokeapi.fort_search(fort_id=self.data.id, 
                                 player_latitude=self.loc.get_latitude(), 
                                 player_longitude=self.loc.get_longitude(), 
                                 fort_latitude=self.data.latitude, 
                                 fort_longitude=self.data.longitude)
        resp = self.pokeapi.send_requests()
        if resp.result != 1:
            self.logger.error('Coudnt spin pokestop at (%s, %s), response code %s', 
                              self.data.latitude,
                              self.data.longitude,
                              FortSearchResponse.Result.Name(resp.result))
            return False

        self.logger.info('Finished spining fort, Loot:')
        self.logger.info('%s xp', resp.experience_awarded)
        for item in resp.items_awarded:
            self.logger.info('%sx %s (Total: %s)',
                             item.item_count,
                             ItemId.Name(item.item_id),
                             self.pokebot.inventory.get_items_count(item.item_id))
        return True


class CatchPokemonAction(Action):
    """
    """

    def __init__(self, pokebot, data):
        Action.__init__(self, pokebot, data)
