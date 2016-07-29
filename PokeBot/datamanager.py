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

    def __init__(self, pb2_cell):
        self.s2_cell_id = pb2_cell.s2_cell_id
        self.creation_time = time.time()
        self.cell = pb2_cell

    def __eq__(self, other):
        return self.s2_cell_id == other.s2_cell_id

    def is_expired(self):
        diff = time.time() - self.creation_time
        if diff > self.MAP_CELL_CACHE_TIME:
            return True
        return False

    def compare_to_proto_map_cell(self, pb2_map_cell):
        """
        compare if this MapCell is same as proto map cell
        """
        return self.s2_cell_id == pb2_map_cell.s2_cell_id

    def update(self, pb2_cell):
        """
        update cell if we have same cell id
        """
        if self.compare_to_proto_map_cell(pb2_cell):
            self.cell.CopyFrom(pb2_cell)

    def get_map_cell_objects(self, data_type):
        """
        return map objects from this cell if we have something from specifield DataType 
        """
        if data_type in [DataType.FORT_GYM, DataType.FORT_POKESTOP] and self.cell.forts:
            fort_type = Gym_pb2.GYM if data_type == DataType.FORT_GYM else Gym_pb2.CHECKPOINT
            return [fort for fort in self.cell.forts if fort is not None and fort.enabled and fort.type == fort_type]
        elif data_type == DataType.WILD_POKEMON and self.cell.wild_pokemons:
            return [wpokemon for wpokemon in self.cell.wild_pokemons if wpokemon is not None]
        elif data_type == DataType.CATCHABLE_POKEMON and self.cell.catchable_pokemons:
            return [cpokemon for cpokemon in self.cell.catchable_pokemons if cpokemon is not None]
        elif data_type == DataType.NEARBY_POKEMON and self.cell.nearby_pokemons:
            return [npokemon for npokemon in self.cell.nearby_pokemons if npokemon is not None]
        else:
            return []


class MapCellData(object):
    """ Data stored in dictionary for pokemon/forts
    """

    def __init__(self, data_type, action, data, lat, lon, distance):
        self.data_type = data_type
        self.action = action
        self.data = data
        self.location = (lat, lon)
        self.distance = distance
        self.action.map_cell_data = self
    
    def __str__(self):
        return 'DictData: type({})'.format(self.data_type.name)

    def __eq__(self, other):
        return self.data == other.data

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
        self.action_classes = self.default_action_classes()

        self.map_cells = []

    def default_action_classes(self):
        return {
            DataType.FORT_GYM.name: Action,
            DataType.FORT_POKESTOP.name: FortPokestopAction,
            DataType.WILD_POKEMON.name: WildPokemonCatchAction,
            DataType.CATCHABLE_POKEMON.name: MapPokemonCatchAction,
            DataType.NEARBY_POKEMON.name: Action
        }

    def get_map_cells_objects(self, data_type):
        output = []
        for mapcell in self.map_cells:
            output += mapcell.get_map_cell_objects(data_type)
        return output
        # return [mapcell.get_map_cell_objects(data_type) for mapcell in self.map_cells]

    def get_map_cells_objects_data(self, data_type):
        map_cells = self.get_map_cells_objects(data_type)
        output = []
        for cell in map_cells:
            # check if cell have latitude and longitude. if it doesnt then calculate from cell id
            if cell.latitude and cell.longitude:
                loc = (cell.latitude, cell.longitude)
            else:
                latlng = LatLng.from_point(Cell(cell.s2_cell_id).get_center())
                loc = (latlng.lat().degrees, latlng.lng().degrees)
            dist = Coordinates.distance_haversine_km(*self.loc.get_lat_lng(), *loc)
            output.append(
                MapCellData(
                    data_type,
                    self.get_action_class(data_type)(self.pokebot, cell),
                    cell,
                    loc[0],
                    loc[1],
                    dist))
        return output

    def get_action_class(self, data_type):
        return self.action_classes[data_type.name]

    def reset_map_cells(self):
        self.map_cells = []

    def update(self, map_cells):
        """ Start updating dictionary with new values or add existing values
        """
        # update all dicts
        for cell in map_cells:
            # update map cells
            local_map_cells = [mcell for mcell in self.map_cells if mcell.s2_cell_id == cell.s2_cell_id]
            # if we already have cell then only update it
            if local_map_cells:
                for c in local_map_cells:
                    c.update(cell)
            # if we dont have map cell then make one
            else:
                self.map_cells.append(MapCell(cell))
        
        # delete all expired map cells
        for map_cell in self.map_cells:
            if map_cell.is_expired:
                del map_cell

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
                del item.data

    def items(self, mode):
        """ available modes all|pokemon|pokestop
        """
        result = []
        if mode in ['all', 'pokestop']:
            result += self.get_map_cells_objects_data(DataType.FORT_POKESTOP)

        if mode in ['all', 'pokemon']:
            # we can catch only catchable pokemons
            result += self.get_map_cells_objects_data(DataType.CATCHABLE_POKEMON)
        # return result
        return [item for item in result if item.is_active()]

    def sorted_items(self, mode):
        items = self.items(mode)
        items.sort(key=lambda obj: obj.distance)
        return items

