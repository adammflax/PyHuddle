from httpadapter.adapter import Adapter
from api.huddleerrors import HandleCodeResponse

__author__ = 'adam.flax'

class HttpFakeAdapter(Adapter):

    def __init__(self, fakeServer):
        self.fakeServer = fakeServer
        self._huddleErrors = HandleCodeResponse()

    def getRequest(self, url, header):
        """
        implementation of a get request
        """
        response = self.fakeServer.get(url, header)

        self._huddleErrors.handleResponseError(response)

        return response

    def deleteRequest(self, url, header):
        """
        implementation of a delete request
        """
        response = self.fakeServer.delete(url, header)

        self._huddleErrors.handleResponseError(response)
        return response

    def postRequest(self, url, header, body):
        """
        implementation of a post request
        """
        response = self.fakeServer.post(url, body, header)

        self._huddleErrors.handleResponseError(response)
        return response


    def putRequest(self, url, header, body):
        """
        implementation of a PUT request
        """
        response = self.fakeServer.put(url, body, header)

        self._huddleErrors.handleResponseError(response)
        return response



