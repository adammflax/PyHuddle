import json
from ..api import Api
from ..hyperlinkresource import HyperLinkResource
from ..nonhyperlinkresource import NonHyperLinkResource
from ..tasks.tasks import Task

__author__ = 'adam.flax'

class Calendar(Api):
    """
    Provides api methods for a calandar. This class requires a calandar link. Once it has this you can edit details about
    the calandar and its task. Meta data about this folder is stored iin the metaData attribute which is of type
    NonHyperlinkResource. To get the meta data call lazyGet() See the resource class for what you can do with this meta
    data. Please note this uses Huddles old api which means this api does not hav the useful link meta data
    For more details about calandars look at https://code.google.com/p/huddle-apis/wiki/SummaryCalendar
    """

    def __init__(self, client, calandarLink):
        Api.__init__(self, client, calandarLink)

        #override the base headers
        self._baseHeader = client.createBaseHeader().copy()
        self._baseHeader['Accept'] = "application/json"
        self._baseHeader['Content-type'] = "application/json"

    def refresh(self):
        return Calandar(self._client, self.selfLink)

    def lazyGet(self):
        """
        we want this to be a nonHyperLink Resource as the calandar + task api is different to the files 1
        """
        if self._metaData is None:
            self._metaData = NonHyperLinkResource(self._getRequest())

        return self._metaData

    def getTasks(self):
        """
        Returns all of the users tasks in the calandars. This is returned as a list of tasks

        example: getTasks()
        {api.task.Task object, api.task.Task  object, api.task.Task object}
        """
        tasks = []

        for task in self.lazyGet().jsonObj['events']:
            tasks.append(Task(self._client, self._config['API']['huddleTaskServer'] + str(task['id'])))

        return tasks

    def createTask(self, title, description=None, status="NotStarted", plannedStartDate=None, completedDate=None,
                   completedBy=None, updatedDate=None, createdDate=None, attachments=[]):
        """
        Creates a task on the given calandar. By default status is set to NotStarted. Note if you have any attachments
        you need to store them in a list. What you store in them is document objects.  e.g. [api.Document.Document,
        api.Document.Document,api.Document.Document]

        example createTask("I am a task", updateDate="2011-05-10T00:00:00Z")
        api.task.Task object
        """
        url = self.selfLink
        header = self._baseHeader.copy()

        body = {"Status" : status, "PlannedStartDate" : plannedStartDate, "CompletedDate" : completedDate,
                "CompletedBy" : completedBy, "CreatedDate" : createdDate, "UpdatedDate" : updatedDate,
                "Title" : title, "Description" : description}

        if attachments: #we have an attachment
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

        response = self._adapter.postRequest(url, header, jsonData)

        return Task(self._client, response['Headers']['location'])


