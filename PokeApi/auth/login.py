from abc import ABC, abstractmethod
import logging

import requests

from PokeApi import exceptions, apiconfig
import POGOProtos.Networking.Envelopes_pb2


class Auth(object):
    """
    """

    def __init__(self):
        """ Base constructor, initializes session
        """
        self.access_token = None
        self.provider = None
        self.username = None
        self.password = None
        self.session = requests.session()
        self.session.headers.update({'User-Agent': 'Niantic App'})
        self.session.verify = False
    
    def __str__(self):
        """
        """
        return "Provider=%s:Token=%s" % (str(self.provider), str(self.access_token))

    def get_auth_info_object(self):
        """ @return authInfo object from protos with specified parametrs for login
        """
        authInfo = POGOProtos.Networking.Envelopes_pb2.RequestEnvelope().AuthInfo()
        authInfo.provider = self.provider
        authInfo.token.contents = self.access_token
        authInfo.token.unknown2 = apiconfig.AUTHINFO_TOKEN_UNKNOWN2

        return authInfo

    def authorize(self):
        """
        try to authorize new or existing connection
        """
        from PokeApi.auth import GoogleLogin, PTCLogin
        
        if self.provider == "ptc":
            auth = PTCLogin().login_user(self.username, self.password)
        else:
            auth = GoogleLogin().login_user(self.username, self.password)
        self.access_token = auth.access_token



class Login(ABC):
    """ Abstract base class for login to server
    """

    def __init__(self):
        """ Base constructor, initializes auth object with session
        """
        self.logger = logging.getLogger(__name__)
        self.auth = Auth()
        self.auth.provider = self.get_provider()

    @abstractmethod
    def get_provider(self):
        """ @retrun provider string for auth object
        """
        pass

    def set_auth_credentials(self, username, password):
        self.auth.username = username
        self.auth.password = password

    def login_token(self, token):
        """ Login into server with token
        @return auth object
        """
        self.logger.info('Success login with token=%s...', token)
        self.auth.access_token = token
        return self.auth

    @abstractmethod
    def login_user(self, username, password):
        """ Login into server with username and password
        @return auth object
        """
        self.set_auth_credentials(username, password)