import unittest

from PokeApi.auth import PTCLogin, Auth, GoogleLogin


class AuthTests(unittest.TestCase):

    def test_ptc_login(self):
        login = PTCLogin().login_user('username', 'password')

    def test_google_login(self):
        login = GoogleLogin().login_user('username', 'password')