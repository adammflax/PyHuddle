from pyhuddle.tests.document.FakeDocumentServers.fakeDocumentServer import FakeDocumentServer

__author__ = 'adam.flax'

class FakeDocumentDownload(FakeDocumentServer):

    def get(self,  url, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response


        #huddleClient will also call a get request so we need to prepare for that
        #also document will call get so we need to prepare for that
        if url == "http://api.huddle.test/entry" or url == "IAmAFakeUrl":
            return self.goodResponse


        if url != "http://api.huddle.dev/files/documents/224403/content":
            return self.badResponse(404, "not found!")

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['Content-Length'] = 400
        newResponse['Headers']['Content-Type'] = "text/plain"
        newResponse['Headers']['Content-Disposition'] = "attachment; filename=" + '""I Am a test.txt"'
        newResponse['Body'] = "I am the body content for this data!"

        return newResponse

    def data(self):
        pass