import json
import sys
from urllib import parse
import webbrowser
from . import  token
from pyhuddle.oauth2.token import Token


class HandleAccessToken(object):

    def __init__(self, adapter, config, createToken=None):
        """
        If you want to write your own createAccesstoken method (i.e you are not using OOB
        You can do so by chucking your function as an optional parameter e.g.
        (self,request, config, createToken=function())
        """
        self._adapter = adapter
        self.oauthToken = None

        #make sure their request implementation matches our adapter
        if not hasattr(adapter, "getRequest"):
            raise TypeError("Your http request implementation is missing the getRequest method")
        if not hasattr(adapter, "postRequest"):
            raise TypeError("Your http request implementation is missing the postRequest method")
        if not hasattr(adapter, "deleteRequest"):
             raise TypeError("Your http request implementation is missing the deleteRequest method")
        if not hasattr(adapter, "putRequest"):
               raise TypeError("Your http request implementation is missing the putRequest method")

        self._config = config
        self._oauth = OAuth(config, self._adapter)

        if createToken is not None:
            self.createAccessToken = createToken
        else:
            self.createAccessToken = self.createAccessTokenReplacement()


    def getAccessToken(self):
        """
        Handles getting you an access token and making sure it has not expired. This method will first look to get you
        a token from the file you specify from the config. If it can't find a valid token in the file or the file at all
        it will request a new token from huddle.

        >>>getAccessToken()
        <OAuth2.handleAccessToken.handleAccessToken object>

        This method may abort the python script if it cannot create a token object.
        This will happen when we get a non token response from the server e.g. a 400 from an invalid client
        """

        #lets see if we have an oauth code
        if self.oauthToken is None:
            self.oauthToken = self.createAccessToken

        if self.oauthToken.isExpired(): #check to see if its expired if so refresh it
            self.oauthToken = self.refreshAccessToken()

        return self.oauthToken #return out access token

    def createAccessTokenReplacement(self):
        """
        Creates an access token by getting an auth code from the user and exchanging it with the server.
        This method will also save a token to the file specified in your config. You should not ever need to call this
        method. Instead call getAccessToken()

        >>>createAccessToken()
        <OAuth2.handleAccessToken.handleAccessToken object>

        This method may abort the python script if it cannot create a token object.
        This will happen when we get a non token response from the server e.g. a 400 from an invalid client
        """

        url = self._config['OAUTH2ENDPOINT']['huddleAuthServer'] + "request?response_type=code" + \
                        "&client_id=" + self._config['OAUTH2']['clientID'] + \
                        "&redirect_uri=" + self._config['OAUTH2']['redirectUri']
        webbrowser.open_new(url)
        code = input('Please enter the code from your web browser:')

        response = self._oauth.obtainAccessTokenBy3LeggedOAuth(code)
        responseBody = json.loads(response['Body'])

        try:
            oauthToken = Token(responseBody)
        except TypeError as e:
            print ("Bad response when requesting a token " + str(response))
            sys.exit()

        return oauthToken


    def refreshAccessToken(self):
        """
        Refreshes an access token  with the server. This method will also update the new token to the file specified
        in your config. You should not ever need to call this method. Instead call getAccessToken()

        >>>__refreshAccessToken()
        <OAuth2.handleAccessToken.handleAccessToken object>

        This method may abort the python script if it cannot create a token object.
        This will happen when we get a non token response from the server e.g. a 400 from an invalid client

        Raises an Assert Error if it attempts to refresh a token object that has no getRefreshToken method
        """

        assert hasattr(self.oauthToken, "getRefreshToken")

        #turn the response into json

        response = self._oauth.refreshAccessToken(self.oauthToken)
        responseBody = json.loads(response['Body'])

        try:
            oauthToken = token.Token(responseBody)
        except TypeError:
            print ("Bad response when refreshing the token " + str(responseBody))
            sys.exit()

        return oauthToken

class OAuth():

    def __init__(self, config, adapter):
        self._config = config
        self._adapter = adapter

    def obtainAccessTokenBy3LeggedOAuth(self, auth_code):
        """
        Makes a POST request to huddle asking for a access token
        For instructions on how to do this look here https://code.google.com/p/huddle-apis/wiki/OauthIntegration#Obtaining_Access_and_Refresh_Tokens
        This method will return the body response this may ever be the new token or the error response
        """
        header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        url = self._config['OAUTH2ENDPOINT']['huddleAccessTokenServer']

        body = {"grant_type": "authorization_code",
                "client_id": self._config['OAUTH2']['clientID'],
                "redirect_uri": self._config['OAUTH2']['redirectUri'],
                "code": auth_code}

        return self._adapter.postRequest(url, header, parse.urlencode(body))

    def refreshAccessToken(self, token):
        """
        Makes a POST request to huddle asking to refresh an old access token
        For instructions on how to do this look here https://code.google.com/p/huddle-apis/wiki/OauthIntegration#Obtaining_Access_and_Refresh_Tokens
        This method will return the body response this may ever be the new token or the error response
        """
        header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        url = self._config['OAUTH2ENDPOINT']['huddleAccessTokenServer']

        body = {"grant_type": "refresh_token",
                "client_id": self._config['OAUTH2']['clientID'],
                "refresh_token": token.getRefreshToken()
        }

        return self._adapter.postRequest(url, header, parse.urlencode(body))