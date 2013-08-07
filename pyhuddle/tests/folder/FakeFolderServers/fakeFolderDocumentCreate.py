import json
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderServer import FakeFolderServer

__author__ = 'adam.flax'

class FakeFolderDocumentCreate(FakeFolderServer):

    def post(self,  url, body, header ):

        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/folders/2227259/documents":
            return self.badResponse(404)

        jsonBody = json.loads(body)

        if "title" not in jsonBody:
            return self.badResponse(400)

        if jsonBody['title'] == "features":
            return self.badResponse(409)

        jsonResponse = json.loads(self.validFolder())
        jsonResponse = jsonResponse['documents'][0]
        jsonResponse['title'] = jsonBody['title']
        jsonResponse['description'] = jsonBody['description']

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 201
        newResponse['Headers']['location'] = url
        newResponse['Body'] = json.dumps(jsonResponse)

        return newResponse

    def put(self, url, body, header):
        #we have other tests for uploading so we dont need to worry about this as much

        if url != "http://api.huddle.dev/files/documents/2227569/upload":
            return self.badResponse(404)

        return self.goodResponse