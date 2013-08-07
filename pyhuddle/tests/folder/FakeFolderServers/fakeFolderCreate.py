import json
from pyhuddle.tests.folder.FakeFolderServers.fakeFolderServer import FakeFolderServer

__author__ = 'adam.flax'

class FakeFolderCreate(FakeFolderServer):

    def post(self,  url, body, header ):

        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "http://api.huddle.dev/files/folders/2227259":
            return self.badResponse(404)

        jsonBody = json.loads(body)

        if "title" not in jsonBody:
            return self.badResponse(400)

        #our server already has a folder of this title
        if jsonBody['title'] == "dfgdg":
            return self.badResponse(409)

        jsonResponse = json.loads(self.validFolder())
        jsonResponse['title'] = jsonBody['title']
        jsonResponse['description'] = jsonBody.get('description', "")

        #we don't copy the dict so when we perform a get request on the new folder it has the data
        #of the new title and description
        newResponse = self.goodResponse
        newResponse['Headers']['status'] = 201
        newResponse['Headers']['location'] = url
        newResponse['Body'] = json.dumps(jsonResponse)

        return newResponse