import logging

from PokeApi.pokeapi import PokeApi
from PokeApi.auth import GoogleLogin, PTCLogin
from PokeApi.data import DataPlayer, DataInventory, InventoryType
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

    def _print_account_info(self):
        self.logger.info('--------------------')
        self.logger.info('')
        self.logger.info('Player: %s', self.player.get_username())
        self.logger.info('Level: %s', self.inventory.get_player_stats().level)
        self.logger.info('Acccount Creation: %s', self.player.get_creation_time())
        self.logger.info('Bag Storage: %s/%s', 
                          self.inventory.get_item_storage(),
                          self.player.get_max_item_storage())
        self.logger.info('Pokemon Storage: %s/%s',
                          self.inventory.get_pokemon_storage(),
                          self.player.get_max_pokemon_storage())

        currencies = self.player.get_currencies()
        for curr in currencies:
            self.logger.info('%s: %s', curr, currencies[curr])

        pokeballs = self.inventory.get_pokeball_stock()
        self.logger.info('PokeBalls: %s', pokeballs[0])
        self.logger.info('GreatBalls: %s', pokeballs[1])
        self.logger.info('UltraBalls: %s', pokeballs[2])
        self.logger.info('')
        self.logger.info('Mode: ' + self.config.mode)
        self.logger.info('--------------------')

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

        self._print_account_info()
        
    
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
        # move to new location
        self.stepper.take_step(delta_time)
        # execute actions
        self.data_manager.execute_actions()
        # delete all data
        self.data_manager.reset_dict_data()

        self.cache.add_cache('location', '{},{}'.format(*self.pokeapi.location_manager.get_lat_lng()))
        self.cache.save()