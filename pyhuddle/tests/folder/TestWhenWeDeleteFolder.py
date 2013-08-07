import unittest
from pyhuddle.api.files.files import Folder
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderDelete import FakeFolderDelete
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeDeleteFolder(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFolderDelete()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.folder = Folder(self.client, "IAmAFakeUrl")
        self.result = self.folder.deleteFolder()

    def test_makeSureWeGetValidParent(self):
        self.assertEqual(self.result.selfLink, "http://api.huddle.dev/files/folders/1371761")

    def test_makeSureWeGetBackAFolder(self):
       self.assertIsInstance(self.result, Folder)

    def test_makeSureGraveyardHaBeenIncreased(self):
        self.assertEqual(len(self.folder.lazyGet().graveyard), 1)


if __name__ == '__main__':
    unittest.main()

