import unittest
from api.files.files import Document
from api.huddleclient import HuddleClient
from tests.document.FakeDocumentServers.fakeDocumentUpdate import FakeDocumentUpdate
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeUpdateADocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeDocumentUpdate()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.document = Document(self.client, "IAmAFakeUrl")
        self.result = self.document.update("foo", "bar")

    def test_makeSureWeGetBackADocument(self):
        self.assertIsInstance(self.result, Document)

    def test_makeSureWeGetBackRightDocumentTitle(self):
        self.assertEqual(self.result.lazyGet().getTitle(), "foo")

    def test_makeSureWeGetBackRightDocumentDescription(self):
        self.assertEqual(self.result.lazyGet().getDescription(), "bar")

if __name__ == '__main__':
    unittest.main()

