__author__ = 'adam.flax'
import json

class Resource(object):
    """
    A base object that is used by all huddle resources, e.g. documents folders workspaces
    This class was made so you always have helper methods for items such as grabbing links
    The deseralized json string can be accessed by the jsonObj variable
    This class can ever take a jsonstring which it will then deseralize as an input or it can take a json object
    """

    def __init__(self, jsonData):
        if isinstance(jsonData, str):
            self.jsonObj = json.loads(jsonData)
        else:
            self.jsonObj = jsonData

    def getTitle(self):
        """
        Returns the title of the Huddle resource

        example getTitle()
        "My Files"
        """
        return self.jsonObj['title']

    def getDescription(self):
        """
        Returns the description of the Huddle resource

        example: getDescription()
        "I am a descrription"
        """
        return self.jsonObj['description']
