from abc import ABC, abstractmethod
import logging

import requests

import PokeApi.exceptions
import POGOProtos.Networking.Envelopes_pb2


"""
"""
class Auth(object):

    """ Base constructor, initializes session
    """
    def __init__(self):
        self.access_token = None
        self.provider = None
        self.session = requests.session()
        self.session.headers.update({'User-Agent': 'Niantic App'})
        self.session.verify = False
    
    """
    """
    def __str__(self):
        return "Provider=%s:Token=%s" % (str(self.provider), str(self.access_token))

    """ @return authInfo object from protos with specified parametrs for login
    """
    def get_auth_info_object(self):
        authInfo = POGOProtos.Networking.Envelopes_pb2.RequestEnvelope().AuthInfo()
        authInfo.provider = self.provider
        authInfo.token.contents = self.access_token
        authInfo.token.unknown2 = 14

        return authInfo


""" Abstract base class for login to server
"""
class Login(ABC):

    """ Base constructor, initializes auth object with session
    """
    def __init__(self):
        self.auth = Auth()
        self.auth.provider = self.get_provider()

    """ @retrun provider string for auth object
    """
    @abstractmethod
    def get_provider(self):
        pass

    """ Login into server with token
    @return auth object
    """
    def login_token(self, token):
        logging.info('Success login with token=%s...' % token)
        self.auth.access_token = token
        return self.auth

    """ Login into server with username and password
    @return auth object
    """
    @abstractmethod
    def login_user(self, username, password):
        pass