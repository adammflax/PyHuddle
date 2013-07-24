import unittest
from api.files.files import Document
from api.files.files import Folder
from api.huddleclient import HuddleClient
from tests.document.FakeDocumentServers.fakeDocumentDelete import FakeDocumentDelete
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeDeleteADocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeDocumentDelete()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.document = Document(self.client, "IAmAFakeUrl")
        self.result = self.document.delete()

    def test_makeSureWeGetBackAFolder(self):
        self.assertIsInstance(self.result, Folder)

    def test_makeSureGraveyardHaBeenIncreased(self):
        self.assertEqual(len(self.document.lazyGet().graveyard), 1)

if __name__ == '__main__':
    unittest.main()

