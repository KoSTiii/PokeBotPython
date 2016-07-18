import sys
sys.path.append("../compiledProto")

from login_manager import LoginManager
from envelope_manager import EnvelopeManager
import config
import log_manager as log

from compiledProto.Requests import Request_pb2, RequestType_pb2

print('Program starting...')

lm = LoginManager(config.POKEGO_LOGINTYPE, config.POKEGO_USERNAME, config.POKEGO_PASSWORD)
if lm.login():
    print('Success login')
else:
    print('Error loggin')

print('Token: ' + lm.get_access_token())

em = EnvelopeManager(lm)

player = em.send_request(RequestType_pb2.GET_PLAYER)
print("PLAYER INFO")
print(player)

#inv = em.send_request(RequestType_pb2.GET_INVENTORY)
#log.print_info(inv)

#mapObj = em.send_request(RequestType_pb2.GET_MAP_OBJECTS)
#log.print_info(mapObj)
