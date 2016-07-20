import logging

from . import exceptions
from .serverrequest import ServerRequest
from .auth.login import Auth
from .locations import LocationManager
from .POGOProtos.Networking.Envelopes_pb2 import * 

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
        self.location = None

        self.reset_builder()

    """ reset the builder and ready for new set of requests
    """
    def reset_builder(self):
        self.request_envelope = POGOProtos.Networking.Envelopes_pb2.Envelopes().RequestEnvelope()
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
            logging.error('trying to send request envelope without requests')
            raise exceptions.IllegalStateException('You are trying to send request envelope without requests')

        # delete all request and add new ones
        del self.request_envelope.requests[:]
        # preprare all requests for right format
        for request in self.requests:
            self.request_envelope.requests.MergeFrom(request.get_request())

        # add location to request envelope
        if not self.location:
            logging.error('location is not set')
            raise exceptions.IllegalStateException('You need to set location')
        self.request_envelope.latitude = self.location.get_latitude()
        self.request_envelope.longitude = self.location.get_longitude()
        self.request_envelope.altitude = self.location.get_altitude()

        logging.debug('----- REQUEST -----\n%s', self.request_envelope)
        
        try:
            # start sending
            protobuf = self.request_envelope.SerializeToString()
            response = self.auth.session.post(self.api_endpoint, data=protobuf, verify=False)
        except Exception as e:
            logging.error('Error sending request: %s', e)
            raise e
        try:
            # response envelope parsing
            response_envelope = POGOProtos_pb2.Networking.Envelopes().ResponseEnvelope()
            response_envelope.ParseFromString(response.content)
        except Exception as e:
            logging.error('Error parsing response envelope: %s', e)
            raise e

        logging.debug('----- RESPONSE -----\n%s', response_envelope)

        # if error occured when sending
        if response_envelope.status_code is 102:
            logging.error('login expired or failed login')
            raise exceptions.LoginFailedException('Login failed when sending request')

        # we get redirection to other api endpoint server
        if response_envelope.api_url is not None and response_envelope.api_url is not '':
            self.api_endpoint = ('https://%s/rpc' % response_envelope.api_url)
            logging.debug('changed api endpoint to: %s', self.api_endpoint)

        # we get auth ticket
        if response_envelope.auth_ticket:
            self.last_auth_ticket = response_envelope.auth_ticket

        # do something with response content
        count = 0
        for data in response_envelope.returns:
            self.requests[count].handleData(data)
            count += 1

        # status_code 53 suposed to be retry. after 5 retries raise exception
        if response_envelope.status_code is 53 or response_envelope.status_code is 52:
            if self.retry_count > 5:
                raise exceptions.IllegalStateException('Retry count is more than 5 tries. quiting..')
            
            logging.debug('Retrying sending request envelope to server. status_code=53')
            self.retry_count += 1
            self.send_requests()

        self.reset_builder()

    """ add new request
    @param base_request is class BaseRequest
    """
    def add_request(self, base_request):
        if not isinstance(base_request, ServerRequest):
            logging.error('request is not instance of ServerRequest')
            raise exceptions.IllegalStateException('Request is not instance of BaseRequest class')

        logging.debug('Added request')
        self.requests.append(base_request)
        self.hasRequests = True

    """ set the current location
    """
    def set_location(self, location):
        if not isinstance(location, LocationManager):
            logging.error('location is not instance of LocationManager')
            raise exceptions.IllegalStateException('Location is not type of LocationManager')
        logging.debug('Location successfuly changed')
        self.location = location
