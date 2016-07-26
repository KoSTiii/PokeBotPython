import logging
import random

from PokeApi.locations import Coordinates


def steps_to_meters(steps):
    return steps * 0.762

def maters_to_steps(meters):
    return meters * 1.312


""" Base Stepper class for walking logic
"""
class Stepper(object):

    # standard deviation for steps
    STEP_STD_DEV = 3.7873

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

        if course > 360:
            course = 360 - course
        if course < 0:
            course = 360 + course
        self._last_course = course
        return course

    """ Change walk pace to make more humanish
    """
    def get_speed(self):
        return random.uniform(self.steps - Stepper.STEP_STD_DEV, self.steps + Stepper.STEP_STD_DEV)

    """ Stepper main update method (take step)
    update main location and also return it
    """
    def take_step(self, delta_time):
        steps_made = self.get_speed() * delta_time
        dist_in_meters = steps_to_meters(steps_made)
        course = self.get_course()
        new_pos = Coordinates.extrapolate(self.loc.get_latitude(),
                                          self.loc.get_longitude(),
                                          course,
                                          dist_in_meters)
        
        self.logger.debug('Steps made %s, course %s degree in %s seconds. From position (%s, %s) to position (%s, %s)',
            steps_made, course, delta_time, self.loc.get_latitude(), self.loc.get_longitude(), *new_pos)
        
        self.loc.set_location(*new_pos, 0)
        return new_pos


class ClosestStepper(Stepper):

    def __init__(self, pokebot, datamanager):
        Stepper.__init__(self, pokebot)
        self.datamanager = datamanager
        self.mode = self.pokebot.config.mode

    """ Return course to the closest object
    """
    def get_course(self):
        items = self.datamanager.sorted_items(self.mode)
        if items:
            destination = items[0]
            course = Coordinates.angle_between_coords(*self.loc.get_lat_lng(), *destination.location)

            self.logger.info('Walking to (%s, %s) which is %s)', *destination.location, destination.data_type.name)

            return course
        else:
            return Stepper.get_course(self)


""" Calculate the best route to go find pokemons and forts
if nothing is close by use Stepper class to move
"""
class DijkstraStepper(Stepper):

    def __init__(self, pokebot):
        Stepper.__init__(self, pokebot)

    def get_course(self):
        return 0

