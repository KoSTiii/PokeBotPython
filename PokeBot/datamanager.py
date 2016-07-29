import time
from enum import Enum

from s2sphere import LatLng, Cell, CellId

from PokeApi.locations import Coordinates
from PokeBot.actions import Action, FortPokestopAction, CatchPokemonAction, MapPokemonCatchAction, WildPokemonCatchAction
from POGOProtos.Data import Gym_pb2


class DataType(Enum):
    """ Enum of all posible types that we monitoring
    """
    FORT_GYM = 0
    FORT_POKESTOP = 1
    WILD_POKEMON = 2
    CATCHABLE_POKEMON = 3
    NEARBY_POKEMON = 4


class MapCell(object):

    MAP_CELL_CACHE_TIME = 120 # if cell doesnt get updated in this period then delete

    def __init__(self, cell):
        self.s2_cell_id = cell.s2_cell_id
        self.creation_time = time.time()
        self.cell = cell

    def __eq__(self, other):
        return self.s2_cell_id == other.s2_cell_id

    def is_expired(self):
        diff = time.time() - self.creation_time
        if diff > self.MAP_CELL_CACHE_TIME:
            return True
        return False

    def compare_to_proto_map_cell(self, map_cell):
        """
        compare if this MapCell is same as proto map cell
        """
        return self.s2_cell_id == map_cell.s2_cell_id

    def update(self, cell):
        """
        update cell if we have same cell id
        """
        if self.s2_cell_id == cell.s2_cell_id:
            self.cell.CopyFrom(cell)

    def get_map_objects(self, data_type):
        """
        return map objects from this cell if we have something from specifield DataType 
        """
        if data_type in [DataType.FORT_GYM, DataType.FORT_POKESTOP] and self.cell.HasField('forts'):
            fort_type = Gym_pb2.GYM if data_type == DataType.FORT_GYM else Gym_pb2.CHECKPOINT
            return [fort for fort in self.cell.forts if fort.enabled and fort.type == fort_type]
        elif data_type == DataType.WILD_POKEMON and self.cell.HasField('wild_pokemons'):
            return [wpokemon for wpokemon in self.cell.wild_pokemons]
        elif data_type == DataType.CATCHABLE_POKEMON and self.cell.HasField('catchable_pokemons'):
            return [cpokemon for cpokemon in self.cell.catchable_pokemons]
        elif data_type == DataType.NEARBY_POKEMON and self.cell.HasField('nearby_pokemons'):
            return [npokemon for npokemon in self.cell.nearby_pokemons]
        return []


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
        self.action.dict_data = self
        # check if this item is active
    
    def __str__(self):
        return str('DictData: id({}) type({})'.format(self.unique_id, str(self.data_type.name)))

    def __eq__(self, other):
        return self.unique_id == other.unique_id

    def is_active(self):
        return self.action.is_active()

    def try_action(self):
        """
        Try complete action
        """
        return self.action.do_action()


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
            DataType.WILD_POKEMON.name: WildPokemonCatchAction,
            DataType.CATCHABLE_POKEMON.name: MapPokemonCatchAction,
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

    def reset_dict_data(self):
        self.dict = self.default_dict_values()
    
    def update_item_to_dict(self, item_type, item, item_lat, item_lng):
        """
        try update item if already exists, if not then add new
        """
        list_items_dict = self.get_list_from_dict(item_type)
        # try to get all items with same date
        list_items = [itm for itm in list_items_dict if itm.data == item]
        dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), item_lat, item_lng)

        # check if we already have this item in list
        # if we already have item update them (update distance)
        if list_items:
            list_items[0].distance = dist
            list_items[0].data.CopyFrom(item)
        # create new dict_data
        else:
            dict_data = DictData(self.get_counter(),
                                 item_type, 
                                 self.get_action_class(item_type)(self.pokebot, item),
                                 item,
                                 item_lat,
                                 item_lng,
                                 dist)
            self.get_list_from_dict(item_type).append(dict_data)

    def update_forts(self, fort):
        """ update fort with new value. if we find new fort add to list
        """
        # fort type is pokestop
        if fort.type == Gym_pb2.CHECKPOINT:
            self.update_item_to_dict(DataType.FORT_POKESTOP, fort, fort.latitude, fort.longitude)
            #pokestop_list = self.get_list_from_dict(DataType.FORT_POKESTOP)
            # get list item if we already have them saved
            #list_fort = [item for item in pokestop_list if item.data.id == fort.id] # list comprehension

            # check if we already have this fort in list
            # if we already have fort update them (update distance)
            """
            if list_fort:
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
                list_fort[0].distance = dist
                list_fort[0].data.CopyFrom(fort)
                list_fort[0].update_active()
            # if we dont have fort add them
            else:
                "" "
                dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
                dict_data = DictData(self.get_counter(),
                             DataType.FORT_POKESTOP, 
                             self.get_action_class(DataType.FORT_POKESTOP)(self.pokebot, fort),
                             fort,
                             fort.latitude,
                             fort.longitude,
                             dist)
                dict_data.update_active()
                self.get_list_from_dict(DataType.FORT_POKESTOP).append(dict_data)
                """

        # fort type is gym
        elif fort.type == Gym_pb2.GYM:
            """
            gym_list = self.get_list_from_dict(DataType.FORT_GYM)

            dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), fort.latitude, fort.longitude)
            self.get_list_from_dict(DataType.FORT_GYM).append(
                DictData(self.get_counter(), DataType.FORT_GYM, fort, fort.latitude, fort.longitude, dist))
            """

    def update_wild_pokemon(self, pokemon):
        """ Update pokemon in dict
        """

    def update(self, map_cells):
        """ Start updating dictionary with new values or add existing values
        """
        # update all dicts
        for cell in map_cells:

            # check if we farm pokestops
            if self.pokebot.config.mode in ['all', 'pokestop']:
                # update forts
                for fort in cell.forts:
                    self.update_forts(fort)

            # check if we farm pokemons
            if self.pokebot.config.mode in ['all', 'pokemon']:
                # update wild pokemons
                for wpokemon in cell.wild_pokemons:
                    self.update_item_to_dict(DataType.WILD_POKEMON, wpokemon, wpokemon.latitude, wpokemon.longitude)

                # update catchable pokemon
                for cpokemon in cell.catchable_pokemons:
                    self.update_item_to_dict(DataType.CATCHABLE_POKEMON, cpokemon, cpokemon.latitude, cpokemon.longitude)

                # update nearby pokemons
                """
                for npokemon in cell.nearby_pokemons:
                    npokemon_pos = LatLng.from_point(Cell(CellId(cell.s2_cell_id)).get_center())
                    self.update_item_to_dict(DataType.NEARBY_POKEMON, npokemon, npokemon_pos.lat().degrees, npokemon_pos.lng().degrees)
                """

        # print all pokemons close by
        """
        pokes = self.get_pokemons()
        for poke in pokes:
            duplicates = [pokemon for pokemon in pokes if pokemon.distance == poke.distance]
            print('-------------------------------------')
            print(duplicates)
            print('-------------------------------------')
        """

    def execute_actions(self):
        """
        Execute action from dict_data.action
        """
        # execute all actions
        items_to_execute_action = self.sorted_items(self.pokebot.config.mode)
        for item in items_to_execute_action:
            # check if we can execute action
            if item.action.check_action():
                item.try_action()
                # delete item if action is successeded
                list_ = self.get_list_from_dict(item.data_type)
                list_.remove(item)
                


    def get_pokemons(self):
        return self.get_list_from_dict(DataType.WILD_POKEMON) \
             + self.get_list_from_dict(DataType.CATCHABLE_POKEMON) \
             + self.get_list_from_dict(DataType.NEARBY_POKEMON)

    def items(self, mode):
        """ available modes all|pokemon|pokestop
        """
        result = []
        if mode in ['all', 'pokestop']:
            result += self.get_list_from_dict(DataType.FORT_POKESTOP)

        if mode in ['all', 'pokemon']:
            # we can catch only catchable pokemons
            result += self.get_list_from_dict(DataType.WILD_POKEMON) \
                    + self.get_list_from_dict(DataType.CATCHABLE_POKEMON) \
                    + self.get_list_from_dict(DataType.NEARBY_POKEMON)
        # return result
        return [item for item in result if item.is_active()]

    def sorted_items(self, mode):
        items = self.items(mode)
        items.sort(key=lambda obj: obj.distance)
        return items

