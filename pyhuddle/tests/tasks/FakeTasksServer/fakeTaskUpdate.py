import json
from tests.tasks.FakeTasksServer.fakeTaskServer import FakeTaskServer

__author__ = 'adam.flax'

class FakeTaskUpdate(FakeTaskServer):


    def put(self, url, body, header):
        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response

        if url != "IamAFakeUrl":
            return self.badResponse(404)

        jsonBodyData = json.loads(body)

        data = self.validTask()
        jsonData =  json.loads(data)

        jsonData['title'] = jsonBodyData['Title']
        jsonData['description'] = jsonBodyData['Description']

        newResponse = self.goodResponse
        newResponse['Headers']['status'] = 200
        newResponse['Body'] = jsonData

        return newResponse