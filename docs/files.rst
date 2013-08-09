  
Files
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------
Documents
`````````

class \ *files*\.\ **Document**\(api.Api)
	An api class for performing operations with Huddle's documents
	
	**__init__**\(self, client, documentLink)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our document  resource
		
	**refresh**\()
		as all api objects are immutable they will not update. If for some reason you wish to force it to update you can do so by calling the refresh method. This will return a Document object of the resource but with updated meta data.
			
	**delete**\()
		deletes the document and stores a refresh to the document in this documents graveyard. This method will then return the parent folder
			
	**restore**\()
		restores this document if it has been deleted **and** it has a reference of it in the graveyard, it will then remove the reference to this document from the graveyard
			
	**update**\(self, tiele=None, description=None)
		*String* title: the title of the folder
		*String* description: the description of the folder
		
		updates the documents name and/or description. Returns a document object of the updated document
		
		.. note:: please remember api objects are immutable so if you update the document and call items in ``metaData`` you will not see the changes unless you refresh first
			
	**copyTo**\(self, folder)
		*Folder* folder: the folder object you wish to copy the document to
		
		copies the document to a folder, Returns a document object of the copied document
			
	**createNewVersion**\(self, file, title=None, description=None, versionNote = None)
		*File* file: a file opened with binary reading i.e if you are rading from a file do it like this ``open("file path", "rb")``
			
		*String* title: a title of the document
		*String* description a description of the document
		*String* version note: a version note about the new document
			
		Locks the document and uploads the new version of this document after it has done this it will unlock the document, if all went well it will return a Document Object of the new document
		
		.. note:: please remember api objects are immutable so if you create a new version of the document and call items in ``metaData`` you will not see the changes unless you refresh first
			
	**__createLock**\()
		locks the document and returns the HTTP response of the lock
			
		.. warning:: You should never have to call this method as functions that need to lock do it for you automatically. It is here for completeness only.
			
	**__deleteLock**\(self url)
		*String* url: the url of the lock to unlock
			
		unlocks the document and returns the HTTP response of the lock
			
		.. warning:: You should never have to call this method as functions that need to unlock  a doucment do it for you automatically. It is here for completeness only.
		
	**download**\(self)
		returns a dictionary of the data you will need to construct a file on the users computer. This method does not physically download the file, It just provided the data so that you can make that download happen
		The dictionary returned is {"filename": name, "mime" : mimetype, "binary" : content of the file}
		
	**moveTo**\(self, folder)
		*Folder* folder: the folder object you wish to move document to
		
		moves the document to a folder, Returns a document object of the moved document
			
	**versionHistory**\(self)
		returns a dictionary of the version history of the object
			
	**getComments**\(self)
		returns the comments on the document as a Comments Object

Folders
```````		

class \ *files*\.\ **Folder**\(api.Api)
	An api class for performing operations with Huddle's folders
	
	**__init__**\(self, client, folderLink)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our folder resource
		
	**refresh**\()
		As all api objects are immutable they will not update. If for some reason you wish to force it to update you can do so by calling the refresh method. This will return a Folder object of the resource but with updated meta data.	
		
	**getFolders**\()
		returns a list of all sub folders as a list of Folder objects
		
	**getDocuments**\()
		returns a list of all documents in the folders as a list of Document objects
		
	**createDocument**\(self, file, description="", index=None)
		*File* file: a file opened with binary reading i.e if you are rading from a file do it like this ``open("file path", "rb")``
		
		*String* description a description of the document
		
		*Int* index: the folder/subfolder you wish to create the document in, if you don't specify a number it will upload it to this folder, if you specify a number it will upload it to this folders  sub folder e.g. index=0 will upload the document to the first sub folder in this folder
		
		Attemtps to create a new document and upload the content you specified in the file to it. If it succeeds it will be returned as a Document object
		
		.. note:: please remember api objects are immutable so if you create a document and call ``getDocuments()`` you will not see the changes unless you refresh first
	
	
	**createFolder**\(self, file, description="", index=None)
		*String* title: a title of the folder
		
		*String* description a description of the folder
		
		*Int* index: the folder/subfolder you wish to put the folder into, if you don't specify a number it will create the folder in this folder, if you specify a number it will upload it to this folders sub folder e.g. index=0 will create the folder in the first sub folder in this folder
		
		Attemtps to create a new folder, if it succeeds it will return the newly created folder as a folder object
		
		.. note:: please remember api objects are immutable so if you create a folder and call ``getFolder()`` you will not see the changes unless you refresh first
		
	**updateFolder**\(self, title=None, description=None, index=None)
			*String* title: a title of the folder
		
		*String* description a description of the folder
		
		*Int* index: the folder/subfolder you wish to update, if you don't specify a number it will update this folder, if you specify a number it will update that subfolder instead e.g. index=0 will update the folder in the first sub folder in this folder
		
		Updates the meta data of the folder. If it succeeds it will return a folder object of the updated folder
		
		.. note:: please remember api objects are immutable so if you update a folder and call ``getFolder()`` you will not see the changes unless you refresh first
		
	**deleteFolder**\(self, index=None)
		*Int* index: the folder/subfolder you wish to delete, if you don't specify a number it will delete this folder, if you specify a number it will delete that subfolder instead e.g. index=0 will delete the folder in the first sub folder in this folder
		
		Deletes the specified folder and all of it sub folders and documents, if it succeeds it will return the parent folder of the folder you just deleted as a folder resource. If you delete a folder its meta data will be stored in the graveyard 
		
		.. note:: please remember api objects are immutable so if you delete a folder and call ``getFolder()`` you will not see the changes unless you refresh first
		
	**restoreFolder**\(self, index)		
		*Int* index: the position in the graveyards list of the folder you wish to restore e.g. restore(0) will restore the first folder in the graveyard
		
		Updates the meta data of the folder. If it succeeds it will return a folder object of the updated folder and remove the metadata from the graveyard
		
		.. note:: please remember api objects are immutable so if you restore a folder and call ``getFolder()`` you will not see the changes unless you refresh first
		
	**moveTo**\(self, folder)
		*Folder* folder: the folder object you wish to move the folder and all of its sub folders and files to
		
		moves the folder to a parernt folder, Returns a folder object of the folder you just moved the folder to

		.. note:: please remember api objects are immutable so if you move a folder and call ``getFolder()`` you will not see the changes unless you refresh first
		
	**copyTo**\(self, folder)
		*Folder* folder: the folder object you wish to move the folder and all of its sub folders and files to
		
		copies the folder to a parernt folder, Returns a folder object of the folder you just copied the folder to
		
	**editPermissions**\(self, json)
		*String* json: the json string structure of the permissions
	
