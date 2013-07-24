from oauth2.oauthapi import OAuth
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeAuthServer import FakeAuthServer

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
        request  = self.oAuth.obtainAccessToken("123456")
        body = '{"access_token" : "token", "expires_in" : 3600, "refresh_token" : "tokenRefresh"}'

        self.assertEqual(request['Headers']['status'], 200)
        self.assertEqual(request['Body'], body)


if __name__ == '__main__':
    unittest.main()