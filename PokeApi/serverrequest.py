import importlib

from PokeApi import exceptions
from POGOProtos.Networking.Envelopes_pb2 import AuthTicket, ResponseEnvelope, RequestEnvelope, Unknown6
from POGOProtos.Networking import Responses_pb2, Requests_pb2

""" modify string with separator '_' to camel case.
example: GET_PLAYER -> GetPlayer
"""
def to_camel_case(string):
    names = string.split('_')
    ret = []
    for name in names:
        ret.append(name.capitalize())
    return "".join(ret)


""" Base abstract request class
"""
class ServerRequest(object):

    """ constructor for base request
    """
    def __init__(self, request_type, request_message=None):
        # pogledamoo ce obstaja ta vrednost
        if request_type not in Requests_pb2.RequestType.values():
            raise exceptions.ObjectNotInitialized('RequestType specified not found in enum')

        self.requst_type = request_type
        self.data = None

        self.request = RequestEnvelope().requests
        req = self.request.add()
        req.request_type = self.requst_type
        if request_message is not None:
            req.request_message = request_message.SerializeToString()
    
    def __str__(self):
        if self.data is None:
            return str('RequestType: ' + Requests_pb2.RequestType.Name(self.requst_type))
        else:
            return str(self.get_structured_data())

    """ handle response data from this request
    """
    def handleData(self, data):
        self.data = data

    """ return request
    """
    def get_request(self):
        return self.request

    """ @retrun right object with proper return format
    """
    def get_structured_data(self):
        if self.data is None:
            raise exceptions.ObjectNotInitialized('Data not initialized')

        # dobimo class name iz vrednosti iz enum npr. GET_PLAYER -> GetPlayerResponse in lahko to vrnemo
        camelCaseResponseName = "".join([to_camel_case(Requests_pb2.RequestType.Name(self.requst_type)), 'Response'])

        class_ = getattr(importlib.import_module("POGOProtos.Networking.Responses_pb2"), camelCaseResponseName)
        dataInstance = class_()
        dataInstance.ParseFromString(self.data)
        return dataInstance
    