Workspace
````````

class \ *files*\.\ **Workspace**\(api.Api)
	An api class for performing operations with Huddle's folders
	
	**__init__**\(self, client, workspaceLink)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our workspace resource
		
	**refresh**\()
		As all api objects are immutable they will not update. If for some reason you wish to force it to update you can do so by calling the refresh method. This will return a Workspace object of the resource but with updated meta data.	

	**getFolders**\()
		Returns a list of root folders in the workspace as a list of Folder objects
		
	**getCalandar**\()
		returns the workspace's calandar as a calandar object
		
	**getWorkspaceID**\()
		returns the workspaces ID as a int
		
		.. warning:: you should never have to call this method, it is used specifically for the parts of the api that do not use hypermedia controls. It is here for completeness only.
Tutorials
----------------

make a new folder, upload a file to it, move the folder
````````

::

	config = Config("config.ini").config 	#grab our config info
	adapter = HttpAdapterHttpUrlLib() 	#pick a http library to use
	tokenHandler = HandleAccessToken(adapter, config) 	#get our token
	client = HuddleClient(tokenHandler, adapter, config) #all api requests need to start with this. This allows us to hit /entry

	
These 4 lines are needed at the start of any script. They are effectively the setting up of the library. This involves
 * loading your PyHuddle settings
 * choosing an HTTP adapter to use
 * getting an access token
 * talking to huddle and hitting /entry/

Now that we have hit your /entry/ folder we can enter a workspace, get our folder
::

	ws = client.getWorkSpaces()[0]
	folder = ws.getFolders()[0]

	folder = folder.createFolder("title", "description")
	
	with open("file path", "rb") as f:
		folder.createDocument(f, "description")
		
	folderB = ws.getFolder()[1]
	
	folder.moveTo(folderB)
	
delete the first sub folder in a folder and then restore it
````````

::

	config = Config("config.ini").config 	#grab our config info
	adapter = HttpAdapterHttpUrlLib() 	#pick a http library to use
	tokenHandler = HandleAccessToken(adapter, config) 	#get our token
	client = HuddleClient(tokenHandler, adapter, config) #all api requests need to start with this. This allows us to hit /entry

	
These 4 lines are needed at the start of any script. They are effectively the setting up of the library. This involves
 * loading your PyHuddle settings
 * choosing an HTTP adapter to use
 * getting an access token
 * talking to huddle and hitting /entry/

Now that we have hit your /entry/ folder we can enter a workspace, get our folder
::

	ws = client.getWorkSpaces()[0]
	folder = ws.getFolders()[0]

	folder.deleteFolder(0)
	folder.restoreFolder(0) #the index here is what position the folder we just deleted in, is in on the graveyard
	
edit permissions of the folder
````````

::

	config = Config("config.ini").config 	#grab our config info
	adapter = HttpAdapterHttpUrlLib() 	#pick a http library to use
	tokenHandler = HandleAccessToken(adapter, config) 	#get our token
	client = HuddleClient(tokenHandler, adapter, config) #all api requests need to start with this. This allows us to hit /entry

	
These 4 lines are needed at the start of any script. They are effectively the setting up of the library. This involves
 * loading your PyHuddle settings
 * choosing an HTTP adapter to use
 * getting an access token
 * talking to huddle and hitting /entry/

Now that we have hit your /entry/ folder we can enter a workspace, get our folder
::

	ws = client.getWorkSpaces()[0]
	folder = ws.getFolders()[0]

	permissions = """
			{
				"link": { "rel": "self", "href": "/folders/123/permissions" },
				
				"permissionChange": [
				{
					"cascade": "false",
					"team": 
						{ 
							"title": "teamA",
							"type": "members",
							"link": { "rel": "self", "href": "/teams/12345" },
							"permissions": { "permission": [ { "type": "Read" }, { "type": "Edit" } ] }
						}
				},
				{
					"cascade": "true",
					"team": 
						{ 
							"title": "teamB", 
							"type": "members",  
							"link": { "rel": "self", "href": "/teams/22345"  }, "permissions": " "}
						}
				}]
			}
	"""
	
	folder.editPermissions(permissions)
	
		
