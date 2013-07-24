import unittest
from api.files.files import Document
from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.document.FakeDocumentServers.fakeDocumentCopy import FakeDocumentCopy
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeCopyTheDocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeDocumentCopy()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.document = Document(self.client, "IAmAFakeUrl")
        self.result = self.document.copyTo(self.folder)

    def test_makeSureWeGetBackADocument(self):
        self.assertIsInstance(self.result, Document)

    def test_makeSureWeHaveMoved(self):
        self.assertNotEqual(self.result.selfLink, "IAmAFakeUrl")

if __name__ == '__main__':
    unittest.main()

