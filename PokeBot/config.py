import json

from PokeApi.locations import LocationManager


""" BotConfig is configuration for bot 
"""
class BotConfig(object):

    """ Initialize BotConfigs from json file
    """
    @classmethod
    def from_file(cls, json_file):
        configs = []
        fjson = json.load(open(json_file))

        # make bot configs objects
        for cfg in fjson:
            config = BotConfig(cfg['provider'],
                            cfg['username'],
                            cfg['password'],
                            cfg['location'],
                            cfg['cache'],
                            cfg['maxstep'],
                            cfg['step'])
            configs.append(config)

        return configs

    """ Initialize bot config
    """
    def __init__(self, provider, username, password, location, cache=True, maxstep=50, step=10):
        self.provider = provider
        self.username = username
        self.password = password
        self.location = location
        self.cache = cache
        self.maxsteps = maxstep
        self.step = step
    
    """ Return location in LocationManager class
    """
    def get_location_manager(self):
        coords = self.location.split(',')
        return LocationManager(float(coords[0]), float(coords[1]))
