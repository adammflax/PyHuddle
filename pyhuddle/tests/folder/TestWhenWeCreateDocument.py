import unittest
from api.files.files import Document
from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.document.fakeFile import FakeFile
from tests.fakeParser import FakeParser
from tests.folder.FakeFolderServers.fakeFolderDocumentCreate import FakeFolderDocumentCreate
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken


__author__ = 'adam.flax'

class WhenWeCreateDocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderDocumentCreate()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        file = FakeFile("test.txt", "contents")
        self.result = self.folder.createDocument(file)

    #MOST of the tests are done in the WhenWeUplaodFile

    def test_makeSureWeGetBackADocument(self):
         self.assertIsInstance(self.result, Document)

if __name__ == '__main__':
    unittest.main()

