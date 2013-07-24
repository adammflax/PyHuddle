import json
import sys
import webbrowser
from . import  token
from . import oauthapi

class HandleAccessToken(object):

    def __init__(self, request, config, createToken=None):
        """
        If you want to write your own createAccesstoken method (i.e you are not using OOB
        You can do so by chucking your function as an optional parameter e.g.
        (self,request, config, createToken=function())
        """
        self.request = request
        self.oauthToken = None

        #make sure their request implementation matches our adapter
        if not hasattr(request, "getRequest"):
            raise TypeError("Your http request implementation is missing the getRequest method")
        if not hasattr(request, "postRequest"):
            raise TypeError("Your http request implementation is missing the postRequest method")
        if not hasattr(request, "deleteRequest"):
             raise TypeError("Your http request implementation is missing the deleteRequest method")
        if not hasattr(request, "putRequest"):
               raise TypeError("Your http request implementation is missing the putRequest method")

        self._config = config
        self._oauth = oAuthApi.OAuth(config, self.request)

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

        response = self._oauth.obtainAccessToken(code)
        responseBody = json.loads(response['Body'])

        try:
            oauthToken = token.Token(responseBody)
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





