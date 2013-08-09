import unittest
from pyhuddle.api.huddle_client import HuddleClient
from pyhuddle.user.user import User
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeHandleAccessToken import FakeHandleAccessToken
from pyhuddle.tests.user.FakeUserServer.FakeFriendServer import FakeFriendServer


class WhenWeGetUsersFriends(unittest.TestCase):
    def setUp(self):
        handleAccessToken = FakeHandleAccessToken()
        fakeParser = FakeParser()
        server = FakeFriendServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.client = HuddleClient(handleAccessToken, request, config)
        self.user = self.client.user
        self.result = self.user.getFriends()

    def test_makeSureWeGetOneFriendBack(self):
        self.assertEqual(1, len(self.result))

    def test_makeSureWeGetBackAUser(self):
        self.assertIsInstance(self.result[0], User)

if __name__ == '__main__':
    unittest.main()

