import struct
import time

from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng, Cell

from POGOProtos.Networking import Requests_pb2, Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager


def f2i(float):
    return struct.unpack('<Q', struct.pack('<d', float))[0]


def f2h(float):
    return hex(struct.unpack('<Q', struct.pack('<d', float))[0])


def h2f(hex):
    return struct.unpack('<d', struct.pack('<Q', int(hex,16)))[0]


def encode(cellid):
    output = []
    encoder._VarintEncoder()(output.append, cellid)
    return ''.join(str(o) for o in output)


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


def map_object_request(auth, cellids, loc):
    rh = RequestHandler(auth)
    rh.set_location(loc)

    # create mesasge
    mapObjectMessage = Messages_pb2.GetMapObjectsMessage()
    mapObjectMessage.cell_id.extend(cellids)
    mapObjectMessage.since_timestamp_ms.extend([0] * len(cellids))
    mapObjectMessage.latitude = loc.get_latitude()
    mapObjectMessage.longitude = loc.get_longitude()

    # create server request
    mapObjects = ServerRequest(Requests_pb2.GET_MAP_OBJECTS, mapObjectMessage.SerializeToString())
    rh.add_request(mapObjects)
    rh.send_requests()

    # get response
    mapObjectResponse = mapObjects.get_structured_data()
    print(mapObjectResponse)
    return mapObjectResponse

def get_map_objects(auth, loc):

    parentCls = CellId.from_lat_lng(LatLng.from_degrees(loc.latitude, loc.longitude)).parent(15)
    parentCells = get_cellid(loc.latitude, loc.longitude)
    mapObjectResponse = map_object_request(auth, parentCells, loc)

    originalLoc = LocationManager(loc.latitude, loc.longitude)

    mapResponses = [mapObjectResponse]
    for child in parentCls.children():
        latlng = LatLng.from_point(Cell(child).get_center())
        newLoc = LocationManager(latlng.lat().degrees, latlng.lng().degrees)
        mapResponses.append(map_object_request(auth, get_cellid(newLoc.latitude, newLoc.longitude), newLoc))

    for response in mapResponses:
        print(response)
        """if response.nearby_pokemons:
            print('le pokemon')
        if response.catchable_pokemons:
            print('catchable pokemon')
        if response.wild_pokemons:
            print('wild pokemon')
        if response.forts:
            print('le gyms')
        """
    
    return mapObjectResponse.map_cells