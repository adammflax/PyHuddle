import unittest

from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.folder.FakeFolderServers.fakeFolderUpdate import FakeFolderUpdate
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken


__author__ = 'adam.flax'

class WhenWeUpdateFolder(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderUpdate()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.result = self.folder.updateFolder("I am a title", "description")

    def test_makeSureWeGetBackAFolder(self):
        self.assertIsInstance(self.result, Folder)

    def test_makeSureWeGetValidParent(self):
        self.assertEqual(self.result.selfLink, "http://api.huddle.dev/files/folders/2227259")

if __name__ == '__main__':
    unittest.main()

