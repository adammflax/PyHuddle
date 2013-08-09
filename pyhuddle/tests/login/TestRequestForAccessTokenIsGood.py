from pyhuddle.oauth2.handle_access_token import OAuth
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeAuthServer import FakeAuthServer

__author__ = 'adam.flax'

import unittest


class WhenWeAskServerForAccessToken(unittest.TestCase):
    def setUp(self):
        fakeParser = FakeParser()
        server = FakeAuthServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.oAuth = OAuth(config, request)

    def test_getAccessToken(self):
        request  = self.oAuth.obtainAccessTokenBy3LeggedOAuth("123456")
        body = '{"access_token" : "token", "expires_in" : 3600, "refresh_token" : "tokenRefresh"}'

        self.assertEqual(request['Headers']['status'], 200)
        self.assertEqual(request['Body'], body)


if __name__ == '__main__':
    unittest.main()
