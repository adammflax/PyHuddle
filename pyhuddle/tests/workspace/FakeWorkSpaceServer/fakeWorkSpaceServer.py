from tests.fakeServer import fakeServer

__author__ = 'adam.flax'

class FakeWorkspaceServer(fakeServer):

    def __init__(self):
        fakeServer.__init__(self)
        self.goodResponse['Body'] = self.validWorkspace()

    def validWorkspace(self):
        return  """

{
    "type": "shared",
    "links": [ {
        "rel": "self",
        "href": "http://api.huddle.dev/workspaces/1371756"
    }, {
        "rel": "documentLibrary",
        "href": "http://api.huddle.dev/files/folders/1371761"
    }, {
        "rel": "changes",
        "href": "http://api.huddle.dev/files/workspaces/1371756/changes"
    }, {
        "rel": "workspaceMembers",
        "href": "http://api.huddle.dev/v2/workspaces/1371756/members"
    }, {
        "rel": "permissions",
        "href": "http://api.huddle.dev/files/workspaces/1371756/permissions"
    } ],
    "title": "foofoo",
    "description": "",
    "settings": [ {
        "name": "CanSync",
        "value": "False"
    }, {
        "name": "IsManager",
        "value": "True"
    }, {
        "name": "Status",
        "value": "Active"
    } ]
}
                """