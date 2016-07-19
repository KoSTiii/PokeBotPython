from . import POGOProtos_pb2

""" Base abstract request class
"""
class ServerRequest(object):

    """ constructor for base request
    """
    def __init__(self, request_type, request_message=None):
        self.requst_type = request_type
        self.data = None

        self.request = POGOProtos_pb2.Networking.Envelopes().RequestEnvelope().requests
        req = self.request.add()
        req.request_type = self.requst_type
        if request_message is not None:
            req.request_message = bytes(request_message, 'utf-8')

    """ handle response data from this request
    """
    def handleData(self, data):
        self.data = data

    """ return request
    """
    def get_request(self):
        return self.request

    