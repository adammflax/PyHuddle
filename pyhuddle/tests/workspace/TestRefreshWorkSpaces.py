import unittest
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken
from pyhuddle.tests.workspace.fakeWorkspacerServer import FakeAuthServer

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

