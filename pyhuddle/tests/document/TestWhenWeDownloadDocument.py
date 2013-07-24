import unittest
from api.files.files import Document
from api.huddleclient import HuddleClient
from tests.document.FakeDocumentServers.fakeDocumentDownload import FakeDocumentDownload
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeDownloadADocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeDocumentDownload()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.document = Document(self.client, "IAmAFakeUrl")
        self.result = self.document.download()

    def test_makeSureWeGetBackAValidMimeType(self):
        self.assertEqual("text/plain", self.result['mime'])

    def test_makeSureWeGetBackAValidFileName(self):
        self.assertEqual("I Am a test.txt", self.result['filename'])

    def test_makeSureWeGetBackValidBinary(self):
        self.assertEqual("I am the body content for this data!", self.result['binary'])

if __name__ == '__main__':
    unittest.main()

