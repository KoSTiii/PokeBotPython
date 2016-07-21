import logging
import time

import s2sphere

from PokeApi.auth import PTCLogin, Auth
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager
from PokeApi.pokeapi import PokeApi
from PokeApi import mapobjects
from POGOProtos.Networking import Requests_pb2, Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2



logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.DEBUG)

#auth = PTCLogin().login_user('bumbar1', 'bumbar1')
auth = PTCLogin().login_token('TGT-1220083-HV4tlpchp4msdmxTx4XgqaddEheVladyfgN4vCnKr7Y7dazins-sso.pokemon.com')
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
#print(pokeapi.get_profile())
print(pokeapi.get_settings())

#loc = LocationManager(46.23083761, 15.26096731, 0)
loc = LocationManager(46.229257, 15.302431, 0) # teharje krozisce

# get map object
#while True:
map_cells = mapobjects.get_map_objects(auth, loc)
time.sleep(2)