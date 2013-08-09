import unittest
from pyhuddle.files.files import Document
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentRestore import FakeDocumentRestore
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

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
        self.document.metaData.graveyard.append(self.document) #add to the graveyard
        self.result = self.document.restore()

    def test_makeSureWeGetBackADocument(self):
        self.assertIsInstance(self.result, Document)

    def test_makeSureWeGetBackRightDocument(self):
        self.assertEqual(self.result.metaData.getTitle(), "I Am a test")

    def test_makeSureGraveyardHaBeenDecreased(self):
        self.assertEqual(len(self.document.metaData.graveyard), 0)

if __name__ == '__main__':
    unittest.main()

