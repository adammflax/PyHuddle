import unittest

from api.huddleclient import HuddleClient
from tests.calandar.FakeCalandarServers.fakeCalandarServer import FakeCalandarServer
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken


__author__ = 'adam.flax'

class WhenWeAskForTasksOncCalandarList(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeCalandarServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.calandar = self.client.getWorkSpaces()[0].getCalandar()
        self.result = self.calandar.getTasks()

    def test_makeSureWeHaveTypeList(self):
        self.assertIsInstance(self.result, list)

    def test_makeSureWeHaveRightAmount(self):
        self.assertEqual(1, len(self.result))

if __name__ == '__main__':
    unittest.main()

