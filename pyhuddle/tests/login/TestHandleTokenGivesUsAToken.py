import unittest
from pyhuddle.oauth2.token import Token
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken


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
