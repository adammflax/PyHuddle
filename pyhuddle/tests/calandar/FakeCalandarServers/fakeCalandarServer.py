from pyhuddle.tests.workspace.FakeWorkSpaceServer.fakeWorkSpaceServer import FakeWorkspaceServer
from pyhuddle.tests.workspace.fakeWorkspacerServer import FakeAuthServer

__author__ = 'adam.flax'

class FakeCalandarServer(FakeWorkspaceServer):

    def get(self, url, header):
        if url == "http://api.huddle.test/entry":
            return FakeAuthServer().goodResponse

        if url == "http://api.huddle.dev/workspaces/1237967":
            return self.goodResponse

        if url != "http://api.huddle.dev/v2/calendar/workspaces/1237967":
            return self.badResponse("404")

        newResponse = self.goodResponse.copy()
        newResponse['Body'] = self.validCalandar()

        return newResponse

    def validCalandar(self):
        return """
      {
    "uri": "http://api.huddle.dev/v2/calendar/workspaces/2227254",
    "workspace": {
        "id": 2227254,
        "uri": "http://api.huddle.dev/workspaces/2227254",
        "displayName": "AcceptanceTest"
    },
    "events": [ {
        "status": "InProgress",
        "plannedStartDate": "Wed, 26 Jun 2013 00:00:00 GMT",
        "owner": {
            "id": 1237965,
            "uri": "http://api.huddle.dev/users/1237965",
            "displayName": "adam flax",
            "username": "adam.flax",
            "logoPath": "/images/logos/avatar.jpg",
            "email": "adam.flax@huddle.net"
        },
        "assignments": [ {
            "assignee": {
                "id": 1237965,
                "uri": "http://api.huddle.dev/users/1237965",
                "displayName": "adam flax",
                "username": "adam.flax",
                "logoPath": "/images/logos/avatar.jpg",
                "email": "adam.flax@huddle.net"
            },
            "assigner": {
                "id": 1237965,
                "uri": "http://api.huddle.dev/users/1237965",
                "displayName": "adam flax",
                "username": "adam.flax",
                "logoPath": "/images/logos/avatar.jpg",
                "email": "adam.flax@huddle.net"
            }
        } ],
        "createdDate": "Wed, 26 Jun 2013 12:43:43 GMT",
        "updatedDate": "Wed, 26 Jun 2013 12:43:43 GMT",
        "attachments": [ ],
        "comments": [ ],
        "workspaceSummary": {
            "id": 2227254,
            "uri": "http://api.huddle.dev/workspaces/2227254",
            "displayName": "AcceptanceTest"
        },
        "customFields": [ ],
        "id": 18269,
        "title": "Blow up London",
        "description": "",
        "uri": "http://api.huddle.dev/v2/calendar/tasks/18269"
    } ]
}
                """