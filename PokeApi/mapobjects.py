import struct
import time

from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng, Cell

from POGOProtos.Networking import Requests_pb2, Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager, f2i


def get_cellid(lat, long):
    origin = CellId.from_lat_lng(LatLng.from_degrees(lat, long)).parent(15)
    walk = [origin.id()]

    # 10 before and 10 after
    next = origin.next()
    prev = origin.prev()
    for i in range(10):
        walk.append(prev.id())
        walk.append(next.id())
        next = next.next()
        prev = prev.prev()
    return sorted(walk)


""" dobi krog okoli centra tocke
"""
def get_neighbours(lat, long):
    ns = 0.0025
    ew = 0.0025
    walk = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            thiscell = CellId.from_lat_lng(LatLng.from_degrees(lat + ns*i, long + ew*j)).parent(15)
            if abs(i * j) < 4:
                walk.append(thiscell.id())
    return sorted(walk)


""" Map object request to the server
@return object of GetMapObjectResponse
"""
def map_object_request(req_hand, cellids, loc):
    #req_hand.set_location(loc)

    # create mesasge
    mapObjectMessage = Messages_pb2.GetMapObjectsMessage()
    mapObjectMessage.cell_id.extend(cellids)
    mapObjectMessage.since_timestamp_ms.extend([0] * len(cellids))
    mapObjectMessage.latitude = f2i(loc.get_latitude())
    mapObjectMessage.longitude = f2i(loc.get_longitude())

    # create server request
    mapObjects = ServerRequest(Requests_pb2.GET_MAP_OBJECTS, mapObjectMessage)
    req_hand.add_request(mapObjects)
    req_hand.send_requests()

    # get response
    mapObjectResponse = mapObjects.get_structured_data()
    return mapObjectResponse


""" get all objects from server
"""
def get_map_objects(req_hand, loc):
    # get cells id
    parentCells = get_cellid(loc.latitude, loc.longitude)
    mapObjectResponse = map_object_request(req_hand, parentCells, loc)

    for map_cell in mapObjectResponse.map_cells:
        print(map_cell)
        if map_cell.nearby_pokemons:
            print('le pokemon')
        if map_cell.catchable_pokemons:
            print('catchable pokemon')
        if map_cell.wild_pokemons:
            print('wild pokemon')
        if map_cell.forts:
            print('le gyms')
    
    return mapObjectResponse.map_cells