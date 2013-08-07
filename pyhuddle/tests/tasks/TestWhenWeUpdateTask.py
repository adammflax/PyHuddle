import unittest
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.api.tasks.tasks import Task
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken
from pyhuddle.tests.tasks.FakeTasksServer.fakeTaskUpdate import FakeTaskUpdate

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

