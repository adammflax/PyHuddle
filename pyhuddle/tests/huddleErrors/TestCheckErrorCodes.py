import unittest
from pyhuddle.api.huddle_errors import HandleCodeResponse, HuddleBadRequestError, HuddleAuthenticationError, HuddleForbiddenError, HuddleNotFoundError, HuddleConflictError, HuddleGoneError, HuddleBadResponseError

__author__ = 'adam.flax'

class WhenWeHandleHttpResponseToCheckForStatusCode(unittest.TestCase):
    def setUp(self):
        self.code = HandleCodeResponse()

    def test_ifWeGetA200ThrowNoError(self):
        self.assertIsNone(self.makeRequest(200))

    def test_ifWeGetA204ThrowNoError(self):
        self.assertIsNone(self.makeRequest(204))

    def test_ifWeGetA301ThrowNoError(self):
        self.assertIsNone(self.makeRequest(301))

    def test_makeSure400RaisesBadRequest(self):
        self.assertRaises(HuddleBadRequestError, self.makeRequest, 400)

    def test_makeSure401RaisesAuthentication(self):
        self.assertRaises(HuddleAuthenticationError, self.makeRequest, 401)

    def test_makeSure403RaisesForbidden(self):
        self.assertRaises(HuddleForbiddenError, self.makeRequest, 403)

    def test_makeSure404RaisesNotFound(self):
        self.assertRaises(HuddleNotFoundError, self.makeRequest, 404)

    def test_makeSure409RaisesConflict(self):
        self.assertRaises(HuddleConflictError, self.makeRequest, 409)

    def test_makeSure410RaisesGone(self):
        self.assertRaises(HuddleGoneError, self.makeRequest, 410)

    def test_makeSureAnyBadCodeRaisesError(self):
        self.assertRaises(HuddleBadResponseError, self.makeRequest, 510)
        self.assertRaises(HuddleBadResponseError, self.makeRequest, 500)
        self.assertRaises(HuddleBadResponseError, self.makeRequest, 700)

    def makeRequest(self, code):
        request = {"Headers" : {"status" : code}, "Body" : {"I Am A Body"}}
        self.code.CheckForErrors(request)

if __name__ == '__main__':
    unittest.main()

