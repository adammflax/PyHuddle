import json
from tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentCopy(FakeDocumentServer):

    def post(self,  url, body, header):
        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/documents/2225001/copy":
            return self.badResponse(404, "not found!")

        jsonBody = json.loads(body)

        if "targetFolder" not in jsonBody:
            return self.badResponse(400, "missing body data targetFolder element")

        if "link" not in jsonBody['targetFolder']:
            return self.badResponse(400, "missing body data no link list in targetFolderElement")

        if "href" not in jsonBody['targetFolder']['link'] or "rel" not in jsonBody['targetFolder']['link']:
            return self.badResponse(400, "missing body data no href or rel found in link")

        if jsonBody['targetFolder']['link']['rel'] != "self":
            return self.badResponse(400, "missing body data rel link is not self")

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 201
        newResponse['Headers']['location'] = 'http://api.huddle.dev/files/documents/2225009'

        return newResponse

    def data(self):
        pass