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
auth = PTCLogin().login_token('TGT-329495-AhVBlxhY3SgqMrA05JMRdk0jx1xIhGxZVvupXaLdXQMdkTv1hI-sso.pokemon.com')
logging.info(auth)

#loc = LocationManager(46.2397495, 15.2677063, 0) # celje
#loc = LocationManager(46.23083761, 15.26096731, 0) # celje
loc = LocationManager(46.229257, 15.302431, 0) # teharje krozisce

pokeapi = PokeApi(auth, loc)
print(pokeapi.get_profile())

pokeapi.get_map_objects()