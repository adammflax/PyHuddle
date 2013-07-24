import json
from ..api import Api
from ..hyperlinkresource import HyperLinkResource

__author__ = 'adam.flax'

class User(Api):
    """
    Provides api methods for a user. This class requires a user link. Once it has this you can get information about
    the user. Meta data about this user is stored in the metaData attribute which is of type
    HyperlinkResource. To get the meta data call lazyGet() See the resource class for what you can do with this meta data.
    For more details about users look at https://code.google.com/p/huddle-apis/wiki/User
    """
    def __init__(self, client, userLink):
        Api.__init__(self, client, userLink)


    def getFriends(self, workspace=None):
        """
        Returns a list of all of the users friends. If you specify a workspace it will instead return a list of all
        the users friends in that workspace. This method returns a list of User objects. Unlike the api its self this
        method will NOT add you to the list, instead it will return every friend except for you

        example: getFriends()
        {api.user.User Object, api.user.User Object, api.user.User Object}

        Raises an AssertError if you have no friends =-(
        """


        url = self.lazyGet().getLink("friends")
        assert url is not None
        if workspace is not None: assert hasattr(workspace, "selfLink")

        if workspace is not None:
            workspaceID = workspace.selfLink.rsplit('/',1)
            url = self.lazyGet().getLink("friends") + "?workspace=" + workspaceID[1] #do we need the [1]

        response = self._adapter.getRequest(url, self._baseHeader)
        jsonObj = json.loads(response['Body'])

        friends = []

        for friend in jsonObj['users']:
            f = HyperLinkResource(friend)

            if f.selfLink != self.selfLink: #make sure you don't get appended on
                friends.append(User(self._client, f.selfLink))

        return friends