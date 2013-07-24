from urllib import parse

__author__ = 'adam.flax'


class OAuth(object):

    def __init__(self, config, request):
        self._config = config
        self._request = request

    def obtainAccessToken(self, code):
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
                "code": code}

        return self._request.postRequest(url, header, parse.urlencode(body))

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

        return self._request.postRequest(url, header, parse.urlencode(body))