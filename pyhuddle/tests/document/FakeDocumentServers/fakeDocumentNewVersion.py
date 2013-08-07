import json
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentLock import FakeDocumentLock
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentNewVersion(FakeDocumentServer):

    def __init__(self):
        FakeDocumentServer.__init__(self)
        self.fakeDocumentLock = FakeDocumentLock()

    def post(self, url,body, header):
        if url == "http://api.huddle.dev/files/documents/2225001/lock":
             return self.fakeDocumentLock.post(url, body, header)
        elif url != "http://api.huddle.dev/files/documents/2225001/version":
            return self.badResponse(404, "not found")
        else:
            jsonBody = json.loads(body)

            if "title" not in jsonBody:
                return self.badResponse(400, "bad format no title found")

            if "extension" not in jsonBody:
                return self.badResponse(400, "bad format no extension found")

            newJsonData = json.loads(self.validDocument())
            newJsonData['title'] = jsonBody['title']
            newJsonData['description'] = jsonBody.get('description', "")
            newJsonData['extension'] = jsonBody['extension']

            newResponse = self.goodResponse
            newResponse['Headers']['status'] = 201
            newResponse['Body'] = json.dumps(newJsonData)

            return newResponse

    def delete(self, url, header):
        return self.fakeDocumentLock.delete(url, header)

    def put(self,  url, body, header):
        #we have other tests for uploading so we dont need to worry about this as much
        if url != "http://api.huddle.dev/files/documents/2225001/upload":
            return self.badResponse(404, "not found")

        return self.goodResponse

