from POGOProtos.Networking.Envelopes_pb2 import AuthTicket, ResponseEnvelope, RequestEnvelope, Unknown6

""" Base abstract request class
"""
class ServerRequest(object):

    """ constructor for base request
    """
    def __init__(self, request_type, request_message=None):
        self.requst_type = request_type
        self.data = None

        self.request = RequestEnvelope().requests
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

    