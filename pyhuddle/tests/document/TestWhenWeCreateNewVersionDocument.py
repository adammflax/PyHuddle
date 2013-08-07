import unittest
from pyhuddle.api.files.files import Document
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentNewVersion import FakeDocumentNewVersion
from pyhuddle.tests.document.fakeFile import FakeFile
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeCreateANewVersionOfTheDocument(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeDocumentNewVersion()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.document = Document(self.client, "IAmAFakeUrl")
        self.fakeFile = FakeFile("test.txt", "contents")
        self.result = self.document.createNewVersion(self.fakeFile, "foo", "bar")

    def test_makeSureWeGetBackADocument(self):
        self.assertIsInstance(self.result, Document)

    def test_makeSureWeGetBackRightDocumentTitle(self):
        self.assertEqual("foo", self.result.lazyGet().getTitle())

    def test_makeSureWeGetBackRightDocumentDescription(self):
        self.assertEqual("bar", self.result.lazyGet().getDescription())

if __name__ == '__main__':
    unittest.main()

