import logging
import random

from PokeApi.locations import Coordinates
from PokeBot.helpers import clamp


def steps_to_meters(steps):
    return steps * 0.762

def maters_to_steps(meters):
    return meters * 1.312


""" Base Stepper class for walking logic
"""
class Stepper(object):

    # standard deviation for steps
    STEP_STD_DEV = 2

    """ Initialize stepper class
    """
    def __init__(self, pokebot):
        self.logger = logging.getLogger(__name__)
        self.pokebot = pokebot
        self.loc = pokebot.pokeapi.location_manager
        self.steps = pokebot.config.steps
        self.maxsteps = pokebot.config.maxsteps

        self._last_bearing = random.randint(0, 360)

    def _update(self):
        """
        Update items each tick
        """

    def get_bearing(self):
        """ return heading bearing in deggress (0 - 360)
        """
        random_bearing = random.randint(-45, 45)
        bearing = self._last_bearing + random_bearing

        if bearing > 360:
            bearing = 360 - bearing
        if bearing < 0:
            bearing = 360 + bearing
        self._last_bearing = bearing
        return bearing
    
    def get_speed(self):
        """ Change walk pace to make more humanish
        """
        return random.uniform(self.steps - Stepper.STEP_STD_DEV, self.steps + Stepper.STEP_STD_DEV)

    def get_distance(self, maxdistance):
        """
        return distance in meters to fine tune positioning
        """
        return maxdistance
    

    def take_step(self, delta_time):
        """ Stepper main update method (take step)
        update main location and also return it
        """
        steps_made = self.get_speed() * delta_time
        dist_in_meters = steps_to_meters(steps_made)

        self._update()
        distance = self.get_distance(dist_in_meters)
        bearing = self.get_bearing()
        new_pos = Coordinates.extrapolate(self.loc.get_latitude(),
                                          self.loc.get_longitude(),
                                          bearing,
                                          distance)
        
        self.logger.info('Moved %0.2fm, bearing %s degree in %0.2f seconds. From position (%0.7f, %0.7f) to position (%0.7f, %0.7f)',
            distance, bearing, delta_time, self.loc.get_latitude(), self.loc.get_longitude(), *new_pos)
        
        self.loc.set_location(*new_pos, 0)
        return new_pos


class ClosestStepper(Stepper):

    def __init__(self, pokebot, datamanager):
        super().__init__(pokebot)
        self.datamanager = datamanager
        self.mode = self.pokebot.config.mode
        self.items = None

    def _update(self):
        """
        Update items each tick
        """
        self.items = self.datamanager.sorted_items(self.mode)

    def get_distance(self, maxdistance):
        """
        return max distance if object distance > maxdistance
        """
        if self.items:
            self.logger.debug('Distance: %s', clamp(self.items[0].distance, 0, maxdistance))
            return clamp(self.items[0].distance, 0, maxdistance)
        return super().get_distance(maxdistance)

    """ Return bearing to the closest object
    """
    def get_bearing(self):
        if self.items:
            destination = self.items[0]
            bearing = Coordinates.angle_between_coords(*self.loc.get_lat_lng(), *destination.location)

            self.logger.info('Walking to (%0.7f, %0.7f, %0.2fm) which is %s', 
                             *destination.location,
                             destination.distance,
                             destination.data_type.name)

            return bearing
        else:
            return super().get_bearing()


""" Calculate the best route to go find pokemons and forts
if nothing is close by use Stepper class to move
"""
class DijkstraStepper(Stepper):

    def __init__(self, pokebot):
        super().__init__(pokebot)

    def get_bearing(self):
        return 0

