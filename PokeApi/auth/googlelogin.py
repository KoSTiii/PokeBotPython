import json
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from .login import Login, Auth
from .. import exceptions

# disable insecure warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


""" Google Login class for login to pokemon server with google account
"""
class GoogleLogin(Login):

    """ @retrun provider string for auth object
    """
    def get_provider(self):
        return 'google'

    """ Login into server with username and password
    @return auth object
    """
    def login_user(self, username, password):
        pass