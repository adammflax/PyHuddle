from pyhuddle.tests.folder.FakeFolderServers.fakeFolderServer import FakeFolderServer

__author__ = 'adam.flax'

class FakeFolderMove(FakeFolderServer):

    def put(self,  url, body, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/folders/2227259/move":
            return self.badResponse(404)

        #we don't copy this so when we perform a get on the new folder we get the meta data we want
        newResponse = self.goodResponse
        newResponse['Headers']['status'] = 204
        newResponse['Headers']['link'] = '<http://api.huddle.dev/files/folders/2227259>; rel="parent"'
        newResponse['Body'] = body

        return newResponse