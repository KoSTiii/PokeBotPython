import logging

from PokeApi.pokeapi import PokeApi
from PokeApi.auth import GoogleLogin, PTCLogin
from PokeBot.config import BotConfig, SUPPORTED_PROVIDERS


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

    """ Authorize account with sprecified info from json file
    """
    def _authorize(self):
        if self.config.provider is 'ptc':
            return PTCLogin().login_user(self.config.username, self.config.password)
        elif self.config.provider is 'google':
            return GoogleLogin().login_user(self.config.username, self.config.password)
        else:
            self.logger.error('wrong provider specified')
            raise ValueError('{0}: provider is not supported. Supported providers: {1}'
                             .format(self.config.provider, SUPPORTED_PROVIDERS))

    """ Update bot
    """
    def update(self):
        pass