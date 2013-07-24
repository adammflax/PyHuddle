import unittest
import json
from oauth2.oauthapi import OAuth
from oauth2.token import Token
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeAuthServer import FakeAuthServer

class WhenWeAskServerToRefreshToken(unittest.TestCase):
    def setUp(self):
        fakeParser = FakeParser()
        server = FakeAuthServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        jsonToken = json.loads('{"access_token" : "token", "expires_in" : 3600, "refresh_token" : "tokenRefresh"}')

        self.oAuth = OAuth(config, request)
        self.token  = Token(jsonToken)

    def test_getAccessToken(self):
        request  = self.oAuth.refreshAccessToken(self.token)
        body = '{"access_token" : "refreshedToken", "expires_in" : 3600, "refresh_token" : "re-refreshToken"}'

        self.assertEqual(request['Headers']['status'], 200)
        self.assertEqual(request['Body'], body)

if __name__ == '__main__':
    unittest.main()