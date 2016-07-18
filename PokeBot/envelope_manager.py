from compiledProto import Envelopes_pb2
from compiledProto.Requests import Request_pb2, RequestType_pb2

from location_manager import LocationManager
import config

#
#
#
class EnvelopeManager():

    def __init__(self, login_manager):
        self.loginManager = login_manager
        self.apiEndpointUrl = config.API_URL

        self.init_api_endpoint_url()

    def init_api_endpoint_url(self):
        req = Envelopes_pb2.Envelopes().RequestEnvelope()

        req1 = req.requests.add()
        req1.request_type = RequestType_pb2.GET_PLAYER
        req2 = req.requests.add()
        req2.request_type = RequestType_pb2.GET_HATCHED_EGGS
        req3 = req.requests.add()
        req3.request_type = RequestType_pb2.GET_INVENTORY
        req4 = req.requests.add()
        req4.request_type = RequestType_pb2.CHECK_AWARDED_BADGES

        req5 = req.requests.add()
        req5.request_type = RequestType_pb2.DOWNLOAD_SETTINGS
        req5.request_message.message = bytes("4a2e9bc330dae60e7b74fc85b98868ab4700802e", "utf-8")

        p_ret = self.request_envelope(req.requests)
        try:
            if hasattr(p_ret, 'api_url'):
                if p_ret.api_url == '':
                    print('Error getting api endpoint url')
                    return

            self.apiEndpointUrl = ('https://%s/rpc' % p_ret.api_url)
            print('api endpoint url: ' + self.apiEndpointUrl)
        except Exception as e:
            print('Exception init_api_endpoint_url()')
            print(e)

    # base request for sending all messager
    # returns response envelope
    def request_envelope(self, req):
        try:
            envelope = Envelopes_pb2.Envelopes()
            req_env = envelope.RequestEnvelope()

            # base codes for all requests
            req_env.status_code = 2
            req_env.request_id = 8145806132888207460

            # add requests
            req_env.requests.MergeFrom(req)

            # location position infos
            lm = LocationManager(46.23083761, 15.26096731, 201)
            req_env.latitude = lm.get_latitude()
            req_env.longitude = lm.get_longitude()
            req_env.altitude = lm.get_altitude()

            req_env.unknown12 = 989
            req_env.auth_info.provider = self.loginManager.get_service()
            req_env.auth_info.token.contents = self.loginManager.get_access_token()
            req_env.auth_info.token.unknown2 = 59

            # start sending
            protobuf = req_env.SerializeToString()
            #print(req_env)
            r = self.loginManager.get_session().post(self.apiEndpointUrl, data=protobuf, verify=False)

            res_env = envelope.ResponseEnvelope()
            res_env.ParseFromString(r.content)
            #print(res_env)

            return res_env

        except Exception as e:
            print('Exception request_envelope()')
            print(e)
            return None


    def send_request(self, requestType):
        try:
            re = Envelopes_pb2.Envelopes().RequestEnvelope()

            req = re.requests.add()
            req.request_type = requestType

            return self.request_envelope(re.requests)

        except Exception as e:
            print('Exception send_request()')
            print(e)
            return None
