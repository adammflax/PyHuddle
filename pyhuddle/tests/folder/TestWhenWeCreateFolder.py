import unittest

from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.folder.FakeFolderServers.fakeFolderCreate import FakeFolderCreate
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken


__author__ = 'adam.flax'

class WhenWeCreateFolder(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderCreate()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.result = self.folder.createFolder("I am a title", "description")

    def test_makeSureWeGetBackAFolder(self):
        self.assertIsInstance(self.result, Folder)

    def test_makeSureWeGotFolderWeWanted(self):
        self.assertEqual("I am a title", self.result.lazyGet().getTitle())

    def test_makeSureWeGteDescriptionWeWantedFromCreateWithDescription(self):
        self.assertEqual("description", self.result.lazyGet().getDescription())

if __name__ == '__main__':
    unittest.main()

