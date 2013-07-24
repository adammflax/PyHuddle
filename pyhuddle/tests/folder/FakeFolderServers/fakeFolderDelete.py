from tests.folder.FakeFolderServers.fakeFolderServer import FakeFolderServer

__author__ = 'adam.flax'

class FakeFolderDelete(FakeFolderServer):

    def delete(self,  url, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/folders/2227259":
            return self.badResponse(404)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 204
        newResponse['Headers']['link'] = '<http://api.huddle.dev/files/folders/1371761>; rel="parent"'
        newResponse['Body'] = {}

        return newResponse