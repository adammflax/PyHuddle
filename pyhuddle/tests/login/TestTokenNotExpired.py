import json
from oauth2.token import Token

__author__ = 'adam.flax'

import unittest


class WhenWeCheckToMakeSureTokenHasNotExpired(unittest.TestCase):
    def setUp(self):
        self.newJson = json.loads('{"access_token" : "token", "expires_in" : 3600, "refresh_token" : "tokenRefresh"}')
        self.expiredJson =  json.loads('{"access_token" : "token", "expires_in" : -3600, "refresh_token" : "tokenRefresh"}')

    def test_newJsonShouldOfNotExpired(self):
        token = Token(self.newJson)
        self.assertFalse(token.isExpired())

    def test_expiredJsonShouldOfExpired(self):
        token = Token(self.expiredJson)
        self.assertTrue(token.isExpired)


if __name__ == '__main__':
    unittest.main()
