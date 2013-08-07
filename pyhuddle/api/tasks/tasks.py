import json
from ..api import Api
from ..hyperlink_resource import HyperLinkResource
from ..non_hyperlink_resource import NonHyperLinkResource

__author__ = 'adam.flax'

class Task(Api):

    """
    Provides api methods for a task. This class requires a task link. Once it has this you can edit details about
    the task. Meta data about this task is stored in the metaData attribute which is of type
    NonHyperlinkResource. To get the meta data call lazyGet() See the resource class for what you can do with this meta
    data. Please note this uses Huddles old api which means this api does not have the useful link meta data
    For more details about tasks look at https://code.google.com/p/huddle-apis/wiki/Task
    """
    def __init__(self, client, taskUri):
        Api.__init__(self, client, taskUri)

        #override the base headers
        self._baseHeader = client.createBaseHeader().copy()
        self._baseHeader['Accept'] = "application/json"
        self._baseHeader['Content-type'] = "application/json"

    def refresh(self):
        return Task(self._client, self.selfLink)

    def lazyGet(self):
        """
        we want this to be a nonHyperLink Resource as the calandar + task api is different to the files 1
        """
        if self._metaData is None:
            self._metaData = NonHyperLinkResource(self._getRequest())

        return self._metaData

    def delete(self):
        """
        Deletes the given the task. Please note that the task is part of the old api. There is no way to restore a task
        once it has ben deleted. For this reason there is no graveyard object on the task api. The method will also
        return None as we get no response back and  as a task can not be restored we reach a dead end here so there is
        no point returning anything.

        example delete()
        None
        """
        url = self.selfLink
        header = self._baseHeader.copy()

        self._adapter.deleteRequest(url, header)

        #this makes me feel dirty
        return None

    def edit(self, title=None, description=None, status=None, plannedStartDate=None, completedDate=None,
                   completedBy=None, updatedDate=None, createdDate=None, attachments=[]):
        """
        edits the task. Note if you have any attachments you need to store them in a list.
        What you store in them is document objects.  e.g. [api.Document.Document, api.Document.Document]

        example editTask(title="I am a task")
        api.task.Task object
        """
        url = self.selfLink
        header = self._baseHeader.copy()

        body = {"Status" : status, "PlannedStartDate" : plannedStartDate, "CompletedDate" : completedDate,
                "CompletedBy" : completedBy, "CreatedDate" : createdDate, "UpdatedDate" : updatedDate,
                "Title" : title, "Description" : description}

        if len(attachments) > 0: #we have an attachment
            attachmentsTaskFormat = []

            for attachment in attachments:
                id = attachment.selfLink.rsplit('/',1)[1]
                uri = attachment.lazyGet().getLink("download")
                title = attachment.lazyGet().getTitle()
                description = attachment.lazyGet().getDescription()
                workSpace = HyperLinkResource(attachment.lazyGet.jsonObj['workspace'])
                workSpaceID = workSpace.selfLink.rsplit('/',1)[1]
                attachmentsTaskFormat.append({
                                                "id": id,
                                                "url": uri,
                                                "title": title,
                                                "description": description,
                                                "workspaceid" : workSpaceID,
                                                "attachedObjectInfoId": id
                                            })

            body['attachments': attachmentsTaskFormat]

        jsonData = json.dumps(body)

        response = self._adapter.putRequest(url, header, jsonData)

        return Task(self._client, self.selfLink)

    def addComment(self, text):
        """
        Adds a comment to this task this is another dead end like delete so we are returning None.
        this may seem strange as other comments return dataas you would expect to.
        However the comment api for tasks is different to that of files api

        example(addComment("I am a comment rawr")
        None
        """
        url = self.selfLink
        header = self._baseHeader.copy()

        body = {"Text" : text}

        jsonData = json.dumps(body)

        response = self._adapter.postRequest(url, header, jsonData)

        return None