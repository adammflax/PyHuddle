import json
from pyhuddle.tests.calandar.FakeCalandarServers.fakeCalandarServer import FakeCalandarServer
from pyhuddle.tests.workspace.fakeWorkspacerServer import FakeAuthServer

__author__ = 'adam.flax'

class FakeCalandarTaskCreateServer(FakeCalandarServer):

    def get(self, url, header):
        if url == "http://api.huddle.test/entry":
            return FakeAuthServer().goodResponse

        if url != "http://api.huddle.dev/v2/calandar/events/18279":
            return self.badResponse("404")

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 200
        newResponse['Body'] = self.validTask()

        return newResponse

    def post(self, url,body, header):
        response = self.isRequestWithBodyValid(url, header, body)

        if response is not True: return response
        if url != "IAmAFakeUrl":
            return self.badResponse(404)

        jsonBody = json.loads(body)

        if "Title" not in jsonBody:
            return self.badResponse(400)

        if "Status" not in jsonBody:
            return self.badResponse(400)

        newResponse = self.goodResponse.copy()
        newResponse['Headers']['status'] = 201
        newResponse['Headers']['location'] = 'http://api.huddle.dev/v2/calandar/events/18279'
        newResponse['Body'] = self.validTask()

        return newResponse

    def isRequestWithBodyValid(self, url, header, body):
        if header['Authorization'] != "OAuth2 token":
            return self.badResponse(401)
        if header['Accept'] != "application/json":
            return self.badResponse(406)

        try:
            json.loads(body)
        except ValueError:
            return self.badResponse(400)

        return True

    def validTask(self):
        return """
     {
    "status": "NotStarted",
    "owner": {
        "id": 1237965,
        "uri": "http://api.huddle.dev/users/1237965",
        "displayName": "adam flax",
        "username": "adam.flax",
        "logoPath": "/images/logos/avatar.jpg",
        "email": "adam.flax@huddle.net"
    },
    "assignments": [ ],
    "createdDate": "Thu, 27 Jun 2013 07:55:58 GMT",
    "updatedDate": "Thu, 27 Jun 2013 07:55:58 GMT",
    "attachments": [ ],
    "comments": [ ],
    "workspaceSummary": {
        "id": 1371756,
        "uri": "http://api.huddle.dev/workspaces/1371756",
        "displayName": "foofoo"
    },
    "customFields": [ ],
    "id": 18279,
    "title": "foo",
    "description": "bar",
    "uri": "http://api.huddle.dev/v2/calandar/events/18279"
}
                """