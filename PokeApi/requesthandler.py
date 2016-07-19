from . import POGOProtos_pb2, exceptions
from .serverrequest import ServerRequest
from .auth.login import Auth


""" Main request handler class for handling all messages to server
"""
class RequestHandler(object):

    API_URL = 'https://pgorelease.nianticlabs.com/plfe/rpc'

    """ Initialize request handler
    """
    def __init__(self, auth):
        if not isinstance(auth, Auth):
            raise exceptions.InvalidAuthenticationException('Parameter auth is not object from Auth class')
        
        self.auth = auth
        self.last_auth_ticket = None
        self.api_endpoint = self.API_URL
        self.request_envelope = None
        self.requests = []
        self.hasRequests = False
        self.retry_count = 0

        self.reset_builder()

    """ reset the builder and ready for new set of requests
    """
    def reset_builder(self):
        self.request_envelope = POGOProtos_pb2.Networking.Envelopes().RequestEnvelope()
        self.request_envelope.status_code = 2
        self.request_envelope.request_id = 8145806132888207460

        self.request_envelope.unknown12 = 989
        self.request_envelope.auth_info.CopyFrom(self.auth.get_auth_info_object())

        if self.last_auth_ticket and self.last_auth_ticket.expire_timestamp_ms > 0:
            self.request_envelope.auth_ticket.CopyFrom(self.last_auth_ticket)

        self.requests = []
        self.hasRequests = False

    """ send the requests to server
    @return response request
    """
    def send_requests(self):
        if not self.hasRequests:
            raise exceptions.IllegalStateException('You are trying to send request envelope without requests')

        # delete all request and add new ones
        del self.request_envelope.requests[:]
        # preprare all requests for right format
        for request in self.requests:
            self.request_envelope.requests.MergeFrom(request.get_request())

        print('----------------------REQUEST------------------------')
        print(self.request_envelope)
        
        # start sending
        protobuf = self.request_envelope.SerializeToString()
        response = self.auth.session.post(self.api_endpoint, data=protobuf, verify=False)
        # response envelope parsing
        response_envelope = POGOProtos_pb2.Networking.Envelopes().ResponseEnvelope()
        response_envelope.ParseFromString(response.content)
        
        print('----------------------RESPONSE------------------------')
        print(response_envelope)

        # if error occured when sending
        if response_envelope.status_code is 102:
            raise exceptions.LoginFailedException('Login failed when sending request')

        # we get redirection to other api endpoint server
        if response_envelope.api_url is not None and response_envelope.api_url is not '':
            self.api_endpoint = ('https://%s/rpc' % response_envelope.api_url)

        # we get auth ticket
        if response_envelope.auth_ticket:
            self.last_auth_ticket = response_envelope.auth_ticket

        # do something with response content
        count = 0
        for data in response_envelope.returns:
            self.requests[count].handleData(data)
            count += 1

        # status_code 53 suposed to be retry. after 5 retries raise exception
        if response_envelope.status_code is 53:
            if self.retry_count > 5:
                raise exceptions.IllegalStateException('Retry count is more than 5 tries. quiting..')
            
            self.retry_count += 1
            self.send_requests()

        self.reset_builder()

    """ add new request
    @param base_request is class BaseRequest
    """
    def add_request(self, base_request):
        if not isinstance(base_request, ServerRequest):
            raise exceptions.IllegalStateException('Request is not instance of BaseRequest class')

        self.requests.append(base_request)
        self.hasRequests = True

    """ set the current location
    """
    def set_location(self, latitude, longitude, altitude):
        self.request_envelope.latitude = latitude
        self.request_envelope.longitude = longitude
        self.request_envelope.altitude = altitude
