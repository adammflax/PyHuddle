from tests.fakeServer import fakeServer

__author__ = 'adam.flax'

class FakeDocumentServer(fakeServer):

    def __init__(self):
        fakeServer.__init__(self)
        self.goodResponse['Body'] = self.validDocument()

    def validDocument(self):
        data = """{
                    "title": "I Am a test",
                    "description": "",
                    "links": [ {
                        "rel": "self",
                        "href": "http://api.huddle.dev/files/documents/2225001"
                    }, {
                        "rel": "version-history",
                        "href": "http://api.huddle.dev/files/documents/2225001/versions"
                    }, {
                        "rel": "comments",
                        "href": "http://api.huddle.dev/files/documents/2225001/comments",
                        "count": "1"
                    }, {
                        "rel": "approvals",
                        "href": "http://api.huddle.dev/files/documents/2225001/approvals"
                    }, {
                        "rel": "permissions",
                        "href": "http://api.huddle.dev/files/folders/1371761/permissions"
                    }, {
                        "rel": "share",
                        "href": "http://api.huddle.dev/files/documents/2225001/share"
                    }, {
                        "rel": "audittrail",
                        "href": "http://api.huddle.dev/files/documents/2225001/audittrail"
                    }, {
                        "rel": "printed",
                        "href": "http://api.huddle.dev/files/documents/2225001/audittrail/printed"
                    }, {
                        "rel": "bulk-delete",
                        "href": "http://api.huddle.dev/files/bulkprocess/delete/"
                    }, {
                        "rel": "preview",
                        "href": "http://api.huddle.dev/files/documents/versions/224403/preview"
                    }, {
                        "rel": "alternate",
                        "href": "huddle://files/documents/2225001"
                    }, {
                        "rel": "alternate",
                        "href": "http://my.huddle.dev/workspaces/1371756/files/2225001",
                        "type": "text/html"
                    }, {
                        "rel": "content",
                        "href": "http://api.huddle.dev/files/documents/224403/content",
                        "type": "text/plain",
                        "title": "I Am a test.txt"
                    }, {
                        "rel": "parent",
                        "href": "http://api.huddle.dev/files/folders/1371761",
                        "title": "foofoo"
                    }, {
                        "rel": "edit",
                        "href": "http://api.huddle.dev/files/documents/2225001/edit"
                    }, {
                        "rel": "create-version",
                        "href": "http://api.huddle.dev/files/documents/2225001/version"
                    }, {
                        "rel": "lock",
                        "href": "http://api.huddle.dev/files/documents/2225001/lock"
                    }, {
                        "rel": "upload",
                        "href": "http://api.huddle.dev/files/documents/2225001/upload"
                    },{
                        "rel": "delete",
                        "href": "http://api.huddle.dev/files/documents/2225001"
                    }, {
                        "rel": "move",
                        "href": "http://api.huddle.dev/files/documents/2225001/edit"
                    }, {
                        "rel": "copy",
                        "href": "http://api.huddle.dev/files/documents/2225001/copy"
                    } ],
                    "actors": [ {
                        "name": "adam flax",
                        "email": "adam.flax@huddle.net",
                        "rel": "owner",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/users/1237965"
                        }, {
                            "rel": "avatar",
                            "href": "http://api.huddle.dev/files/users/1237965/avatar",
                            "type": "image/jpeg"
                        }, {
                            "rel": "alternate",
                            "href": "http://my.huddle.dev/user/adam.flax",
                            "type": "text/html"
                        } ]
                    }, {
                        "name": "adam flax",
                        "email": "adam.flax@huddle.net",
                        "rel": "updated-by",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/users/1237965"
                        }, {
                            "rel": "avatar",
                            "href": "http://api.huddle.dev/files/users/1237965/avatar",
                            "type": "image/jpeg"
                        }, {
                            "rel": "alternate",
                            "href": "http://my.huddle.dev/user/adam.flax",
                            "type": "text/html"
                        } ]
                    } ],
                    "version": 1,
                    "size": 46,
                    "updated": "Mon, 17 Jun 2013 09:20:12 GMT",
                    "created": "Mon, 17 Jun 2013 09:20:12 GMT",
                    "processingStatus": "Complete",
                    "views": 2,
                    "workspace": {
                        "title": "foofoo",
                        "links": [ {
                            "rel": "self",
                            "href": "http://api.huddle.dev/workspaces/1371756"
                        } ]
                    }
                }
     """

        return data


