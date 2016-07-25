import logging

import json
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from gpsoauth import perform_master_login, perform_oauth

from PokeApi.auth.login import Login, Auth
from PokeApi import exceptions, apiconfig

# disable insecure warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


""" Google Login class for login to pokemon server with google account
"""
class GoogleLogin(Login):

    """ Constuctor. initializes base class
    """
    def __init__(self):
        Login.__init__(self)

    """ @retrun provider string for auth object
    """
    def get_provider(self):
        return 'google'

    """ Login into server with username and password
    @return auth object
    """
    def login_user(self, username, password):
        self.logger.info('Started logging into google services with username=%s' % username)

        login = perform_master_login(username, password, apiconfig.GOOGLE_LOGIN_ANDROID_ID)
        login = perform_oauth(username, login.get('Token', ''), apiconfig.GOOGLE_LOGIN_ANDROID_ID, apiconfig.GOOGLE_LOGIN_SERVICE, apiconfig.GOOGLE_LOGIN_APP, apiconfig.GOOGLE_LOGIN_CLIENT_SIG)
            
        auth_token = login.get('Auth')
        
        if auth_token is None:
            self.logger.error('Login failed with google login')
            raise exceptions.LoginFailedException('Cant login to google services')

        self.auth.access_token = auth_token
        self.logger.info('Login successed to google with username=' + username)
        return self.auth