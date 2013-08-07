from pyhuddle.tests.fakeServer import fakeServer

__author__ = 'adam.flax'

class FakeUserServer(fakeServer):

    def __init__(self):
        fakeServer.__init__(self)
        self.goodResponse['Body'] = self.validUser()

    def validUser(self):
        return """{
                "links": [ {
                    "rel": "avatar",
                    "href": "http://api.huddle.dev/files/users/1237965/avatar",
                    "type": "image/jpeg"
                }, {
                    "rel": "alternate",
                    "href": "http://my.huddle.dev/user/adam.flax",
                    "type": "text/html"
                }, {
                    "rel": "approvals",
                    "href": "http://api.huddle.dev/files/users/1237965/approvals"
                }, {
                    "rel": "friends",
                    "href": "http://api.huddle.dev/users/1237965/friends"
                }, {
                    "rel": "self",
                    "href": "http://api.huddle.dev/users/1237965"
                }, {
                    "rel": "recommendations",
                    "href": "http://api.huddle.dev/files/documents/recommendations/1237965"
                } ],
                "profile": {
                    "company": {
                        "name": "huddle",
                        "links": [ ],
                        "role": ""
                    },
                    "personal": {
                        "firstName": "adam",
                        "surname": "flax",
                        "displayName": "adam flax"
                    },
                    "contacts": [ {
                        "rel": "mail",
                        "value": "adam.flax@huddle.net"
                    }, {
                        "rel": "telephone",
                        "value": "07500869458"
                    } ]
                },
                "membership": {
                    "workspaces": [ {
                        "type": "private",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/1237967"
                        }, {
                            "rel": "documentLibrary",
                            "href": "http://api.huddle.dev/files/folders/1237971"
                        }, {
                            "rel": "changes",
                            "href": "http://api.huddle.dev/files/workspaces/1237967/changes"
                        }, {
                            "rel": "workspaceMembers",
                            "href": "http://api.huddle.dev/v2/workspaces/1237967/members"
                        }, {
                            "rel": "permissions",
                            "href": "http://api.huddle.dev/files/workspaces/1237967/permissions"
                        } ],
                        "title": "My Files",
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
                    }, {
                        "type": "shared",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/1237974"
                        }, {
                            "rel": "documentLibrary",
                            "href": "http://api.huddle.dev/files/folders/1237979"
                        }, {
                            "rel": "changes",
                            "href": "http://api.huddle.dev/files/workspaces/1237974/changes"
                        }, {
                            "rel": "workspaceMembers",
                            "href": "http://api.huddle.dev/v2/workspaces/1237974/members"
                        }, {
                            "rel": "permissions",
                            "href": "http://api.huddle.dev/files/workspaces/1237974/permissions"
                        } ],
                        "title": "adam flax's workspace",
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
                    }, {
                        "type": "shared",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/1327034"
                        }, {
                            "rel": "documentLibrary",
                            "href": "http://api.huddle.dev/files/folders/1327039"
                        }, {
                            "rel": "changes",
                            "href": "http://api.huddle.dev/files/workspaces/1327034/changes"
                        }, {
                            "rel": "workspaceMembers",
                            "href": "http://api.huddle.dev/v2/workspaces/1327034/members"
                        }, {
                            "rel": "permissions",
                            "href": "http://api.huddle.dev/files/workspaces/1327034/permissions"
                        } ],
                        "title": "ProviderShowOff",
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
                    }, {
                        "type": "shared",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/1371735"
                        }, {
                            "rel": "documentLibrary",
                            "href": "http://api.huddle.dev/files/folders/1371740"
                        }, {
                            "rel": "changes",
                            "href": "http://api.huddle.dev/files/workspaces/1371735/changes"
                        }, {
                            "rel": "workspaceMembers",
                            "href": "http://api.huddle.dev/v2/workspaces/1371735/members"
                        }, {
                            "rel": "permissions",
                            "href": "http://api.huddle.dev/files/workspaces/1371735/permissions"
                        } ],
                        "title": "foo",
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
                    }, {
                        "type": "shared",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/1371742"
                        }, {
                            "rel": "documentLibrary",
                            "href": "http://api.huddle.dev/files/folders/1371747"
                        }, {
                            "rel": "changes",
                            "href": "http://api.huddle.dev/files/workspaces/1371742/changes"
                        }, {
                            "rel": "workspaceMembers",
                            "href": "http://api.huddle.dev/v2/workspaces/1371742/members"
                        }, {
                            "rel": "permissions",
                            "href": "http://api.huddle.dev/files/workspaces/1371742/permissions"
                        } ],
                        "title": "bar",
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
                    }, {
                        "type": "shared",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/1371749"
                        }, {
                            "rel": "documentLibrary",
                            "href": "http://api.huddle.dev/files/folders/1371754"
                        }, {
                            "rel": "changes",
                            "href": "http://api.huddle.dev/files/workspaces/1371749/changes"
                        }, {
                            "rel": "workspaceMembers",
                            "href": "http://api.huddle.dev/v2/workspaces/1371749/members"
                        }, {
                            "rel": "permissions",
                            "href": "http://api.huddle.dev/files/workspaces/1371749/permissions"
                        } ],
                        "title": "baz",
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
                    }, {
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
                    }, {
                        "type": "shared",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/2227254"
                        }, {
                            "rel": "documentLibrary",
                            "href": "http://api.huddle.dev/files/folders/2227259"
                        }, {
                            "rel": "changes",
                            "href": "http://api.huddle.dev/files/workspaces/2227254/changes"
                        }, {
                            "rel": "workspaceMembers",
                            "href": "http://api.huddle.dev/v2/workspaces/2227254/members"
                        }, {
                            "rel": "permissions",
                            "href": "http://api.huddle.dev/files/workspaces/2227254/permissions"
                        } ],
                        "title": "AcceptanceTest",
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
                    } ]
                },
                "internationalisation": {
                    "timeZone": "Europe/London",
                    "utcOffset": 60
                }
            }
            """