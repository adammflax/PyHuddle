from tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentRestore(FakeDocumentServer):

    def put(self,  url, body, header):
        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response


        if url != "IAmAFakeUrl/restore":
            return self.badResponse(404)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 204
        newResponse['Headers']['location'] = "http://api.huddle.dev/files/documents/2225001"
        newResponse['Body'] = {}

        return newResponse