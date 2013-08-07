from pyhuddle.tests.tasks.FakeTasksServer.fakeTaskServer import FakeTaskServer

class FakeTaskDelete(FakeTaskServer):


    def delete(self,  url, header):
        response = self.isRequestValid(url, header)

        if response is not True: return response

        if url != "IAmAFakeUrl":
            return self.badResponse(404)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 200
        newResponse['Body'] = {}

        return newResponse