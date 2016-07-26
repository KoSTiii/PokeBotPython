"""
"""

import logging

import json
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from PokeApi.auth.login import Login, Auth
from PokeApi import exceptions, apiconfig

# disable insecure warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class PTCLogin(Login):
    """ PTCLogin class for login to pokemon server
    """

    def __init__(self):
        """ Constuctor. initializes base class
        """
        Login.__init__(self)

    def get_provider(self):
        """ @retrun provider string for auth object
        """
        return 'ptc'

    def login_user(self, username, password):
        """ Login into server with username and password
        @return auth object
        """
        self.logger.info('Started logging into ptc services with username=%s', username)

        head = {'User-Agent': 'niantic'}
        r = self.auth.session.get(apiconfig.LOGIN_URL, headers=head)
        if r.status_code is not requests.codes.ok:
            raise exceptions.LoginFailedException('Login Server seems to be offline')

        jdata = json.loads(r.content.decode('utf-8'))
        data = {
            'lt': jdata['lt'],
            'execution': jdata['execution'],
            '_eventId': 'submit',
            'username': username,
            'password': password,
        }
        r1 = self.auth.session.post(apiconfig.LOGIN_URL, data=data, headers=head)

        ticket = None
        try:
            ticket = re.sub('.*ticket=', '', r1.history[0].headers['Location'])
        except Exception as e:
            raise exceptions.LoginFailedException('Error when getting results from login server')

        data1 = {
            'client_id': 'mobile-app_pokemon-go',
            'redirect_uri': 'https://www.nianticlabs.com/pokemongo/error',
            'client_secret': apiconfig.PTC_CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'code': ticket,
        }
        r2 = self.auth.session.post(apiconfig.LOGIN_OAUTH, data=data1)
        access_token = re.sub('&expires.*', '', r2.content.decode('utf-8'))
        access_token = re.sub('.*access_token=', '', access_token)

        if not access_token:
            self.logger.info('Login failed with ptc login')
            raise exceptions.LoginFailedException('Error getting access token')

        self.logger.info('Login successed to ptc with username=' + username)
        self.auth.access_token = access_token
        return self.auth
