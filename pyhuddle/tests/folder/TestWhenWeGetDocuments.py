import unittest

from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.folder.FakeFolderServers.fakeFolderGet import FakeFolderGet
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken


__author__ = 'adam.flax'

class WhenWeGetDocuments(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderGet()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.result = self.folder.getDocuments()

    def test_makeSureWeGetFoldersListBack(self):
        self.assertEqual(len(self.result), 1)

    def test_makeSureDocumentHasValidUrl(self):
        self.assertEqual(self.result[0].selfLink, "http://api.huddle.dev/files/documents/2227569")

    def test_makeSureSubFolderUrlIsNotParentFolderUrl(self):
        self.assertNotEqual(self.result[0].selfLink, self.folder.selfLink)

if __name__ == '__main__':
    unittest.main()

