import logging
import time

from PokeApi.auth import PTCLogin, Auth
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager
from PokeApi.pokeapi import PokeApi
from POGOProtos.Networking import Requests_pb2, Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2

import s2sphere


logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.DEBUG)

#auth = PTCLogin().login_user('bumbar2', 'bumbar2')
auth = PTCLogin().login_token('TGT-663178-avlUsomETSRcfexCsnJRPNsA6BPymzpiRBciDFzscthhlSJfeY-sso.pokemon.com')
logging.info(auth)

"""
rh = RequestHandler(auth)
loc = LocationManager(46.23083761, 15.26096731, 201)
rh.set_location(loc)

player = ServerRequest(Requests_pb2.GET_INVENTORY)
rh.add_request(player)
rh.send_requests()

dataInstance = player.get_structured_data()
logging.info(dataInstance)
"""

pokeapi = PokeApi(auth)
print(pokeapi.get_profile())

# get map object
"""
origin = s2sphere.CellId.from_lat_lng(s2sphere.LatLng.from_degrees(loc.latitude, loc.longitude)).parent(15)
walk = [origin.id()]
next = origin.next()
prev = origin.prev()
for i in range(10):
    walk.append(prev.id())
    walk.append(next.id())
    next = next.next()
    prev = prev.prev()

mapObjectMessage = Messages_pb2.GetMapObjectsMessage()
mapObjectMessage.cell_id.extend(walk)
mapObjectMessage.since_timestamp_ms.extend([int(time.time())] * 21)
mapObjectMessage.latitude = loc.get_latitude()
mapObjectMessage.longitude = loc.get_longitude()

mapObjects = ServerRequest(Requests_pb2.GET_MAP_OBJECTS, mapObjectMessage.SerializeToString())
rh.add_request(mapObjects)
rh.send_requests()

print(mapObjects.get_structured_data())
"""