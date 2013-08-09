from pyhuddle.tests.fakeServer import fakeServer
from pyhuddle.tests.workspace.fakeWorkspacerServer import FakeAuthServer


class FakeTaskServer(fakeServer):

    def __init__(self):
        fakeServer.__init__(self)
        self.goodResponse['Body'] = self.validTask()
        self.goodResponse['Headers']['Content-Type'] = "application/json"


    def get(self, url, header):
        if url == "http://api.huddle.test/entry":
            return FakeAuthServer().goodResponse

        if url != "IamAFakeUrl":
            return self.badResponse(404)

        return self.goodResponse

    def isRequestValid(self, url, header):
        if header['Authorization'] != "OAuth2 token":
            return self.badResponse(401)

        if header['Accept'] != "application/json":
            return self.badResponse(406)

        return True

    def validTask(self):
        return """{
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