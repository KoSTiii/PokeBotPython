import time
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
        # set from dict data
        self.dict_data = None


    def do_action(self):
        """
        Do action if check_action() return True
        """
        if self.check_action():
            self._make_action()

    def is_active(self):
        """
        Check if this item is active
        """
        return False

    def check_action(self):
        """
        Check action if is possible to execute before execution
        """
        return False

    def _make_action(self):
        """
        action exetution method
        """
        return False


class FortPokestopAction(Action):
    """
    Action for spining the pokestop
    """

    def __init__(self, pokebot, data):
        Action.__init__(self, pokebot, data)

    def is_active(self):
        """
        Check if pokestop is enabled and is not on cooldown
        """
        if self.data.cooldown_complete_timestamp_ms:
            fort_cooldown = self.data.cooldown_complete_timestamp_ms / 1000.0
            diff = time.time() - fort_cooldown
            # if diif is less than 0 means that fort is on cooldown
            if diff < 0:
                return False
        
        if self.data.enabled:
            return True
        return False

    def check_action(self):
        """
        if pokestop is acvtive and distance is less than 40
        """
        if self.is_active() and self.dict_data.distance <= 40:
            return True
        return False

    def _make_action(self):
        self.logger.info('Spining pokestop (%s) at position (%s,%s)', 
                         self.data.id,
                         self.data.latitude,
                         self.data.longitude)
        self.pokeapi.fort_search(fort_id=self.data.id, 
                                 player_latitude=self.loc.get_latitude(), 
                                 player_longitude=self.loc.get_longitude(), 
                                 fort_latitude=self.data.latitude, 
                                 fort_longitude=self.data.longitude)
        resp = self.pokeapi.send_requests()
        if resp.result != 1:
            self.logger.error('Coudnt spin pokestop (%s) at (%s, %s), response code %s', 
                              self.data.id,
                              self.data.latitude,
                              self.data.longitude,
                              FortSearchResponse.Result.Name(resp.result))
            return False

        self.logger.info('Finished spining fort (%s)', self.data.id)
        self.logger.info('Loot:')
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
