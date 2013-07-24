from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.workspace.fakeWorkspacerServer import FakeAuthServer
import unittest
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeRefreshWorkspaces(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeAuthServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        client = HuddleClient(handleAccessToken, request, config)
        self.ws = client.getWorkSpaces()[0]

    def test_makeSureRefreshGetsSameResource(self):
        self.assertEqual(self.ws.selfLink, self.ws.refresh().selfLink)

if __name__ == '__main__':
    unittest.main()

