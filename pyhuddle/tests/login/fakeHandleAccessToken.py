import json
from pyhuddle.oauth2 import token
from pyhuddle.oauth2.oauth_api import OAuth
from pyhuddle.tests.fakeParser import FakeParser
from pyhuddle.oauth2.handle_access_token import HandleAccessToken
from pyhuddle.tests.httpFakeAdapter import HttpFakeAdapter
from pyhuddle.tests.login.fakeAuthServer import FakeAuthServer

__author__ = 'adam.flax'

class FakeHandleAccessToken(HandleAccessToken):

    def __init__(self):
        self._token = json.loads('{"access_token" : "token", "expires_in" : 3600, "refresh_token" : "tokenRefresh"}')
        fakeParser = FakeParser()
        server = FakeAuthServer()

        config = fakeParser.getParser()
        request = HttpFakeAdapter(server)

        self.oAuth = OAuth(config, request)

    def getAccessToken(self):
        token = self.createAccessToken()

        if token.isExpired() is True:
            token = self.refreshAccessToken(token)

        return token

    def createAccessToken(self):
        response = self.oAuth.obtainAccessToken("123456")
        responseBody = json.loads(response['Body'])

        oauthToken = token.Token(responseBody)

        return oauthToken

    def refreshAccessToken(self, tokenData):
        response = self.oAuth.refreshAccessToken(tokenData)
        responseBody = json.loads(response['Body'])

        oauthToken = token.Token(responseBody)

        return oauthToken
