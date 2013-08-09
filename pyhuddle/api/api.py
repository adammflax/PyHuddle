from pyhuddle.api.resource import HyperLinkResource

__author__ = 'adam.flax'

class Api(object):
    """
    The class that all api classes implement
    """

    def __init__(self, client, link):
        self._baseHeader = client.createBaseHeader()
        self._token = client.token
        self._adapter = client.adapter
        self._config = client.config
        self._client = client
        self.selfLink = link
        self._metaData = None

        if not hasattr(self._adapter, "postRequest"): raise TypeError("Your adapter does not have a post method!")
        if not hasattr(self._adapter, "putRequest"): raise TypeError("Your adapter does not have a put method!")
        if not hasattr(self._adapter, "getRequest"): raise TypeError("Your adapter does not have a get method!")
        if not hasattr(self._adapter, "deleteRequest"): raise TypeError("Your adapter does not have a delete method!")
        if not hasattr(self._client, "getUrlFromHeaderLink"): raise TypeError("Your client object does not "
                                                                             "have a getUrlFromHeaderLink attribute")
        assert self.selfLink is not None

    @property
    def metaData(self):
        """
        We do not want to perform a GET request about the object until we need to. As a lot of objects can get created
        when we perform some methods like getFolders and you may not need them all. For this reason when you want to get
        metaData about the object call this method which will. The apis that don't use hyperlinkResource override
        this method to make sure they implement the right resource object.
        """
        if self._metaData is None:
            self._metaData = HyperLinkResource(self._getRequest())

        return self._metaData

    def _getRequest(self):
        """
        Performs a GET request to that objects selfLink and returns the body of the request as a string in utf-8 format
        """
        body = self._adapter.getRequest(self.selfLink, self._baseHeader)['Body']
        return body


