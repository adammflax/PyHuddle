from oauth2.token import Token
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

import unittest

class WhenWeAskTokenHandlerForAToken(unittest.TestCase):
    def setUp(self):
        self.handleAccessToken = FakeHandleAccessToken()

    def test_getAccessToken(self):
        token = self.handleAccessToken.getAccessToken()

        self.assertTrue(isinstance(token, Token))
        self.assertEqual(token.getAccessToken(), "token")
        self.assertEqual(token.getRefreshToken(), "tokenRefresh")
        self.assertEqual(token.getExpiry(), 3600)
        self.assertFalse(token.isExpired())


if __name__ == '__main__':
    unittest.main()
