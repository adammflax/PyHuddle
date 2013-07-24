from tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentDelete(FakeDocumentServer):

    def delete(self,  url, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/documents/2225001":
            return self.badResponse(404, "not found!")

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 200
        newResponse['Headers']['link'] = '<http://api.huddle.dev/files/folders/2227259>; rel="parent"'
        newResponse['Body'] = {}

        return newResponse