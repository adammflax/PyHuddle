import unittest
from pyhuddle.api.files.files import Folder
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderMove import FakeFolderMove
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeMoveFolder(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderMove()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.folderB = Folder(self.client, "newUrl")
        self.result = self.folder.moveTo(self.folderB)

    def test_makeSureWeGetValidParent(self):
        self.assertEqual(self.result.lazyGet().getLink("parent"), "newUrl")

    def test_makeSureWeGetBackAFolder(self):
        self.assertIsInstance(self.result, Folder)

    def test_makeSureWeHaveMoved(self):
        self.assertNotEqual(self.result.selfLink, "IAmAFakeUrl")

if __name__ == '__main__':
    unittest.main()

