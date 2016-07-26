import importlib

from PokeApi import exceptions
from POGOProtos.Networking.Envelopes_pb2 import AuthTicket, ResponseEnvelope, RequestEnvelope, Unknown6
from POGOProtos.Networking import Responses_pb2, Requests_pb2

def to_camel_case(string):
    """ modify string with separator '_' to camel case.
    example: GET_PLAYER -> GetPlayer
    """
    names = string.split('_')
    ret = []
    for name in names:
        ret.append(name.capitalize())
    return "".join(ret)


class ServerRequest(object):
    """ Base abstract request class
    """

    def __init__(self, request_type, request_message=None):
        """ constructor for base request
        """
        # pogledamoo ce obstaja ta vrednost
        if request_type not in Requests_pb2.RequestType.values():
            raise exceptions.ObjectNotInitialized('RequestType specified not found in enum')

        self.request_type = request_type
        self.data = None

        self.request = RequestEnvelope().requests
        self.req = self.request.add()

        self.req.request_type = self.request_type
        self.set_request_message(request_message)
    
    def __str__(self):
        if self.data is None:
            return str('RequestType: ' + Requests_pb2.RequestType.Name(self.request_type))
        else:
            return str(self.get_structured_data())

    def set_request_message(self, request_message):
        """ set request message
        """
        if request_message is not None:
            self.req.request_message = request_message.SerializeToString()

    def handleData(self, data):
        """ handle response data from this request
        """
        self.data = data

    def get_request(self):
        """ return request
        """
        return self.request

    def get_structured_data(self):
        """ @retrun right object with proper return format
        """
        if self.data is None:
            raise exceptions.ObjectNotInitialized('Data not initialized')

        # dobimo class name iz vrednosti iz enum npr. GET_PLAYER -> GetPlayerResponse in lahko to vrnemo
        camelCaseResponseName = "".join([to_camel_case(Requests_pb2.RequestType.Name(self.request_type)), 'Response'])

        class_ = getattr(importlib.import_module("POGOProtos.Networking.Responses_pb2"), camelCaseResponseName)
        dataInstance = class_()
        dataInstance.ParseFromString(self.data)
        return dataInstance
    