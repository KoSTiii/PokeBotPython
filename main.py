
import PokeApi

#auth = PokeApi.auth.PTCLogin().login_user('bumbar1', 'bumbar1')
auth = PokeApi.auth.PTCLogin().login_token('TGT-698435-Qd0H7Ak1vznrdStsgwsSFQc6ny6dkH9CkeH7fDsQXB7QGhK5zy-sso.pokemon.com')
print(auth)

print(auth.get_auth_info_object())

rh = PokeApi.requesthandler.RequestHandler(auth)

player = PokeApi.serverrequest.ServerRequest(PokeApi.POGOProtos_pb2.Networking.Requests.GET_PLAYER)
rh.add_request(player)
rh.send_requests()

#help(PokeApi.POGOProtos_pb2.Networking.Responses.GetPlayerResponse)

print(player.data)
test = player.data.decode('utf-8', 'ignore')
#playerData = PokeApi.POGOProtos_pb2.Networking.Responses.GetPlayerResponse().MergeFromString(player.data)
#playerData.SerializeToString()
print(test)
