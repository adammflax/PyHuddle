import unittest
from api.files.files import Document
from api.huddleclient import HuddleClient
from tests.document.FakeDocumentServers.fakeDocumentRestore import FakeDocumentRestore
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeRestoreADocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeDocumentRestore()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.document = Document(self.client, "IAmAFakeUrl")
        self.document.lazyGet().graveyard.append(self.document) #add to the graveyard
        self.result = self.document.restore()

    def test_makeSureWeGetBackADocument(self):
        self.assertIsInstance(self.result, Document)

    def test_makeSureWeGetBackRightDocument(self):
        self.assertEqual(self.result.lazyGet().getTitle(), "I Am a test")

    def test_makeSureGraveyardHaBeenDecreased(self):
        self.assertEqual(len(self.document.lazyGet().graveyard), 0)

if __name__ == '__main__':
    unittest.main()

