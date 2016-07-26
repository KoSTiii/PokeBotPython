from enum import Enum

from s2sphere import LatLng, Cell, CellId

from PokeApi.locations import Coordinates
from POGOProtos.Data import Gym_pb2


""" Enum of all posible types that we monitoring
"""
class DataType(Enum):
    FORT_GYM = 0
    FORT_POKESTOP = 1
    WILD_POKEMON = 2
    CATCHABLE_POKEMON = 3
    NEARBY_POKEMON = 4


"""
"""
class DictData(object):

    def __init__(self, unique_id, data_type, data, lat, lon, distance):
        self.unique_id = unique_id
        self.data_type = data_type
        self.data = data
        self.location = (lat, lon)
        self.distance = distance
        self.active = True
    
    def __str__(self):
        return str('id:{};data:{}'.format(self.unique_id, str(self.data)))


"""
"""
class DataManager(object):

    def __init__(self, pokebot):
        self.pokebot = pokebot
        self.loc = pokebot.pokeapi.location_manager
        self.unique_counter = 0
        self.dict = self.default_dict_values()

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

    def get_list_from_dict(self, data_type):
        return self.dict[data_type.name]

    def get_counter(self):
        count = self.unique_counter
        self.unique_counter += 1
        return count

    def reset_counter(self):
        self.unique_counter = 0

    """ update fort with new value. if we find new fort add to list
    """
    def update_forts(self, fort):
        # fort type is pokestop
        if fort.type == Gym_pb2.CHECKPOINT:
            pokestop_list = self.get_list_from_dict(DataType.FORT_POKESTOP)
            # get list item if we already have them saved
            list_fort = (item for item in pokestop_list if item.data.id == fort.id) # generator comprehension

            # check if we already have this fort in list
            # if we already have fort update them ()update distance
            if list_fort:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
                list_fort[0].distance = dist
            # if we dont have fort add them
            else:
                """
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
                self.get_list_from_dict(DataType.FORT_POKESTOP).append(
                    DictData(self.get_counter(), DataType.FORT_POKESTOP, fort, fort.latitude, fort.longitude, dist))
                """

        # fort type is gym
        elif fort.type == Gym_pb2.GYM:
            """
            gym_list = self.get_list_from_dict(DataType.FORT_GYM)

            dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
            self.get_list_from_dict(DataType.FORT_GYM).append(
                DictData(self.get_counter(), DataType.FORT_GYM, fort, fort.latitude, fort.longitude, dist))
            """

    """ Update pokemon in dict
    """
    def update_pokemons(self, pokemon):
        pass
        

    """ Start updating dictionary with new values or add existing values
    """
    def update_dict(self, map_cells):
        #self.dict = self.default_dict_values()
        for cell in map_cells:
            # update forts
            for fort in cell.forts:
                self.update_forts(fort)

            # update wild pokemons
            for wpokemon in cell.wild_pokemons:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), wpokemon.latitude, wpokemon.longitude)
                self.get_list_from_dict(DataType.WILD_POKEMON).append(
                    DictData(self.get_counter(), DataType.WILD_POKEMON, wpokemon, wpokemon.latitude, wpokemon.longitude, dist))

            # update catchable pokemon
            for cpokemon in cell.catchable_pokemons:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), cpokemon.latitude, cpokemon.longitude)
                self.get_list_from_dict(DataType.CATCHABLE_POKEMON).append(
                    DictData(self.get_counter(), DataType.CATCHABLE_POKEMON, cpokemon, cpokemon.latitude, cpokemon.longitude, dist))

            # update nearby pokemons
            for npokemon in cell.nearby_pokemons:
                npokemon_pos = LatLng.from_point(Cell(CellId(cell.s2_cell_id)).get_center())
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), npokemon_pos.lat().degrees, npokemon_pos.lng().degrees)
                self.get_list_from_dict(DataType.NEARBY_POKEMON).append(
                    DictData(self.get_counter(), DataType.NEARBY_POKEMON, npokemon, npokemon_pos.lat().degrees, npokemon_pos.lng().degrees, dist))

    """ available modes all|pokemon|pokestop
    """
    def items(self, mode):
        result = []
        if mode in ['all', 'pokestop']:
            result += self.get_list_from_dict(DataType.FORT_POKESTOP)

        if mode in ['all', 'pokemon']:
            result += self.get_list_from_dict(DataType.WILD_POKEMON) \
                    + self.get_list_from_dict(DataType.CATCHABLE_POKEMON) \
                    + self.get_list_from_dict(DataType.NEARBY_POKEMON)
        return result
        # return (item for item in result if item.active)

    def sorted_items(self, mode):
        items = self.items(mode)
        items.sort(key=lambda obj: obj.distance)
        return items

