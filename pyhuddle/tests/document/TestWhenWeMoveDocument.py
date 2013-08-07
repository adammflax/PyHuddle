import unittest
from pyhuddle.api.files.files import Document, Folder
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentMove import FakeDocumentMove
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeMoveADocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeDocumentMove()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.document = Document(self.client, "IAmAFakeUrl")
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.result = self.document.moveTo(self.folder)

    def test_makeSureWeGetBackAValidParent(self):
        self.assertNotEqual(self.result.lazyGet().getLink("parent"), self.document.lazyGet().getLink("parent"))

    def test_makeSureWeGetBackADocument(self):
        self.assertIsInstance(self.result, Document)

if __name__ == '__main__':
    unittest.main()

