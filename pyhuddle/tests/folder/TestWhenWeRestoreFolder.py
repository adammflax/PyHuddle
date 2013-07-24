import unittest
from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.folder.FakeFolderServers.fakeFolderRestore import FakeFolderRestore
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeRestoreFolder(unittest.TestCase):

    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderRestore()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.folder.lazyGet().graveyard.append(self.folder.lazyGet()) #add to graveyard

        self.result = self.folder.restoreFolder(0)

    def test_makeSureWeGetValidParent(self):
        self.assertEqual(self.result.selfLink, "http://api.huddle.dev/files/folders/2227259")

    def test_makeSureWeGetBackAFolder(self):
        self.assertIsInstance(self.result, Folder)

    def test_makeSureGraveyardHaBeenIncreased(self):
        self.assertEqual(len(self.folder.lazyGet().graveyard), 0)


if __name__ == '__main__':
    unittest.main()

