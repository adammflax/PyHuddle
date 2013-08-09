import json
from pyhuddle.api.api import Api
from pyhuddle.api.create_multipart_form_request import MultiPartFormRequest
from pyhuddle.api.huddle_errors import HuddleConflictError
from pyhuddle.api.resource import HyperLinkResource
from pyhuddle.calandar.calandar import Calendar
from pyhuddle.comments.comments import Comments


__author__ = 'adam.flax'

class Document(Api):
    """
    Provides api methods for a document. This class requires a document link. Once it has this you can get information
    about the document. Meta data about this document is stored in the metaData attribute which is of type
    HyperlinkResource. To get the meta data call lazyGet() See the resource class for what you can do with this meta data.
    For more details about documents look at https://code.google.com/p/huddle-apis/wiki/Document
    """
    def __init__(self, client, documentLink):
        Api.__init__(self, client, documentLink)

    def refresh(self):
        return Document(self._client, self.selfLink)

    def delete(self):
        """
        Used to delete the document.  This method will return a folder object of the parent folder that this document
        resided in. Once the document has been deleted it will be added to this documents graveyard. This graveyard is
        used to restore the deleted document. If you delete this document it will set metadata.deleted to
        true. This will stop you doing any method except restore.

        example: delete()
        api.folder.Folder object

        Raises an AssertError if the this document doesn't have a delete link
        """
        documentUrl = self.metaData.getLink("delete")
        assert documentUrl is not None

        response = self._adapter.deleteRequest(documentUrl, self._baseHeader)
        self.metaData.graveyard.append(self.metaData)

        return Folder(self._client, self._client.getUrlFromHeaderLink(response['Headers']['link']))

    def restore(self):
        """
        Restores the document from this objects graveyard. If the document is deleted and not in the graveyard there
        is no way to restore the folder without knowing the full uri of the deleted folders restore link.
        Once the document has been restored that document will be removed from the graveyard.
        This method will return the document object of the restoredDocument

         example: restore()
        restores the folder on the the graveyard at index 0
        """
        documentUrl = self.metaData.graveyard[0].selfLink + "/restore"
        response = self._adapter.putRequest(documentUrl, self._baseHeader, "{}")
        self.metaData.graveyard.pop()

        return Document(self._client, response['Headers']['location'])

    def update(self, title=None, description = None):
        """
        Updates the meta data about this document. This method returns the document object of the updated document.
        This method allows you to edit the title and description of the document, if you leave 1 argument as optional
        it won't update that argument

        example: update("I am an optional title", "I am an optional description")
        api.document.Document Object

        Raises an AssertError if this document does not have an edit link
        """
        jsonData = self.metaData.jsonObj
        header = self._baseHeader.copy()

        header['Content-type'] = "application/vnd.huddle.data+json"
        url = self.metaData.getLink("edit")
        assert url is not None

        if title is not None: jsonData['title'] = title
        if description is not None: jsonData['description'] = description

        response = self._adapter.putRequest(url, header, json.dumps(jsonData))

        return Document(self._client, self._client.getUrlFromHeaderLink(response['Headers']['link']))

    def copyTo(self, folder):
        """
        Copies this document to target folder. This method returns a Document Object of the new copied document.

        example: copyTo(Folder)
        api.document.Document Object

        Raises an AssertError if this document does not have a copy link
        Raises an AssertError if the folder parameter does not act like a folder
        """
        copyUrl = self.metaData.getLink("copy")

        if not hasattr(folder, "metaData"): raise TypeError("Your newFolder does not have a metaData property")
        assert getattr(folder, "selfLink")
        assert copyUrl is not None

        header = self._baseHeader.copy()
        header['Content-type'] = "application/vnd.huddle.data+json"
        body = '{ "targetFolder":{ "link":{ "rel": "self", "href": "' + folder.selfLink + '" } } }'

        response = self._adapter.postRequest(copyUrl, header, body)

        return Document(self._client, response['Headers']['location'])

    def createNewVersion(self, file, title=None, description =None, versionNote = None):
        """
        Creates a new version of the document. While you are uploading the new version of the document the document is
        locked. When you create a new version of the document you can specify the ability to alter meta data such as
        the title, description and a note about why you are uploading this new version. This method returns a Document
        object of the new version of the document. This meta data may be different then a normal document as it may not
        of finished uploading the new version. Unlike other api methods this method will handle HuddleConflictErrors
        so make sure your httpAdapter throws these if you get a 409 response

        example: createNewVersion(file)
        api.document.Document Object

        Raises an AssertError if we cannot find a create-version link
        Raises an AssertError if it cannot find the upload url of the document
        """
        newVersionUrl = self.metaData.getLink("create-version")
        assert newVersionUrl is not None

        uploadFile = MultiPartFormRequest(file)

        header = self._baseHeader.copy()
        header['Content-type'] = "application/vnd.huddle.data+json"
        body = json.dumps({"title" : title, "description" : description, "versionNote" : versionNote, "extension" : uploadFile.extension})

        #create a lock
        lockResponse = self.__createLock()

        response = self._adapter.postRequest(newVersionUrl, header, body)

        r = HyperLinkResource(response['Body'])
        #now that we have a good response get the urls for the next part
        uploadUrl = r.getLink("upload")
        selfUrl = r.selfLink
        assert uploadUrl is not None

        #create the muti_form_data for the body
        boundary = uploadFile.create_boundary_string()
        header['Content-Type'] = "mutipart/form-data; boundary=" + boundary
        body = uploadFile.encode_mutipart_form_data(boundary)

        try:
            response = self._adapter.putRequest(uploadUrl, header, body)
        except HuddleConflictError:
            print("we couldn't upload the document as it has been locked by someone else")
        finally:
            self.__deleteLock(HyperLinkResource(lockResponse['Body']).getLink("delete"))

        return Document(self._client, selfUrl)

    def __createLock(self):
        """
        Puts a lock on the document. You should never need to call this method as it is called by the methods that need
        to lock content. This method returns the httprequest response of the request to lock

        example: __createLock
        {Headers : headerContent, Body: BodyContent}

        Raises an AssertError if we cannot find a lock link
        """
        lockUrl = self.metaData.getLink("lock")
        assert lockUrl is not None

        lockBody = json.dumps({"lockIntent" : "lockedForEdit"})
        header = self._baseHeader.copy()
        header['Content-type'] = "application/vnd.huddle.data+json"
        lockResponse = self._adapter.postRequest(lockUrl, header, lockBody)

        return lockResponse

    def __deleteLock(self, url):
        """
        Unlocks a lock on the document. To unlock the document you need to specify the locks delete link. You should never
        need to call this method as it is called by the methods that need to unlock content. This method returns
        the httprequest response of the request to lock

        example: __deleteLock
        {Headers : headerContent, Body :{}}
        """
        response = self._adapter.deleteRequest(url, self._baseHeader)
        return response

    def download(self):
        """
        Provides data needed to recreate the file for download. This method returns a dictionary of
        {"filename" : name + extension, "mime" : mimeType, "binary" : content of the document

        >>download
        {test.txt, text/plain, "I am the content of this text file"}

        Raises an AssertError if it cannot get the content link from the document
        """
        #the link has some meta data in it that we need to get a hold of so we cant use metaData.getLink()
        data = None

        for link in self.metaData.jsonObj['links']:
            if link.get('rel') == "content":
                data = link

        assert data is not None

        response = self._adapter.getRequest(data['href'], self._baseHeader)
        return {"filename": data['title'], "mime": data['type'], "binary": response['Body'] }


    def moveTo(self, folder):
        """
        Moves this document to another folder. This method returns a document object of the newly moved document

        >>moveTo(Folder>
        api.document.Document object

        Raises an AssertError if it does not have a move link
        Raises an AssertError if the folder object you specify does not act like a folder
        Raises an AssertError if we cannot find a parentLink
        """
        parent = self.metaData.getLinkIndex('parent')
        moveUri = self.metaData.getLink("move")

        assert parent != -1
        assert moveUri is not None
        if not hasattr(folder, "metaData"): raise TypeError("Your newFolder does not have a metaData property")
        assert hasattr(folder, "selfLink")

        header = self._baseHeader.copy()
        header['Content-type'] = "application/vnd.huddle.data+json"
        jsonData = self.metaData.jsonObj
        jsonData['links'][parent] =  {'href' : folder.selfLink, 'rel' : 'parent'}
        response = self._adapter.putRequest(moveUri, header, json.dumps(jsonData))

        return Document(self._client, self._client.getUrlFromHeaderLink(response['Headers']['link']))

    def versionHistory(self):
        """
        grabs the version history of the content. This is returned as a dictionary

        >>versionHistory(Folder>
        {really long json data in here} https://code.google.com/p/huddle-apis/wiki/VersionHistory for how it should
        look

        Raises an AssertError if it does not have a version-history link
        """
        url = self.metaData().getLink("version-history")
        assert url is not None

        header = self._baseHeader.copy()
        response = self._adapter.getRequest(url, header)

        return json.loads(response['Body'])

    def getComments(self):
        url = self.metaData().getLink("comments")
        assert url is not None

        return Comments(self._client, url)


