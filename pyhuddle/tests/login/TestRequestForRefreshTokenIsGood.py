import unittest
import json
from pyhuddle.oauth2.handle_access_token import OAuth
from pyhuddle.oauth2.token import Token
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeAuthServer import FakeAuthServer

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