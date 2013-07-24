from tests.user.FakeUserServer.FakeUserServer import FakeUserServer


class FakeFriendServer(FakeUserServer):


    def get(self, url, header):

        if url == "http://api.huddle.test/entry" or url == "http://api.huddle.dev/users/1237965" :
            return self.goodResponse

        if url != "http://api.huddle.dev/users/1237965/friends":
            return self.badResponse(404)

        newResponse = self.goodResponse.copy()
        newResponse['Body'] = self.validFriends()

        return newResponse

    def validFriends(self):
        return""" {
                    "links": [ {
                        "rel": "self",
                        "href": "http://api.huddle.dev/users/1237965/friends"
                    } ],
                    "users": [ {
                        "links": [ {
                            "rel": "avatar",
                            "href": "http://api.huddle.dev/files/users/505853/avatar",
                            "type": "image/jpeg"
                        }, {
                            "rel": "alternate",
                            "href": "http://my.huddle.dev/user/ip.dev",
                            "type": "text/html"
                        }, {
                            "rel": "friends",
                            "href": "http://api.huddle.dev/users/505853/friends"
                        }, {
                            "rel": "self",
                            "href": "http://api.huddle.dev/users/505853"
                        }, {
                            "rel": "recommendations",
                            "href": "http://api.huddle.dev/files/documents/recommendations/505853"
                        } ],
                        "profile": {
                            "company": {
                                "name": "Huddle",
                                "links": [ ],
                                "role": "Desktop Developer"
                            },
                            "personal": {
                                "firstName": "Ian",
                                "surname": "Pender",
                                "displayName": "Ian Pender",
                                "aboutMe": ""
                            },
                            "contacts": [ {
                                "rel": "mail",
                                "value": "ian.pender@huddle.com"
                            }, {
                                "rel": "telephone",
                                "value": "333"
                            } ]
                        },
                        "internationalisation": {
                            "utcOffset": 0
                        }
                    }, {
                        "links": [ {
                            "rel": "avatar",
                            "href": "http://api.huddle.dev/files/users/1237965/avatar",
                            "type": "image/jpeg"
                        }, {
                            "rel": "alternate",
                            "href": "http://my.huddle.dev/user/adam.flax",
                            "type": "text/html"
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
                                "displayName": "adam flax",
                                "aboutMe": ""
                            },
                            "contacts": [ {
                                "rel": "mail",
                                "value": "adam.flax@huddle.net"
                            }, {
                                "rel": "telephone",
                                "value": "07500869458"
                            } ]
                        },
                        "internationalisation": {
                            "utcOffset": 0
                        }
                    } ]
                }
                """