from pyhuddle.tests.fakeServer import fakeServer

__author__ = 'adam.flax'

class FakeFolderServer(fakeServer):

    def __init__(self):
        fakeServer.__init__(self)
        self.goodResponse['Body'] = self.validFolder()

    def validFolder(self):
        data = """{
    "owner": {
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
    },
    "folders": [ {
        "links": [ {
            "rel": "create-document",
            "href": "http://api.huddle.dev/files/folders/2227556/documents"
        }, {
            "rel": "create-folder",
            "href": "http://api.huddle.dev/files/folders/2227556"
        }, {
            "rel": "delete",
            "href": "http://api.huddle.dev/files/folders/2227556"
        }, {
            "rel": "self",
            "href": "http://api.huddle.dev/files/folders/2227556"
        }, {
            "rel": "permissions",
            "href": "http://api.huddle.dev/files/folders/2227556/permissions"
        }, {
            "rel": "workspace-summary",
            "href": "http://api.huddle.dev/workspaces/2227254"
        }, {
            "rel": "share",
            "href": "http://api.huddle.dev/files/folders/2227556/share"
        }, {
            "rel": "bulk-delete",
            "href": "http://api.huddle.dev/files/bulkprocess/delete/"
        }, {
            "rel": "bulk-move",
            "href": "http://api.huddle.dev/files/bulkprocess/move/"
        }, {
            "rel": "edit",
            "href": "http://api.huddle.dev/files/folders/2227556/edit"
        }, {
            "rel": "editPermissions",
            "href": "http://api.huddle.dev/files/folders/2227556/permissions"
        }, {
            "rel": "move",
            "href": "http://api.huddle.dev/files/folders/2227556/edit"
        }, {
            "rel": "copy",
            "href": "http://api.huddle.dev/files/folders/2227556/copy"
        }, {
            "rel": "parent",
            "href": "http://api.huddle.dev/files/folders/2227259"
        } ],
        "title": "dfgdg",
        "displayName": "dfgdg",
        "description": "dgdgdg",
        "updated": "Mon, 17 Jun 2013 15:50:01 GMT",
        "created": "Mon, 17 Jun 2013 15:50:01 GMT"
    } ],
    "documents": [ {
        "title": "features",
        "description": "",
        "links": [ {
            "rel": "self",
            "href": "http://api.huddle.dev/files/documents/2227569"
        }, {
            "rel": "version-history",
            "href": "http://api.huddle.dev/files/documents/2227569/versions"
        }, {
            "rel": "comments",
            "href": "http://api.huddle.dev/files/documents/2227569/comments",
            "count": "0"
        }, {
            "rel": "approvals",
            "href": "http://api.huddle.dev/files/documents/2227569/approvals"
        }, {
            "rel": "permissions",
            "href": "http://api.huddle.dev/files/folders/2227259/permissions"
        }, {
            "rel": "share",
            "href": "http://api.huddle.dev/files/documents/2227569/share"
        }, {
            "rel": "upload",
            "href": "http://api.huddle.dev/files/documents/2227569/upload"
        },{
            "rel": "audittrail",
            "href": "http://api.huddle.dev/files/documents/2227569/audittrail"
        }, {
            "rel": "printed",
            "href": "http://api.huddle.dev/files/documents/2227569/audittrail/printed"
        }, {
            "rel": "bulk-delete",
            "href": "http://api.huddle.dev/files/bulkprocess/delete/"
        }, {
            "rel": "preview",
            "href": "http://api.huddle.dev/files/documents/versions/225101/preview"
        }, {
            "rel": "alternate",
            "href": "huddle://files/documents/2227569"
        }, {
            "rel": "alternate",
            "href": "http://my.huddle.dev/workspaces/2227254/files/2227569",
            "type": "text/html"
        }, {
            "rel": "content",
            "href": "http://api.huddle.dev/files/documents/225101/content",
            "type": "text/plain",
            "title": "features.txt"
        }, {
            "rel": "parent",
            "href": "http://api.huddle.dev/files/folders/2227259",
            "title": "AcceptanceTest"
        }, {
            "rel": "edit",
            "href": "http://api.huddle.dev/files/documents/2227569/edit"
        }, {
            "rel": "create-version",
            "href": "http://api.huddle.dev/files/documents/2227569/version"
        }, {
            "rel": "lock",
            "href": "http://api.huddle.dev/files/documents/2227569/lock"
        }, {
            "rel": "delete",
            "href": "http://api.huddle.dev/files/documents/2227569"
        }, {
            "rel": "move",
            "href": "http://api.huddle.dev/files/documents/2227569/edit"
        }, {
            "rel": "copy",
            "href": "http://api.huddle.dev/files/documents/2227569/copy"
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
        "size": 296,
        "updated": "Mon, 17 Jun 2013 15:50:03 GMT",
        "created": "Mon, 17 Jun 2013 15:50:03 GMT",
        "processingStatus": "Complete",
        "views": 0,
        "workspace": {
            "title": "AcceptanceTest",
            "links": [ {
                "rel": "self",
                "href": "http://api.huddle.dev/workspaces/2227254"
            } ]
        }
    } ],
    "created": "Mon, 17 Jun 2013 14:51:17 GMT",
    "links": [ {
        "rel": "create-document",
        "href": "http://api.huddle.dev/files/folders/2227259/documents"
    }, {
        "rel": "create-folder",
        "href": "http://api.huddle.dev/files/folders/2227259"
    }, {
        "rel": "self",
        "href": "http://api.huddle.dev/files/folders/2227259"
    }, {
        "rel": "permissions",
        "href": "http://api.huddle.dev/files/folders/2227259/permissions"
    }, {
        "rel": "workspace-summary",
        "href": "http://api.huddle.dev/workspaces/2227254"
    }, {
        "rel": "share",
        "href": "http://api.huddle.dev/files/folders/2227259/share"
    }, {
        "rel": "bulk-delete",
        "href": "http://api.huddle.dev/files/bulkprocess/delete/"
    }, {
        "rel": "bulk-move",
        "href": "http://api.huddle.dev/files/bulkprocess/move/"
    }, {
        "rel": "editPermissions",
        "href": "http://api.huddle.dev/files/folders/2227259/permissions"
    },{
        "rel": "delete",
        "href": "http://api.huddle.dev/files/folders/2227259"
    },{
        "rel": "edit",
        "href": "http://api.huddle.dev/files/folders/2227259/edit"
    },{
        "rel": "move",
        "href": "http://api.huddle.dev/files/folders/2227259/move"
    },{
        "rel": "copy",
        "href": "http://api.huddle.dev/files/folders/2227259/copy"
    },{
        "rel": "parent",
        "href": "http://api.huddle.dev/files/folders/2227259"
    }],
    "title": "DocumentLibrary",
    "displayName": "AcceptanceTest",
    "updated": "Mon, 17 Jun 2013 14:51:17 GMT"
}
 """

        return data

