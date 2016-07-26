import logging


class Action(object):
    """
    Base Action class for handling actions
    """

    def __init__(self, pokebot):
        self.logger = logging.getLogger(__name__)
        self.pokebot = pokebot
        self.pokeapi = self.pokebot.pokeapi
        self.loc = self.pokeapi.location_manager

    def make_action(self):
        pass


class FortPokestopAction(Action):
    """
    Action for spining the pokestop
    """

    def __init__(self, pokebot, fort):
        Action.__init__(self, pokebot)
        self.fort = fort

    def make_action(self):
        self.logger.info('Spining fort at position (%s,%s)', self.loc.latitude, self.loc.longitude)
        self.pokeapi.fort_search(fort_id=self.fort.id, 
                                 player_latitude=self.loc.get_latitude(), 
                                 player_longitude=self.loc.get_longitude(), 
                                 fort_latitude=self.fort.latitude, 
                                 fort_longitude=self.fort.longitude)
        resp = self.pokeapi.send_requests()
        self.logger.info('Finished spining fort response %s', str(resp))
