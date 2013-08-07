import unittest
from pyhuddle.api.files.files import Folder, Document
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentCopy import FakeDocumentCopy
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

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

