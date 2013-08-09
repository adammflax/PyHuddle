
import unittest
from pyhuddle.calandar.calandar import Calendar
from pyhuddle.tasks.tasks import Task
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.api.huddle_client import HuddleClient

from pyhuddle.tests.calandar.FakeCalandarServers.fakeCalandarTaskCreateServer import FakeCalandarTaskCreateServer
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken

__author__ = 'adam.flax'

class WhenWCreateTask(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeCalandarTaskCreateServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.calandar = Calendar(self.client, "IAmAFakeUrl")
        self.result = self.calandar.createTask(title="foo", description="bar")

    def test_makeSureWeHaveTypeTask(self):
        self.assertIsInstance(self.result, Task)

    def test_makeSureWeHaveRightTask(self):
        self.assertEqual("http://api.huddle.dev/v2/calandar/events/18279", self.result.selfLink)

if __name__ == '__main__':
    unittest.main()