class Folder(Api):
    """
    Provides api methods for a folder. This clas requires a folder link. Once it has this you can edit details about
    the folder and its sub folders. Meta data about this folder is stored in the metaData attribute which is of type
    HyperlinkResource. To get the meta data call lazyGet(). See the resource class for what you can do with this meta data.
    For more details about Folders look at https://code.google.com/p/huddle-apis/wiki/Folder
    """

    def __init__(self, client, parentFolderLink):
        Api.__init__(self, client, parentFolderLink)

    def refresh(self):
        return Folder(self._client, self.selfLink)

    def getFolders(self):
        """
        Returns all of the users sub folders in the folder. This is returned as a list of folders

        example: getFolders()
        {api.folder.Folder object, api.folder.Folder object, api.folder.Folder object}
        """

        folders = []

        for folder in self.metaData.jsonObj['folders']:
            f = HyperLinkResource(folder)
            folders.append(Folder(self._client, f.selfLink))

        return folders

    def getDocuments(self):
        """
        Returns all of the users documents in the current directory. This is returned as a list of documents

        example: getDocuments()
        {api.document.Document object, api.document.Document object, api.document.Document object}
        """
        documents = []

        for document in self.metaData.jsonObj['documents']:
            d = HyperLinkResource(document)
            documents.append(Document(self._client, d.selfLink))

        return documents


    def createDocument(self, file, description="", index=None):
        """
        Creates a document in the specified folder. If you do not specify an index it creates one in the parent directory

        example: createDocument(pathToDocument, "descriptionOptional")
        api.document.Document object

        Raises an AssertError if we cannot find a create-document url
        Raises an AssertError if we cannot find a uploadUrl
        Raises an AssertError if the index you provide is not of subtype int
        """

        assert isinstance(index, int) or index is None
        header = self._baseHeader.copy().copy()
        header['Content-Type'] = "application/vnd.huddle.data+json"
        uploadFile = MultiPartFormRequest(file)

        skeletonDocument= {"title" : uploadFile.title, "description" : description, "extension" : uploadFile.extension}
        jsonString = json.dumps(skeletonDocument)

        try:
            if index is None:
                url = self.metaData.getLink("create-document")
            else:
                url = self.getFolders()[index].metaData.getLink("create-document")

            assert url is not None

            response = self._adapter.postRequest(url, header, jsonString)

            uploadUrl = HyperLinkResource(response['Body']).getLink("upload")
            selfUrl = HyperLinkResource(response['Body']).selfLink
            assert uploadUrl is not None

            boundary = uploadFile.create_boundary_string()
            header['Content-Type'] = "mutipart/form-data; boundary=" + boundary
            body = uploadFile.encode_mutipart_form_data(boundary)
            header['Content-Length'] = len(body)

            response = self._adapter.putRequest(uploadUrl, header, body)

            return Document(self._client, selfUrl)
        except IndexError:
            print("the index: " + index + " does not exist in the list of folder numbers we have")

    def createFolder(self, title, description="", index=None):
        """
        creates a sub folder in the specififed directory. The index paramater is optional
        If you do not specify index it will create the sub folder in the parent directory.
        If everything goes right this method will return a folder object of the new folder

        example: createFolder("foo", "bar")
        creates a folder with the title foo and the description bar

        example: createFolder("foo", 2)
        creates a sub folder in the sub folder at index 2 with the title foo

        Raises a assert error if index is not of subtype int
        """
        assert isinstance(index, int) or index is None

        try:
            if index is None:
                url = self.metaData.getLink("create-folder")
            else:
                url = self.getFolders()[index].getLink("create-folder")

            header = self._baseHeader.copy()
            header['Content-Type'] = "application/vnd.huddle.data+json"

            skeletonFolder = {"title" : title, "description" : description}
            jsonString = json.dumps(skeletonFolder)
            response = self._adapter.postRequest(url, header, jsonString)

            return Folder(self._client, response['Headers']['location'])
        except IndexError:
            print("the index: " + index + " does not exist in the list of folder numbers we have")

    def updateFolder(self, title=None, description=None, index = None):
        """
        updated the meta data of the specified folde. If you do not specify index it will update the parent directory.
        This method will return a Folder object of the updated folder

        example: createFolder("foo", "bar")
        updates the parent folder with the title foo and the description bar

        example: createFolder("foo", 2)
        updates a sub folder at index 2 with the title foo

        Raises an AssertError if you call this method while not having the ability to edit the folder
        Raises an AssertError if the index is not of subtype int
        """

        url = self.metaData.getLink("edit")

        assert url is not None
        assert isinstance(index, int) or index is None

        header = self._baseHeader.copy()
        header['Content-Type'] = "application/vnd.huddle.data+json"

        try:
            if index is None:
                jsonData = self.metaData.jsonObj
            else:
                jsonData = self.getFolders()[index].metaData().jsonObj

            if title is not None: jsonData['title'] = title
            if description is not None: jsonData['description'] = description

            response = self._adapter.putRequest(url, header, json.dumps(jsonData))

            newLink = self._client.getUrlFromHeaderLink(response['Headers']['link'])
            return Folder(self._client,  newLink)
        except IndexError:
            print("the index: " + str(index) + " does not exist in the list of folder numbers we have")

    def  deleteFolder(self, index=None):
        """
        Deletes the parent folder, if an index is specified it will delete the sub folder instead.
        This method returns a folder object of the deleted folders parent folder e.g foo-->bar if we deleted
        bar we will be returned a folder of foo. Deleting a folder will also add it to this objects graveyard.
        The graveyard is used to restore folders you delete. This will stop you doing any method except restore.

        example: deleteFolder()
        deletes parent folder

        example: deleteFolder(2)
        deletes the subFolder  of the parent folder found at index 2 in GetFolders()

        Raises an AssertError if the index is not of subtype int
        """
        assert isinstance(index, int) or index is None

        try:
            if index is None:
                url = self.metaData.getLink("delete")
            else:
                url = self.getFolders()[index].metaData().getLink("delete")

            assert url is not None

            response = self._adapter.deleteRequest(url, self._baseHeader)

            self.metaData.graveyard.append(self.metaData)

            newLink = self._client.getUrlFromHeaderLink(response['Headers']['link'])

            return Folder(self._client, newLink)

        except IndexError:
            print("the index: " + str(index) + " does not exist in the list of folder numbers we have")

    def restoreFolder(self, index):
        """
        Restores a folder from this objects graveyard. All resources in the deleted folder will also be restored.
        If the folder is deleted and not in the graveyard there is  no way to restore the folder without knowing
        the full uri of the deleted folders restore link. Once the folder has been restored that folder will be removed
        from the graveyard. This method will return a folder of the restored folder

        example: restoreFolder(0)
        restores the folder on the the graveyard at index 0

        Raises an AssertError if the index is not of subtype int
        """
        assert isinstance(index, int)

        try:
            url = self.metaData.graveyard[index].selfLink + "/restore"
            response = self._adapter.putRequest(url, self._baseHeader, "{}")

            self.metaData.graveyard.pop(index)

            return Folder(self._client, response['Headers']['location'])
        except IndexError:
            print("the index: " + str(index) + " does not exist in the graveyard")

    def moveTo(self, newFolder):
        """
        Moves this folder to the specified folder in the parameter. This method will then return a folder object of the
        parent of the updated folder

        >>moveTo(FolderB)
        this folder is now in folder b

        Raises an AssertError if the folder you are trying to move doesn't have a move link
        Raises an AssertError or if it can't find the parent link of this folder
        Raises an TypeError if the newFolder parameter doesn't act like a folder object
        """
        moveURI = self.metaData.getLink("move")
        parent = self.metaData.getLinkIndex('parent')

        assert parent != -1
        assert moveURI is not None
        if not hasattr(newFolder, "metaData"): raise TypeError("Your newFolder does not have a metaData property")
        if not hasattr(newFolder, "selfLink"): raise TypeError("Your newFolder does not have a self link")

        self.metaData.jsonObj['links'][parent] = {'href' : newFolder.selfLink, 'rel' : 'parent'}
        header = self._baseHeader.copy()
        header['Content-Type'] = "application/vnd.huddle.data+json"
        response = self._adapter.putRequest(moveURI,header, json.dumps(self.metaData.jsonObj))

        newLink = self._client.getUrlFromHeaderLink(response['Headers']['link'])
        return Folder(self._client, newLink)

    def copyTo(self, newFolder):
        """
        Copies this folder to the specified folder in the parameter. This method will then return a folder object of the
        new copied folder

        >>copyTo(FolderB)
        this folder has now been copied to folder b

        Raises an AssertError if the folder you are trying to move doesn't have a copy link
        Raises an TypeError if the newFolder parameter doesn't act like a folder object
        """
        copyUri = self.metaData.getLink("copy")

        if not hasattr(newFolder, "metaData"): raise TypeError("Your newFolder does not have a metaData property")
        if not hasattr(newFolder, "selfLink"): raise TypeError("Your folder object is missing a selfLink")
        assert copyUri is not None

        header = self._baseHeader.copy()
        header['Content-Type'] = "application/vnd.huddle.data+json"
        body = '{ "targetFolder":{ "link":{ "rel": "self", "href": "' + newFolder.selfLink + '" } } }'
        response = self._adapter.postRequest(copyUri, header, body)

        return Folder(self._client, response['Headers']['location'])

    def editPermissions(self, json):
        url = self.metaData().getLink("permissions")

        assert url is not None

        headers = self._baseHeader
        headers['Content-Type'] = "application/vnd.huddle.data+json"

        response = self._adapter.postRequest(url, headers, json)

        return response

