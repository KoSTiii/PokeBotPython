import time
import logging

from PokeApi import exceptions, config
from PokeApi.serverrequest import ServerRequest
from PokeApi.auth import Auth
from PokeApi.locations import LocationManager, f2i
from POGOProtos.Networking.Envelopes_pb2 import AuthTicket, ResponseEnvelope, RequestEnvelope, Unknown6

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
        self.request_envelope = RequestEnvelope()
        self.request_envelope.status_code = config.REQUEST_ENVELOPE_STATUS_CODE
        self.request_envelope.request_id = config.REQUEST_ENVELOPE_ID

        if self.last_auth_ticket is not None and self.last_auth_ticket.expire_timestamp_ms > int(round(time.time() * 1000)):
            self.request_envelope.auth_ticket.CopyFrom(self.last_auth_ticket)
        else:
            self.request_envelope.auth_info.CopyFrom(self.auth.get_auth_info_object())
        self.request_envelope.unknown12 = config.REQUEST_ENVELOPE_UNKNOWN12

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
        self.request_envelope.latitude = self.location.get_latitude() #f2i(self.location.get_latitude())
        self.request_envelope.longitude = self.location.get_longitude() #f2i(self.location.get_longitude())
        self.request_envelope.altitude = self.location.get_altitude() #f2i(self.location.get_altitude())

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
            response_envelope = ResponseEnvelope()
            response_envelope.ParseFromString(response.content)
        except Exception as e:
            logging.error('Error parsing response envelope: %s', e)
            raise e

        logging.debug('----- RESPONSE -----\n%s', response_envelope)

        # we get auth ticket
        if response_envelope.HasField('auth_ticket'): #auth_ticket:
            logging.info('changed auth ticket')
            self.last_auth_ticket = AuthTicket()
            self.last_auth_ticket.CopyFrom(response_envelope.auth_ticket)

        """ 
        Handling status codes from server response
        """
        # not complete message
        if response_envelope.status_code is 100:
            logging.error('Response retuned status code 100 (not complete message)')
            raise Exception('Server returned status_code=100 (not complete message)')
        # if error occured when sending
        if response_envelope.status_code is 102:
            logging.error('not logged in or expired token')
            raise exceptions.NotLoggedInException('Not logged in exception')
        # 52 status code means that we hit the data cap. So we wait 2 seconds and try again
        if response_envelope.status_code is 52:
            logging.debug('Hit data cap. waiting 5 secods and try again')
            time.sleep(5)
            return self.send_requests()
        # status_code 53 suposed to be api endpoint change. after 5 retries raise exception (pomeni spremeni server)
        if response_envelope.status_code is 53:
            self.api_endpoint = ('https://%s/rpc' % response_envelope.api_url)
            logging.debug('changed api endpoint to: %s', self.api_endpoint)
            return self.send_requests()
            """
            # we get redirection to other api endpoint server
            if response_envelope.api_url is not None and response_envelope.api_url is not '':
                self.api_endpoint = ('https://%s/rpc' % response_envelope.api_url)
                logging.debug('changed api endpoint to: %s', self.api_endpoint)
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
