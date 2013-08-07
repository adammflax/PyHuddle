import unittest
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.tests.calandar.FakeCalandarServers.fakeCalandarServer import FakeCalandarServer
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

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

