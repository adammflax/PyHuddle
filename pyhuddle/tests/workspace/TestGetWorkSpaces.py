from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.workspace.fakeWorkspacerServer import FakeAuthServer
import unittest
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeGetWorkspaces(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeAuthServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)

    def test_makeSureWeHave8Workspaces(self):
        self.assertEqual(len(self.client.getWorkSpaces()), 8)

    def test_makeSureWeHaveDocumentLibraryLink(self):
        self.assertEqual(self.client.getWorkSpaces()[0].lazyGet().getLink("documentLibrary"), "http://api.huddle.dev/files/folders/2227259")

    def test_makeSureWeHaveTitleOfAcceptanceTest(self):
        self.assertEqual(self.client.getWorkSpaces()[0].lazyGet().getTitle(), "AcceptanceTest")

if __name__ == '__main__':
    unittest.main()

