import logging

from PokeApi.pokeapi import PokeApi
from PokeApi.auth import GoogleLogin, PTCLogin
from PokeApi.data import DataPlayer, DataInventory
from PokeBot.stepper import Stepper, ClosestStepper
from PokeBot.datamanager import DataManager
from PokeBot.algorithms import dijkstra_algorithm
from PokeBot.botconfig import BotConfig, SUPPORTED_PROVIDERS


""" Main class of pokebot 
"""
class PokeBot(object):

    """ Initialize the Master PokeBot
    """
    def __init__(self, config):
        if not isinstance(config, BotConfig):
            raise TypeError('arg config is not type of class Config')
        
        self.logger = logging.getLogger(__name__)
        self.config = config
        
        self.auth = self._authorize()
        self.pokeapi = PokeApi(self.auth, self.config.get_location_manager())
        self.stepper = Stepper(self)
        self.player = None
        self.inventory = None
        self.data_manager = None
        self.initialize()

    """ Authorize account with sprecified info from json file
    """
    def _authorize(self):
        if self.config.provider == 'ptc':
            return PTCLogin().login_user(self.config.username, self.config.password)
        elif self.config.provider == 'google':
            return GoogleLogin().login_user(self.config.username, self.config.password)
        else:
            self.logger.error('wrong provider specified')
            raise ValueError('{0}: provider is not supported. Supported providers: {1}'
                             .format(self.config.provider, SUPPORTED_PROVIDERS))

    """ Initialize bot
    """
    def initialize(self):
        # send basic requests
        self.pokeapi.get_player()
        self.pokeapi.get_inventory()
        self.pokeapi.get_hatched_eggs()
        response = self.pokeapi.send_requests()

        # set basic types
        self.data_manager = DataManager(self)
        self.player = DataPlayer(self.pokeapi, response[0].player_data)
        self.inventory = DataInventory(self.pokeapi, response[1].inventory_delta)

        self.initialize_new_stepper(ClosestStepper(self, self.data_manager))
        # TODO add hached eggs
        # self.hached_eggs = 
        # self.awarded_badges = 
    
    def initialize_new_stepper(self, stepper):
        self.stepper = stepper

    """ Update loop of the bot
    """
    def update(self, delta_time):
        # send hearthbeat
        hearthbeat_response = self.pokeapi.execute_heartbeat()
        # update player, inventory, hatched eggs, check_awarded_badges
        self.player.update(hearthbeat_response[0].player_data)
        # self.hatched_eggs.update(hearthbeat_response[1])
        self.inventory.update(hearthbeat_response[2].inventory_delta)
        # self.awarded_badges.update(hearthbeat_response[3])

        map_cells = hearthbeat_response[4].map_cells
        # update all data for pokemon, forts, ...
        self.data_manager.update_dict(map_cells)
        #self.logger.info(map_cells)

        self.stepper.take_step(delta_time)
        #dijkstra_algorithm()