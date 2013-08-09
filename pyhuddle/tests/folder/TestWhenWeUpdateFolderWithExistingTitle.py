import unittest
from pyhuddle.api.huddle_errors import HuddleConflictError
from pyhuddle.files.files import Folder
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderUpdate import FakeFolderUpdate
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

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

