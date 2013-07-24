import json
from oauth2 import token
from oauth2.handleaccesstoken import HandleAccessToken
from oauth2.oauthapi import OAuth
from tests.fakeParser import FakeParser
from tests.httpFakeAdapter import HttpFakeAdapter
from tests.login.fakeAuthServer import FakeAuthServer

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
