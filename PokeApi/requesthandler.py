import time
import logging

from PokeApi import exceptions, apiconfig
from PokeApi.serverrequest import ServerRequest
from PokeApi.auth import Auth
from PokeApi.locations import LocationManager, f2i
from POGOProtos.Networking.Envelopes_pb2 import AuthTicket, ResponseEnvelope, RequestEnvelope, Unknown6

class RequestHandler(object):
    """ Main request handler class for handling all messages to server
    """

    API_URL = 'https://pgorelease.nianticlabs.com/plfe/rpc'

    def __init__(self, auth):
        """ Initialize request handler
        """
        if not isinstance(auth, Auth):
            raise exceptions.InvalidAuthenticationException('Parameter auth is not object from Auth class')
        
        self.logger = logging.getLogger(__name__)
        self.auth = auth
        self.last_auth_ticket = None
        self.api_endpoint = self.API_URL
        self.request_envelope = None
        self.requests = []
        self.hasRequests = False
        self.retry_count = 0
        self.location = None

        self.reset_builder()

    def reset_builder(self):
        """ reset the builder and ready for new set of requests
        """
        self.request_envelope = RequestEnvelope()
        self.request_envelope.status_code = apiconfig.REQUEST_ENVELOPE_STATUS_CODE
        self.request_envelope.request_id = apiconfig.REQUEST_ENVELOPE_ID

        if self.last_auth_ticket is not None and self.last_auth_ticket.expire_timestamp_ms > int(round(time.time() * 1000)):
            self.request_envelope.auth_ticket.CopyFrom(self.last_auth_ticket)
        else:
            self.request_envelope.auth_info.CopyFrom(self.auth.get_auth_info_object())
        self.request_envelope.unknown12 = apiconfig.REQUEST_ENVELOPE_UNKNOWN12

        self.requests = []
        self.hasRequests = False

    def send_requests(self):
        """ send the requests to server
        @return response request
        """
        if not self.hasRequests:
            self.logger.error('trying to send request envelope without requests')
            raise exceptions.IllegalStateException('You are trying to send request envelope without requests')

        # delete all request and add new ones
        del self.request_envelope.requests[:]
        # preprare all requests for right format
        for request in self.requests:
            self.request_envelope.requests.MergeFrom(request.get_request())

        # add location to request envelope
        if not self.location:
            self.logger.error('location is not set')
            raise exceptions.IllegalStateException('You need to set location')
        self.request_envelope.latitude = self.location.get_latitude() #f2i(self.location.get_latitude())
        self.request_envelope.longitude = self.location.get_longitude() #f2i(self.location.get_longitude())
        self.request_envelope.altitude = self.location.get_altitude() #f2i(self.location.get_altitude())

        self.logger.debug('----- REQUEST -----\n%s', self.request_envelope)

        try:
            # start sending
            protobuf = self.request_envelope.SerializeToString()
            response = self.auth.session.post(self.api_endpoint, data=protobuf, verify=False)
        except Exception as e:
            self.logger.error('Error sending request: %s', e)
            raise e
        try:
            # response envelope parsing
            response_envelope = ResponseEnvelope()
            response_envelope.ParseFromString(response.content)
        except Exception as e:
            self.logger.error('Error parsing response envelope: %s', e)
            raise e

        self.logger.debug('----- RESPONSE -----\n%s', response_envelope)

        # we get auth ticket
        if response_envelope.HasField('auth_ticket'): #auth_ticket:
            self.logger.debug('changed auth ticket')
            self.last_auth_ticket = AuthTicket()
            self.last_auth_ticket.CopyFrom(response_envelope.auth_ticket)

        """ 
        Handling status codes from server response
        """
        # not complete message
        if response_envelope.status_code is 100:
            self.logger.error('Response retuned status code 100 (not complete message)')
            raise Exception('Server returned status_code=100 (not complete message)')
        # if error occured when sending
        if response_envelope.status_code is 102:
            self.logger.error('not logged in or expired token')
            raise exceptions.NotLoggedInException('Not logged in exception')
        # 52 status code means that we hit the data cap. So we wait 2 seconds and try again
        if response_envelope.status_code is 52:
            self.logger.debug('Hit data cap. waiting 5 secods and try again')
            time.sleep(5)
            return self.send_requests()
        # status_code 53 suposed to be api endpoint change. after 5 retries raise exception (pomeni spremeni server)
        if response_envelope.status_code is 53:
            self.api_endpoint = ('https://%s/rpc' % response_envelope.api_url)
            self.logger.debug('changed api endpoint to: %s', self.api_endpoint)
            return self.send_requests()
            """
            # we get redirection to other api endpoint server
            if response_envelope.api_url is not None and response_envelope.api_url is not '':
                self.api_endpoint = ('https://%s/rpc' % response_envelope.api_url)
                self.logger.debug('changed api endpoint to: %s', self.api_endpoint)
            """

        # do something with response content
        count = 0
        for data in response_envelope.returns:
            self.requests[count].handleData(data)
            count += 1

        # return array of structured data if have multiple request
        # or return directly structured data if is only one request
        output = []
        if len(self.requests) == 1:
            output = self.requests[0].get_structured_data()
        else:
            for srv_req in self.requests:
                output.append(srv_req.get_structured_data())

        # reset the builder and return output msg
        self.reset_builder()
        return output

    def add_request(self, base_request):
        """ add new request
        @param base_request is class BaseRequest
        """
        if not isinstance(base_request, ServerRequest):
            self.logger.error('request is not instance of ServerRequest')
            raise exceptions.IllegalStateException('Request is not instance of BaseRequest class')

        self.logger.debug('Added request')
        self.requests.append(base_request)
        self.hasRequests = True

    def set_location(self, location):
        """ set the current location
        """
        if not isinstance(location, LocationManager):
            self.logger.error('location is not instance of LocationManager')
            raise exceptions.IllegalStateException('Location is not type of LocationManager')
        self.logger.debug('Location successfuly changed')
        self.location = location
