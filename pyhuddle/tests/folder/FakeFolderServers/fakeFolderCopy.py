import json
from tests.folder.FakeFolderServers.fakeFolderServer import FakeFolderServer

__author__ = 'adam.flax'

class FakeFolderCopy(FakeFolderServer):

    def post(self,  url, body, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/folders/2227259/copy":
            return self.badResponse(404)

        jsonBody = json.loads(body)

        if "targetFolder" not in jsonBody:
            return self.badResponse(400)

        if "link" not in jsonBody['targetFolder']:
            return self.badResponse(400)

        if "href" not in jsonBody['targetFolder']['link'] or "rel" not in jsonBody['targetFolder']['link']:
            return self.badResponse(400)

        if jsonBody['targetFolder']['link']['rel'] != "self":
            return self.badResponse(400)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 201
        newResponse['Headers']['location'] = 'http://api.huddle.dev/files/folders/2227259'

        return newResponse