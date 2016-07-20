import logging

import json
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from gpsoauth import perform_master_login, perform_oauth

from PokeApi.auth.login import Login, Auth
from PokeApi import exceptions

# disable insecure warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


""" Google Login class for login to pokemon server with google account
"""
class GoogleLogin(Login):

    GOOGLE_LOGIN_ANDROID_ID = '9774d56d682e549c'
    GOOGLE_LOGIN_SERVICE= 'audience:server:client_id:848232511240-7so421jotr2609rmqakceuu1luuq0ptb.apps.googleusercontent.com'
    GOOGLE_LOGIN_APP = 'com.nianticlabs.pokemongo'
    GOOGLE_LOGIN_CLIENT_SIG = '321187995bc7cdc2b5fc91b11a96e2baa8602c62'

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
        logging.info('Started logging into google services with username=%s' % username)

        login = perform_master_login(username, password, self.GOOGLE_LOGIN_ANDROID_ID)
        login = perform_oauth(username, login.get('Token', ''), self.GOOGLE_LOGIN_ANDROID_ID, self.GOOGLE_LOGIN_SERVICE, self.GOOGLE_LOGIN_APP, self.GOOGLE_LOGIN_CLIENT_SIG)
            
        auth_token = login.get('Auth')
        
        if auth_token is None:
            logging.error('Login failed with google login')
            raise exceptions.LoginFailedException('Cant login to google services')

        self.auth.access_token = auth_token
        logging.info('Login successed to google with username=' + username)
        return self.auth