class WorkSpace(Api):
    """
    Provides api methods for a workspace. This class requires a workspace link. Once it has this you can get information
    about the workspace. Meta data about this workspace is stored in the metaData attribute which is of type
    HyperlinkResource. To get the meta data call lazyGet(). See the resource class for what you can do with this meta data.
    For more details about workspaces look at https://code.google.com/p/huddle-apis/wiki/Workspace
    """
    def __init__(self, client, workspaceLink):
        Api.__init__(self, client, workspaceLink)


    def refresh(self):
        return WorkSpace(self._client, self.selfLink)

    def getFolders(self):
        """
        hits the root folder in your workspace. This is returned as a Folder Object. This method is the same as
        getting the workspaces documentLibrary.

        example: getWorkSpace()
        api.folder.Folder Object
        """
        documentLibary = self.metaData().getLink("documentLibrary")
        assert documentLibary is not None

        folder = Folder(self._client, documentLibary)

        return folder.getFolders()

    def searchForDocument(self, query):
        #may or may not be live

        url = self._config['API']['huddleApiServer'] + "search/documents?query=" + "workspaceids=" + self.getWorkSpaceID()
        header = self._baseHeader.copy()

        response = self._adapter.getRequest(url, header)

        #didn't finish this as search isn't live yet
        print(response)

    def getCalandar(self):
        url = self._config['API']['huddleCalandarServer'] + self.getWorkSpaceID()

        return Calendar(self._client, url)


    def getWorkSpaceID(self):
        return self.selfLink.rsplit('/',1)[1]




