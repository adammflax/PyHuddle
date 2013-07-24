from tests.folder.FakeFolderServers.fakeFolderServer import FakeFolderServer

__author__ = 'adam.flax'

class FakeFolderRestore(FakeFolderServer):

    def put(self,  url, header, body):
        response = self.isRequestWithBodyValid(url, body, header)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/folders/2227259/restore":
            return self.badResponse(404)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 204
        newResponse['Headers']['location'] = 'http://api.huddle.dev/files/folders/2227259'
        newResponse['Body'] = {}

        return newResponse