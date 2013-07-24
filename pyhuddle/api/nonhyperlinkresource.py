import json
from .resource import Resource

__author__ = 'adam.flax'

class NonHyperLinkResource(Resource):

    """
    wrapper resource object for calandars as they don't behave the same way as normal resources
    as its part of an old api
    """

    def __init__(self, jsonData):
        #resource has no links so we need to get selfLink by looking at uri
        Resource.__init__(self, jsonData)
        self.selfLink = self.jsonObj["uri"]

        assert self.selfLink is not None


