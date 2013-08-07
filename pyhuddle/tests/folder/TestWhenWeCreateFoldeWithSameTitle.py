import unittest
from pyhuddle.api.huddle_errors import HuddleConflictError
from pyhuddle.api.files.files import Folder
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderCreate import FakeFolderCreate
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeCreateFolderWithExistingName(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderCreate()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")

    def test_makeSureWeGetBackAFolder(self):
        self.assertRaises(HuddleConflictError, self.folder.createFolder, "dfgdg", "description")


if __name__ == '__main__':
    unittest.main()

