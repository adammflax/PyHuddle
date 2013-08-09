import unittest
from pyhuddle.files.files import Folder
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderGet import FakeFolderGet
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeGetFolder(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderGet()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.result = self.folder.getFolders()

    def test_makeSureWeGetFoldersListBack(self):
        self.assertEqual(len(self.result), 1)

    def test_makeSureSubFolderHasValidUrl(self):
        self.assertEqual(self.result[0].selfLink, "http://api.huddle.dev/files/folders/2227556")

    def test_makeSureSubFolderUrlIsNotParentFolderUrl(self):
        self.assertNotEqual(self.result[0].selfLink, self.folder.selfLink)

if __name__ == '__main__':
    unittest.main()

