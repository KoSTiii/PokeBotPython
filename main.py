import logging
import time
import datetime

import s2sphere

from PokeApi.auth import PTCLogin, Auth
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager
from PokeApi.pokeapi import PokeApi
from PokeApi import mapobjects
from POGOProtos.Networking import Requests_pb2, Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2
from POGOProtos.Data import Gym_pb2


logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.DEBUG)

#auth = PTCLogin().login_user('bumbar1', 'bumbar1')
auth = PTCLogin().login_token('TGT-295844-VnXnz90rXkGogbDDAgT3WLMbob9rckMShmlOZH4udQWkdEyzwA-sso.pokemon.com')
logging.info(auth)

#loc = LocationManager(46.2397495, 15.2677063, 0) # celje
#loc = LocationManager(46.23083761, 15.26096731, 0) # celje
loc = LocationManager(46.229257, 15.302431, 0) # teharje krozisce

pokeapi = PokeApi(auth, loc)
pokeapi.get_profile()

while True:
    map_cells = pokeapi.get_map_objects()

    for map_cell in map_cells:
        for fort in map_cell.forts:

            if fort.type is Gym_pb2.CHECKPOINT:
                # pogledamo ce je fort na cooldownu
                print(datetime.datetime.fromtimestamp(fort.cooldown_complete_timestamp_ms / 1000).strftime('%Y-%m-%d %H:%M:%S.%f'))
                currentTimeMs = int(round(time.time() * 1000))
                if fort.cooldown_complete_timestamp_ms and fort.cooldown_complete_timestamp_ms < currentTimeMs:
                    # spinamo fort ce ga lahko
                    fortSearch = Messages_pb2.FortSearchMessage()
                    fortSearch.fort_id = fort.id
                    fortSearch.player_latitude = loc.get_latitude()
                    fortSearch.player_longitude = loc.get_longitude()
                    fortSearch.fort_latitude = fort.latitude
                    fortSearch.fort_longitude = fort.longitude
                    fortReq = ServerRequest(Requests_pb2.FORT_SEARCH, fortSearch)
                    pokeapi.request_handler.add_request(fortReq)
                    res = pokeapi.request_handler.send_requests()
                    print(res)
                    pprint('FORT CHECKPOINT spined')
    
    # sleep for 
    time.sleep(155)
