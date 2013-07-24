from urllib import parse
import urllib
from tests.fakeServer import fakeServer

__author__ = 'adam.flax'

class FakeAuthServer(fakeServer):

    def __init__(self):
        newHeader = {"Content-Type" : "application/json", "status" : 200, "Cache-Control" : "no-store"}
        newBody = '{"access_token" : "token", "expires_in" : 3600, "refresh_token" : "tokenRefresh"}'
        refreshBody = '{"access_token" : "refreshedToken", "expires_in" : 3600, "refresh_token" : "re-refreshToken"}'

        badHeader = {"Content-Type" : "application/json", "status" :400, "Cache-Control" : "no-store"}
        badBody = '{"error" : "badFormat", "badFormat" : "badFormat", "badFormat" : "badFormat"}'

        self.goodResponse = {"Headers" : newHeader, "Body" : newBody}
        self.goodResponseRefresh = {"Headers" : newHeader, "Body" : refreshBody}
        self.badResponse = {"Headers" : badHeader, "Body" : badBody}

    def get(self, url, header):
        pass

    def post(self, url,body, header):
        requestUrl = url.rsplit('/',1)

        if requestUrl[1] == "token":
            bodyData = urllib.parse.parse_qs(body)

            if bodyData['grant_type'][0] == "authorization_code":
                result = self.checkForAccessTokenRequest(header, body)
                return self.goodResponse if result else self.badResponse

            elif bodyData['grant_type'][0] == "refresh_token":
                result = self.checkForRefreshTokenRequest(header, body)
                return self.goodResponseRefresh if result else self.badResponse
            else:
                return self.badResponse

        return self.notFound()


    def put(self, url, header):
         pass

    def delete(self,  url, header, body):
        pass

    def notFound(self):
        newHeader = {"Content-Type" : "application/json", "status" : 404, "Cache-Control" : "no-store"}
        newBody = {"Error" : "not found", "error_description" : "page not found", "error_uri" : "www.fake.com"}

        return {"Headers" : newHeader, "Body" : parse.urlencode(newBody)}

    def checkForRefreshTokenRequest(self, header, body):

        bodyData = urllib.parse.parse_qs(body)

        if bodyData['client_id'][0] != "fakeClientID":
            return False

        if "grant_type" not in bodyData or "refresh_token" not in bodyData or "client_id"  not in bodyData:
            return False

        if bodyData["refresh_token"][0] != "tokenRefresh":
            return False

        return True

    def checkForAccessTokenRequest(self, header, body):
        bodyData = urllib.parse.parse_qs(body)

        if bodyData['client_id'][0] != "fakeClientID":
            return False

        if "grant_type" not in bodyData or "code" not in bodyData \
            or "client_id"  not in bodyData or "redirect_uri"  not in bodyData:
            return False

        if bodyData["code"][0] != "123456":
            return False

        return True