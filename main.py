import logging

import PokeApi


logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.DEBUG)

#auth = PokeApi.auth.PTCLogin().login_user('bumbar1', 'bumbar1')
auth = PokeApi.auth.PTCLogin().login_token('TGT-258517-Oflc3jkqpYgE7Xd26sxxpjOM4LXQTGiCnszYevKNQgzmdcOcgf-sso.pokemon.com')
logging.info(auth)

rh = PokeApi.RequestHandler(auth)
loc = PokeApi.LocationManager(46.23083761, 15.26096731, 201)
rh.set_location(loc)

player = PokeApi.ServerRequest(PokeApi.POGOProtos_pb2.Networking.Requests.GET_PLAYER)
rh.add_request(player)
rh.send_requests()

playerData = PokeApi.POGOProtos_pb2.Networking.Responses.GetPlayerResponse()
playerData.ParseFromString(player.data)
logging.info(playerData)
