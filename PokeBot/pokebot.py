import time
import logging

from PokeApi.auth import PTCLogin, Auth


""" Main class of pokebot 
"""
class PokeBot():

    """
    """
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)

        self.pokeapi = None

    """
    """
    def init_config(self):
        pass