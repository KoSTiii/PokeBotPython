import logging

from PokeBot.pokebot import PokeBot


""" Base Stepper class for walking logic
"""
class Stepper(object):

    """ Initialize stepper class
    """
    def __init__(self, pokebot):
        self.logger = logging.getLogger(__name__)
        self.pokebot = pokebot
        self.steps = pokebot.botconfig.steps
        self.maxsteps = pokebot.botconfig.maxsteps

    """ Stepper main update method (take step)
    """
    def update(self, cell_ids):
        pass

