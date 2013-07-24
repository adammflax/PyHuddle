import json
from ..api import Api
from ..hyperlinkresource import HyperLinkResource

__author__ = 'adam.flax'

class Comments(Api):

    def __init__(self, client, documentCommentLink):
        Api.__init__(self, client, documentCommentLink)

    def refresh(self):
        return Comments(self._client, self.selfLink)

    def getComments(self):
        """
        gets a list of all the different comments in a document's comments
        This is returned as a list of resources

        example: getComments()
        returns {Resource object, Resource Object, Resource Object}
        """
        comments = []

        for comment in self.lazyGet().jsonObj['comments']:
            f = HyperLinkResource(comment)
            comments.append(HyperLinkResource(comment))

        return comments

    def createComment(self, content, replyToID =None):
        """
        Adds a comment to documents comments. Comments have to be less 2049 characters in size

        example: createComment("I am content")
        returns {DocumentComments Object}

        Raises an AssertError if your content is bigger then 2049 characters
        Raises an AssertError if replyToID is not an int or None
        """
        assert len(content) < 2049
        assert isinstance(replyToID, int) or replyToID is None

        headers = self._baseHeader
        headers['Content-Type'] = "application/vnd.huddle.data+json"

        jsonData = json.dumps({"content" : content, "replytoid" : replyToID})

        response = self._adapter.postRequest(self.selfLink, headers, jsonData)
        return Comments(self._client, self.selfLink)

    def deleteComment(self, index):
        """
        Deletes a comment from the documents comments

        example deleteComment(0)
        returns {DocumentComments Object}

        Raises an AssertError if index is not an int
        Raises an AssertError if the comment does not have a deleteUrl
        """
        assert isinstance(index, int)

        comment = self.getComments()[index]
        deleteUrl = comment.getLink("delete")

        assert deleteUrl is not None

        headers = self._baseHeader

        response = self._adapter.deleteRequest(deleteUrl, headers)

        return Comments(self._client, self.selfLink)