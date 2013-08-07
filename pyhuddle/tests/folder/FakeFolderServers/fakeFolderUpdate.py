import json
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderServer import FakeFolderServer

__author__ = 'adam.flax'

class FakeFolderUpdate(FakeFolderServer):

    def put(self,  url, body, header):

        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/folders/2227259/edit":
            return self.badResponse(404)

        jsonBody = json.loads(body)

        if "title" not in jsonBody:
            return self.badResponse(400)

        if jsonBody['title'] == "dfgdg":
            return self.badResponse(409)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 204
        newResponse['Headers']['link'] = '<http://api.huddle.dev/files/folders/2227259>; rel="parent"'
        newResponse['Body'] = {}

        return self.goodResponse