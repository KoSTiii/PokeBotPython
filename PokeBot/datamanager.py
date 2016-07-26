from enum import Enum

from s2sphere import LatLng, Cell, CellId

from PokeApi.locations import Coordinates
from PokeBot.actions import Action, FortPokestopAction
from POGOProtos.Data import Gym_pb2


class DataType(Enum):
    """ Enum of all posible types that we monitoring
    """
    FORT_GYM = 0
    FORT_POKESTOP = 1
    WILD_POKEMON = 2
    CATCHABLE_POKEMON = 3
    NEARBY_POKEMON = 4


class DictData(object):
    """ Data stored in dictionary for pokemon/forts
    """

    def __init__(self, unique_id, data_type, action, data, lat, lon, distance):
        self.unique_id = unique_id
        self.data_type = data_type
        self.action = action
        self.data = data
        self.location = (lat, lon)
        self.distance = distance
        self.active = True
    
    def __str__(self):
        return str('DictData: id({}) type({})'.format(self.unique_id, str(self.data_type.name)))

    def try_action(self):
        if self.active and self.distance <= 40:
            if self.action.make_action():
                self.active = False
                return True
        return False


class DataManager(object):
    """
    """

    def __init__(self, pokebot):
        self.pokebot = pokebot
        self.loc = pokebot.pokeapi.location_manager
        self.unique_counter = 0
        self.dict = self.default_dict_values()
        self.action_classes = self.default_action_classes()

    def __str__(self):
        return str(self.dict)
    
    def default_dict_values(self):
        return {
            DataType.FORT_GYM.name: [],
            DataType.FORT_POKESTOP.name: [],
            DataType.WILD_POKEMON.name: [],
            DataType.CATCHABLE_POKEMON.name: [],
            DataType.NEARBY_POKEMON.name: []
        }

    def default_action_classes(self):
        return {
            DataType.FORT_GYM.name: Action,
            DataType.FORT_POKESTOP.name: FortPokestopAction,
            DataType.WILD_POKEMON.name: Action,
            DataType.CATCHABLE_POKEMON.name: Action,
            DataType.NEARBY_POKEMON.name: Action
        }

    def get_list_from_dict(self, data_type):
        return self.dict[data_type.name]

    def get_action_class(self, data_type):
        return self.action_classes[data_type.name]

    def get_counter(self):
        count = self.unique_counter
        self.unique_counter += 1
        return count

    def reset_counter(self):
        self.unique_counter = 0

    def update_forts(self, fort):
        """ update fort with new value. if we find new fort add to list
        """
        # check mode
        if self.pokebot.config.mode not in ['all', 'pokestop']:
            return

        # fort type is pokestop
        if fort.type == Gym_pb2.CHECKPOINT:
            pokestop_list = self.get_list_from_dict(DataType.FORT_POKESTOP)
            # get list item if we already have them saved
            list_fort = [item for item in pokestop_list if item.data.id == fort.id] # list comprehension

            # check if we already have this fort in list
            # if we already have fort update them (update distance)
            if list_fort:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
                list_fort[0].distance = dist
            # if we dont have fort add them
            else:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
                self.get_list_from_dict(DataType.FORT_POKESTOP).append(
                    DictData(self.get_counter(),
                             DataType.FORT_POKESTOP, 
                             self.get_action_class(DataType.FORT_POKESTOP)(self.pokebot, fort),
                             fort,
                             fort.latitude,
                             fort.longitude,
                             dist))

        # fort type is gym
        elif fort.type == Gym_pb2.GYM:
            """
            gym_list = self.get_list_from_dict(DataType.FORT_GYM)

            dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
            self.get_list_from_dict(DataType.FORT_GYM).append(
                DictData(self.get_counter(), DataType.FORT_GYM, fort, fort.latitude, fort.longitude, dist))
            """

    def update_pokemons(self, pokemon):
        """ Update pokemon in dict
        """
        # check mode
        if self.pokebot.config.mode not in ['all', 'pokemon']:
            return
        

    def update_dict(self, map_cells):
        """ Start updating dictionary with new values or add existing values
        """
        # update all dicts
        for cell in map_cells:
            # update forts
            for fort in cell.forts:
                self.update_forts(fort)

            # update wild pokemons
            for wpokemon in cell.wild_pokemons:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), wpokemon.latitude, wpokemon.longitude)
                self.get_list_from_dict(DataType.WILD_POKEMON).append(
                    DictData(self.get_counter(),
                             DataType.WILD_POKEMON,
                             self.get_action_class(DataType.WILD_POKEMON)(self.pokebot, wpokemon),
                             wpokemon,
                             wpokemon.latitude,
                             wpokemon.longitude,
                             dist))

            # update catchable pokemon
            for cpokemon in cell.catchable_pokemons:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), cpokemon.latitude, cpokemon.longitude)
                self.get_list_from_dict(DataType.CATCHABLE_POKEMON).append(
                    DictData(self.get_counter(),
                             DataType.CATCHABLE_POKEMON,
                             self.get_action_class(DataType.CATCHABLE_POKEMON)(self.pokebot, cpokemon),
                             cpokemon,
                             cpokemon.latitude,
                             cpokemon.longitude,
                             dist))

            # update nearby pokemons
            for npokemon in cell.nearby_pokemons:
                npokemon_pos = LatLng.from_point(Cell(CellId(cell.s2_cell_id)).get_center())
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), npokemon_pos.lat().degrees, npokemon_pos.lng().degrees)
                self.get_list_from_dict(DataType.NEARBY_POKEMON).append(
                    DictData(self.get_counter(),
                             DataType.NEARBY_POKEMON,
                             self.get_action_class(DataType.NEARBY_POKEMON)(self.pokebot, npokemon),
                             npokemon,
                             npokemon_pos.lat().degrees,
                             npokemon_pos.lng().degrees,
                             dist))
        
        # execute all actions
        items_to_execute_action = self.sorted_items(self.pokebot.config.mode)
        for item in items_to_execute_action:
            item.try_action()

    def items(self, mode):
        """ available modes all|pokemon|pokestop
        """
        result = []
        if mode in ['all', 'pokestop']:
            result += self.get_list_from_dict(DataType.FORT_POKESTOP)

        if mode in ['all', 'pokemon']:
            result += self.get_list_from_dict(DataType.WILD_POKEMON) \
                    + self.get_list_from_dict(DataType.CATCHABLE_POKEMON) \
                    + self.get_list_from_dict(DataType.NEARBY_POKEMON)
        # return result
        return [item for item in result if item.active]

    def sorted_items(self, mode):
        items = self.items(mode)
        items.sort(key=lambda obj: obj.distance)
        return items

