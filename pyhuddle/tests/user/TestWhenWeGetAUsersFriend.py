import unittest

from api.huddleclient import HuddleClient
from api.user.user import User
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeHandleAccessToken import FakeHandleAccessToken
from tests.user.FakeUserServer.FakeFriendServer import FakeFriendServer

__author__ = 'adam.flax'

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

