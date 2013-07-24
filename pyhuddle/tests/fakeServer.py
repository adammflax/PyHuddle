import json

__author__ = 'adam.flax'

class fakeServer(object):
    def __init__(self):
        goodHeader = {"Content-Type" : "application/vnd.huddle.data+json", "status" : 200, "Cache-Control" : "no-store"}
        self.goodResponse = {"Headers" : goodHeader, "Body" : {}}

    def get(self, url, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response

        return self.goodResponse

    def post(self, url,body, header):
        return self.badResponse(405)

    def put(self, url, body, header):
        return self.badResponse(405)

    def delete(self,  url, header):
        return self.badResponse(405)

    def isRequestValid(self, url, header):
        if header['Authorization'] != "OAuth2 token":
            return self.badResponse(401)
        if header['Accept'] != "application/vnd.huddle.data+json":
            return self.badResponse(406)

        return True

    def isRequestWithBodyValid(self, url, header, body):
        response = self.isRequestValid(url, header)

        if response is not True:
            return response

        try:
            json.loads(body)
        except ValueError:
            return self.badResponse(400)

        return True

    def badResponse(self, code):
        badHeader = {"Content-Type" : "application/json", "status" :code , "Cache-Control" : "no-store"}
        badBody = '{"error" : "badResponse", "error_description" : "badResponse", "error_uri" : "https://api.huddle.fake"}'

        return {"Headers" : badHeader, "Body" : badBody}