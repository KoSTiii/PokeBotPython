import requests
import re
import json

import config

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#
#   Login class manager
#
class LoginManager():
    LoginType = ["PTC", "Google"]

    # constructor
    def __init__(self, type, username, password):
        if type not in LoginManager.LoginType:
            type = "PTC"

        self.type = "PTC"
        self.username = username
        self.password = password

        self.accessToken = None

        self.session = requests.session()
        self.session.headers.update({'User-Agent': 'Niantic App'})
        self.session.verify = False

    # login to server
    def login(self):
        if self.type == LoginManager.LoginType[0]:
            return self.login_ptc()
        else:
            return self.login_google()

    def login_google(self):
        return False

    def login_ptc(self):
        head = {'User-Agent': 'niantic'}
        r = self.session.get(config.LOGIN_URL, headers=head)
        jdata = json.loads(r.content.decode('utf-8'))
        data = {
            'lt': jdata['lt'],
            'execution': jdata['execution'],
            '_eventId': 'submit',
            'username': self.username,
            'password': self.password,
        }
        r1 = self.session.post(config.LOGIN_URL, data=data, headers=head)

        ticket = None
        try:
            ticket = re.sub('.*ticket=', '', r1.history[0].headers['Location'])
        except Exception as e:
            print('Error ' + r1.json()['errors'][0])
            return False

        data1 = {
            'client_id': 'mobile-app_pokemon-go',
            'redirect_uri': 'https://www.nianticlabs.com/pokemongo/error',
            'client_secret': config.PTC_CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'code': ticket,
        }
        r2 = self.session.post(config.LOGIN_OAUTH, data=data1)
        access_token = re.sub('&expires.*', '', r2.content.decode('utf-8'))
        access_token = re.sub('.*access_token=', '', access_token)

        if not access_token:
            return False

        self.set_access_token(access_token)
        return True

    # retrurn accessToken
    def get_access_token(self):
        return self.accessToken

    def set_access_token(self, token):
        self.accessToken = token
