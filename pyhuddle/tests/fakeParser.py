from configparser import ConfigParser

__author__ = 'adam.flax'

class FakeParser(object):

    def getParser(self):
        #set up the parser
        parser = ConfigParser()
        parser.add_section("OAUTH2")
        parser.add_section("OAUTH2ENDPOINT")
        parser.add_section("API")

        parser.set("OAUTH2", "redirectUri", "urn:fake:fk:fake:2.0:oob")
        parser.set("OAUTH2","clientID", "fakeClientID")
        parser.set("OAUTH2","tokenFileName", "fakeFile")

        parser.set("OAUTH2ENDPOINT", "huddleAuthServer", "http://login.huddle.test/")
        parser.set("OAUTH2ENDPOINT", "huddleAccessTokenServer", "http://login.huddle.test/token")

        parser.set("API", "accept", "application/vnd.huddle.data+json")
        parser.set("API", "huddleApiServer", "http://api.huddle.test/")
        parser.set("API", "huddleCalandarServer", "http://api.huddle.dev/v2/calendar/workspaces/")
        parser.set("API", "huddleTaskServer", "http://api.huddle.dev/v2/calendar/events/")

        return parser