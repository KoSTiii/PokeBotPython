import logging
import time
import datetime

import s2sphere
import coloredlogs

from PokeApi.auth import PTCLogin, Auth
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager
from PokeApi.pokeapi import PokeApi
from PokeApi import mapobjects
from POGOProtos.Networking import Requests_pb2, Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2
from POGOProtos.Data import Gym_pb2
from PokeBot.pokebot import PokeBot
from PokeBot.botconfig import BotConfig

# setup loggers
#logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.DEBUG)
coloredlogs.install()
logging.getLogger('requests').setLevel(logging.DEBUG)
logging.getLogger('PokeApi').setLevel(logging.DEBUG)
logging.getLogger('PokeApi.auth').setLevel(logging.DEBUG)
logging.getLogger('PokeApi.RequestHandler').setLevel(logging.DEBUG)
logging.getLogger('PokeBot').setLevel(logging.DEBUG)


#auth = PTCLogin().login_user('bumbar1', 'bumbar1')
#auth = PTCLogin().login_token('TGT-4914745-wRCUwvWEU3vv7N1x1HFMNBBeUnvPlxiJjXBbrQwdGdQhc0SUS2-sso.pokemon.com')
#logging.info(auth)

"""
#loc = LocationManager(46.2397495, 15.2677063, 0) # celje
#loc = LocationManager(46.23083761, 15.26096731, 0) # celje
loc = LocationManager(46.229257, 15.302431, 0) # teharje krozisce

pokeapi = PokeApi(auth, loc)
pokeapi.get_profile()

pokeapi.download_settings(hash='05daf51635c82611d1aac95c0b051d3ec088a930')
pokeapi.send_requests()


#map_cells = pokeapi.get_map_objects(cell_id=[0]*21, since_timestamp_ms=[0]*21, latitude=loc.get_latitude(), longitude=loc.get_longitude())
#map_cells = pokeapi.send_requests().map_cells
map_cells = pokeapi.get_all_map_objects().map_cells

for map_cell in map_cells:
    for fort in map_cell.forts:

        if fort.type is Gym_pb2.CHECKPOINT:
            # pogledamo ce je fort na cooldownu
            print(datetime.datetime.fromtimestamp(fort.cooldown_complete_timestamp_ms / 1000).strftime('%Y-%m-%d %H:%M:%S.%f'))
            currentTimeMs = int(round(time.time() * 1000))
            if fort.cooldown_complete_timestamp_ms and fort.cooldown_complete_timestamp_ms < currentTimeMs:
                # spinamo fort ce ga lahko
                pokeapi.fort_search(fort_id=fort.id, 
                                    player_latitude=loc.get_latitude(), 
                                    player_longitude=loc.get_longitude(), 
                                    fort_latitude=fort.latitude, 
                                    fort_longitude=fort.longitude)
                res = pokeapi.send_requests()
                #print(res)
                print('FORT CHECKPOINT spined')
"""

# make config
configs = BotConfig.from_file('config.json')
# BOT TEST
bot = PokeBot(configs[0])