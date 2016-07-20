import logging

from PokeApi.auth import PTCLogin, Auth
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager
import POGOProtos
from POGOProtos.Networking import Requests_pb2, Responses_pb2


logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.DEBUG)

auth = PTCLogin().login_user('bumbar2', 'bumbar2')
#auth = PTCLogin().login_token('TGT-258517-Oflc3jkqpYgE7Xd26sxxpjOM4LXQTGiCnszYevKNQgzmdcOcgf-sso.pokemon.com')
logging.info(auth)

rh = RequestHandler(auth)
loc = LocationManager(46.23083761, 15.26096731, 201)
rh.set_location(loc)

player = ServerRequest(Requests_pb2.GET_INVENTORY)
rh.add_request(player)
rh.send_requests()

dataInstance = player.get_structured_data()
logging.info(dataInstance)
