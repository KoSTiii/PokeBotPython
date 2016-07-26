import logging
import random

from PokeApi.locations import Coordinates

# standard deviation for steps
STEP_STD_DEV = 3.7873


""" Base Stepper class for walking logic
"""
class Stepper(object):

    """ Initialize stepper class
    """
    def __init__(self, pokebot):
        self.logger = logging.getLogger(__name__)
        self.pokebot = pokebot
        self.loc = pokebot.pokeapi.location_manager
        self.steps = pokebot.config.steps
        self.maxsteps = pokebot.config.maxsteps

        self._last_course = random.randint(0, 360)

    """ return heading course in deggress (0 - 360)
    """
    def get_course(self):
        random_course = random.randint(-60, 60)
        course = self._last_course + random_course

        if course >= 360:
            course = 360 - course
        elif course < 0:
            course = 360 + course
        self._last_course = course
        return course

    """ Change walk pace to make more humanish
    """
    def get_speed(self):
        return random.uniform(self.steps - STEP_STD_DEV, self.steps + STEP_STD_DEV)

    """ Stepper main update method (take step)
    update main location and also return it
    """
    def take_step(self, delta_time):
        steps_made = self.get_speed() * delta_time
        dist_in_meters = steps_made * 0.762 # convert steps to m
        course = self.get_course()
        new_pos = Coordinates.extrapolate(self.loc.get_latitude(),
                                          self.loc.get_longitude(),
                                          course,
                                          dist_in_meters)
        self.logger.debug('Steps made {}, course {} degree in {} seconds. From position ({}, {}) to position ({}, {})'.format(
            steps_made, course, delta_time, self.loc.get_latitude(), self.loc.get_longitude(), *new_pos))
        self.loc.set_location(*new_pos, 0)
        return new_pos


""" Calculate the best route to go find pokemons and forts
if nothing is close by use Stepper class to move
"""
class DijkstraStepper(Stepper):

    def __init__(self, pokebot):
        Stepper.__init__(self, pokebot)

    def get_direction(self):
        return 0

