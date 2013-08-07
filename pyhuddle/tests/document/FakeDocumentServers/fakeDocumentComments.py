import json
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentComments(FakeDocumentServer):

    def put(self,  url, body, header):
        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/documents/2225001/edit":
            return self.badResponse(404)

        jsonBody = json.loads(body)

        if "title" not in jsonBody:
            return self.badResponse(400)


        if jsonBody['title'] == "I Am a test":
            return self.badResponse(409)

        newResponse = self.goodResponse
        newResponse['Headers']['status'] = 204
        newResponse['Headers']['link'] = '<http://api.huddle.dev/files/folders/2227259>; rel="parent"'
        newResponse['Body'] = {}

        jsonData = json.loads(self.validDocument())
        jsonData['title'] = jsonBody['title']
        jsonData['description'] = jsonBody.get('description', "")

        self.goodResponse['Body'] = jsonData

        return newResponse

    def data(self):
        pass