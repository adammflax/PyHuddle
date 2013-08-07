import unittest
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.api.tasks.tasks import Task
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken
from pyhuddle.tests.tasks.FakeTasksServer.fakeTaskDelete import FakeTaskDelete

class WhenWeDeleteATask(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeTaskDelete()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.task = Task(self.client, "IAmAFakeUrl")
        self.result = self.task.delete()

    def test_makeSureWeHaveTypeNone(self):
        self.assertIsNone(self.result)


if __name__ == '__main__':
    unittest.main()

