import unittest

from api.huddleclient import HuddleClient
from api.tasks.tasks import Task
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken
from tests.tasks.FakeTasksServer.fakeTaskDelete import FakeTaskDelete


__author__ = 'adam.flax'

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

