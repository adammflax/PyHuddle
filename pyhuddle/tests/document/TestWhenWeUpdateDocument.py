import unittest
from pyhuddle.api.files.files import Document
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentUpdate import FakeDocumentUpdate
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

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

