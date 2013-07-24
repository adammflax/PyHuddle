import re
from .hyperlinkresource import HyperLinkResource
from .user.user import User
from .files.files import WorkSpace

__author__ = 'adam.flax'
class HuddleClient(object):

    def __init__(self, token, adapter, config):
        self.token = token
        self.adapter = adapter
        self.config = config

        if not hasattr(self.adapter, "postRequest"): raise TypeError("Your adapter does not have a post method!")
        if not hasattr(self.adapter, "putRequest"): raise TypeError("Your adapter does not have a put method!")
        if not hasattr(self.adapter, "getRequest"): raise TypeError("Your adapter does not have a get method!")
        if not hasattr(self.adapter, "deleteRequest"): raise TypeError("Your adapter does not have a delete method!")

        self._metaData = None
        self.user = User(self, self.lazyGet().selfLink)

    def lazyGet(self):
        if self._metaData is None:
            #lets hit entry
            url = self.config['API']['huddleApiServer'] + "entry"
            header = self.createBaseHeader()
            body = self.adapter.getRequest(url, header)['Body']
            self._metaData = HyperLinkResource(body)

        return self._metaData

    def getWorkSpaces(self):
        """
        Returns all a users workspaces. This is returned as a list of resources

        >>>getWorkSpaces()
        {<api.resource.Resource object>, <api.resource.Resource object>, <api.resource.Resource object>}

        >>>getWorkSpaces[0]
        <api.resource.Resource object> : returns the first workspace in the list
        """
        workspaces = []

        try:
            for workspace in self.lazyGet().jsonObj['membership']['workspaces']:
                ws = HyperLinkResource(workspace)
                workspaces.append(WorkSpace(self, ws.selfLink))
        except KeyError:
            return {}

        return workspaces

    def createBaseHeader(self):
        """
        Creates the base headers used in all requests for instance the authorization header, the Accept header etc

        >>>createBaseHeader()
        {"Authorization" : "OAuth2 IAMACCESSTOKENIAMA", "Accept" : "application/vnd.huddle.data/json"}
        """

        header = {"Authorization": "OAuth2 " + self.token.getAccessToken().getAccessToken(),
                  'Accept': self.config['API']['accept']}

        return header

    #def getIsGoodResponse(self, response):
        #return True if floor(int(response['Headers']['status']) / 100) == 2 else False

    def getUrlFromHeaderLink(self, link):
        m = re.search('[^<][^>]*', link)

        return m.group(0)

