import unittest
from api.calendar.calendar import Calendar
from api.huddleclient import HuddleClient
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.calandar.FakeCalandarServers.fakeCalandarServer import FakeCalandarServer
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWeGteWorkspaceCalandar(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeCalandarServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.result = self.client.getWorkSpaces()[0].getCalandar()

    def test_makeSureWeHaveTypeCalandar(self):
        self.assertIsInstance(self.result, Calendar)

    def test_makeSureWeHaveRightCalandar(self):
        self.assertEqual("AcceptanceTest", self.result.lazyGet().jsonObj['workspace']['displayName'])

    def test_makeSureHasRightEvents(self):
        self.assertEqual(1, len(self.result.lazyGet().jsonObj['events']))



if __name__ == '__main__':
    unittest.main()

