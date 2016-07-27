import logging

from PokeApi.pokeapi import PokeApi
from PokeApi.auth import GoogleLogin, PTCLogin
from PokeApi.data import DataPlayer, DataInventory
from PokeApi.cache import Cache
from PokeBot.stepper import Stepper, ClosestStepper
from PokeBot.datamanager import DataManager
from PokeBot.algorithms import dijkstra_algorithm
from PokeBot.botconfig import BotConfig, SUPPORTED_PROVIDERS


class PokeBot(object):
    """ Main class of pokebot 
    """

    def __init__(self, config):
        """ Initialize the Master PokeBot
        """
        if not isinstance(config, BotConfig):
            raise TypeError('arg config is not type of class Config')
        
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.cache = Cache('cache_{}.json'.format(self.config.username))
        self.cache.cache_initialize()
        
        self.auth = self._authorize()
        self.pokeapi = PokeApi(self.auth, self.config.get_location_manager())
        self.stepper = Stepper(self)
        self.player = None
        self.inventory = None
        self.data_manager = None
        self.initialize()

    def _authorize(self):
        """ Authorize account with sprecified info from json file
        """
        # try to login with token
        """
        try:
            # TODO refresh token
            token = self.cache.get_cache('login.token')
            provider = self.cache.get_cache('login.provider')
            
            if provider == 'ptc':
                return PTCLogin().login_token(token)
            elif provider == 'google':
                return GoogleLogin().login_token(token)
        except Exception:
            self.logger.debug('Could not login with token')
        """

        if self.config.provider == 'ptc':
            return PTCLogin().login_user(self.config.username, self.config.password)
        elif self.config.provider == 'google':
            return GoogleLogin().login_user(self.config.username, self.config.password)
        else:
            self.logger.error('wrong provider specified')
            raise ValueError('%s: provider is not supported. Supported providers: %s',
                             self.config.provider, SUPPORTED_PROVIDERS)

    def initialize(self):
        """ Initialize bot
        """
        # send basic requests
        self.pokeapi.get_player()
        self.pokeapi.get_inventory()
        self.pokeapi.get_hatched_eggs()
        response = self.pokeapi.send_requests()

        # set basic types
        self.data_manager = DataManager(self)
        self.player = DataPlayer(self.pokeapi, response[0].player_data)
        self.inventory = DataInventory(self.pokeapi, response[1].inventory_delta)
        # TODO add hached eggs
        # self.hached_eggs = DataInventory(self.pokeapi, response[2].)
        # self.awarded_badges = DataInventory(self.pokeapi, response[3].)

        self.initialize_new_stepper(ClosestStepper(self, self.data_manager))

        # save cache login details
        self.cache.add_cache('login.token', self.auth.access_token)
        self.cache.add_cache('login.provider', self.auth.provider)
        self.cache.save()
    
    def initialize_new_stepper(self, stepper):
        self.stepper = stepper

    def update(self, delta_time):
        """ Update loop of the bot
        """
        # send hearthbeat
        hearthbeat_response = self.pokeapi.execute_heartbeat()
        # update player, inventory, hatched eggs, check_awarded_badges
        self.player.update(hearthbeat_response[0].player_data)
        # self.hatched_eggs.update(hearthbeat_response[1])
        self.inventory.update(hearthbeat_response[2].inventory_delta)
        # self.awarded_badges.update(hearthbeat_response[3])

        map_cells = hearthbeat_response[4].map_cells
        # update all data for pokemon, forts, ...
        self.data_manager.update(map_cells)
        # execute actions
        self.data_manager.execute_actions()
        # move to new location
        self.stepper.take_step(delta_time)
        #dijkstra_algorithm()

        self.cache.add_cache('location', '{},{}'.format(*self.pokeapi.location_manager.get_lat_lng()))
        self.cache.save()