import unittest

from api.huddleclient import HuddleClient
from api.tasks.tasks import Task
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken
from tests.tasks.FakeTasksServer.fakeTaskUpdate import FakeTaskUpdate

__author__ = 'adam.flax'

class WhenWeUpdateATask(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeTaskUpdate()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.task = Task(self.client, "IamAFakeUrl")
        self.result = self.task.edit(title="newTitle")

    def test_makeSureWeHaveNewName(self):
        self.assertEqual("newTitle", self.result.lazyGet().getTitle())

if __name__ == '__main__':
    unittest.main()

