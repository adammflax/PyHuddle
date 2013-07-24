from .resource import Resource

__author__ = 'adam.flax'
import json

class HyperLinkResource(Resource):
    """
    90% of huddles api will use this. Only the tasks and calandar api will not as they are structured differently as they are old
    The difference between this and the resource object is that this has all the methods for the links[] part of the json object
    something the tasks and calandar api does not have
    """

    def __init__(self, jsonData):
        Resource.__init__(self, jsonData)
        self.selfLink = self.getLink("self")

        #in order for restore to work a resource needs to know about all of its sub deleted resources
        self.graveyard = []

        assert self.selfLink is not None

    def getLink(self, rel):
        """
        returns the href of a link with whatever rel you specify in the parameter
        this method will return None if it can't find the link you specified

        >>>getLink("self")
        www.my.huddle.net/foo/bar/12345
        """

        for link in self.jsonObj['links']:
            if link.get('rel') == rel:
                return link.get('href')

        return None

    def getLinkIndex(self, rel):
        """
        In a huddle resource, in the json links are stored in 1 big list. This method will return where in the list
        a given link is by specifying its rel

        >>>getLinkIndex("self")
        3

        If it can't find the link in the index this method returns -1
        """
        for i, link in enumerate(self.jsonObj['links']):
            if link.get('rel') == rel:
                return i

        return -1
