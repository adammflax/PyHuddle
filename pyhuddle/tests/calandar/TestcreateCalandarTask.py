
import unittest
from api.calendar.calendar import Calendar
from api.huddleclient import HuddleClient
from api.tasks.tasks import Task
from tests.calandar.FakeCalandarServers.fakeCalandarTaskCreateServer import FakeCalandarTaskCreateServer
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken

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
        self.assertEqual("http://api.huddle.dev/v2/calendar/events/18279", self.result.selfLink)

if __name__ == '__main__':
    unittest.main()

