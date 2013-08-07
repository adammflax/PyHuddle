import json
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentMove(FakeDocumentServer):

    def put(self,  url, body, header):
        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/documents/2225001/edit":
            return self.badResponse(404, "not found!")

        jsonBody = json.loads(body)

        if jsonBody.get("links")[13]['rel'] != "parent":
            return self.badResponse(400, "bad data no parent link found in jsonBody")

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 202
        newResponse['Headers']['link'] = '<http://api.huddle.dev/files/folders/122345>; rel="parent"'
        newResponse['Body'] = {}

        return newResponse
