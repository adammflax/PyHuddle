import unittest

from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.folder.FakeFolderServers.fakeFolderCopy import FakeFolderCopy
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeCopyFolder(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderCopy()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.folderB = Folder(self.client, "newUrl")
        self.result = self.folder.copyTo(self.folderB)

    def test_makeSureWeGetValidParent(self):
        self.assertEqual(self.result.selfLink, "http://api.huddle.dev/files/folders/2227259")

    def test_makeSureWeGetBackAFolder(self):
        self.assertIsInstance(self.result, Folder)

    def test_makeSureWeHaveMoved(self):
        self.assertNotEqual(self.result.selfLink, "IAmAFakeUrl")

if __name__ == '__main__':
    unittest.main()

