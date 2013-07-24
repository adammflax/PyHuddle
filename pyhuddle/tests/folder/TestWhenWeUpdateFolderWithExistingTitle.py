import unittest

from api.files.files import Folder
from api.huddleerrors import HuddleConflictError
from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.folder.FakeFolderServers.fakeFolderUpdate import FakeFolderUpdate
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken


__author__ = 'adam.flax'

class WhenWeUpdateFolderWithANameThatExists(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderUpdate()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")

    def test_makeSureWeGetBackAFolder(self):
         self.assertRaises(HuddleConflictError, self.folder.updateFolder, "dfgdg", "description")

if __name__ == '__main__':
    unittest.main()

