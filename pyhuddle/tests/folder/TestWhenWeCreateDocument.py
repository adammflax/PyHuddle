import unittest
from pyhuddle.files.files import Folder, Document
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.document.fakeFile import FakeFile
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderDocumentCreate import FakeFolderDocumentCreate
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

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

