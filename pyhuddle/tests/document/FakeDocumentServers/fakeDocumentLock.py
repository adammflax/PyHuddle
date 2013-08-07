import json
from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentLock(FakeDocumentServer):

    def post(self,  url, body, header):
        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/documents/2225001/lock":
            return self.badResponse(404)

        jsonBody = json.loads(body)

        if "lockIntent" not in jsonBody:
            return self.badResponse(400)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 201
        newResponse['Body'] = self.data()

        return newResponse

    def delete(self, url, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response

        if url !="http: //api.huddle.dev//documents/123/lock/delete":
            return self.badResponse(404, "not found!")

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['Status'] = 200
        newResponse['Headers']['link'] = '<http://api.huddle.dev/files/folders/2227259>; rel="parent"'
        newResponse['Body'] = {}

        return newResponse


    def data(self):
        return """
            {
                "links": [
                    {
                        "rel": "self",
                        "href": "http://api.huddle.dev//documents/123/lock"
                    },
                    {
                        "rel": "delete",
                        "href": "http: //api.huddle.dev//documents/123/lock/delete"
                    },
                    {
                        "rel": "parent",
                        "href": "http: //api.huddle.dev/documents/123"
                    }
                ],
                "lockIntent": "lockedForEdit"
            }"""