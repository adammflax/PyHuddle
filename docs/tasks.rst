  
Tasks
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------
Tasks
````````

class \ *tasks*\.\ **Tasks**\(api.Api)
	An api class for performing operations with Huddle's task resource
	
	**__init__**\(self, client, taskLink)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our task resource
		
		**refresh**\()
			as all api objects are immutable they will not update. If for some reason you wish to force it to update you can do so by calling the refresh method. This will return a task object of the resource but with 
			updated meta data.
			
		**delete**\()
			deletes the given task. This method returns None.  This may seem strange but this is an old api that does not use hypermedia controls so we cannot do much else.

			.. warning:: As this is an old api it does not have a graveyard. Therefore there is no way to restore the task once its deleted.
			
		**editTask**\(self, title=None, description=None, status="NotStarted", plannedStartDate=None, completedDate=None, completedBy=None, updatedDate=None, attachments=[]):
	
			*String* title: The title of the task
			
			*String* description: The description of the task
			
			*String* status: the status of the task it can be 1 of the following values:
			
			+------------+--------------------------------------+
			|Name        | Description                          |
			+============+======================================+
			|NotStarted  | The task has yet to start            |
			+------------+--------------------------------------+
			|InProgress  | The task is in progress              |
			+------------+--------------------------------------+
			|Complete    | The task has been complete           |
			+------------+--------------------------------------+
			
			*String* plannedStartDate: The planned start date. This should be in this format %Y-%m-%dT%H:%M:%S
			
			*String* completeDate: The date the task was completed by. This should be in this format %Y-%m-%dT%H:%M:%S
			
			*String* completedBy: The user summary of the user who marked the task as complete. This should be in this format %Y-%m-%dT%H:%M:%S
			
			*String* updatedBy: The date the task was last updated on. This should be in this format %Y-%m-%dT%H:%M:%S
			
			*Documents* attachments: a list of document objects to attach to the task
			
			edits the the task if it succeeds, returns a task object 
			
			.. note:: please remember api objects are immutable so if youedit the task and call properties in ``metaData`` you will not see the changes unless you refresh first
		
		**addComment(self, text)
			*String* text: the text to add to the comment
			
			this adds a comment to the task and returns None. This may seem strange but this is an old api that does not use hypermedia controls so we cannot do much else.
		
Tutorials
----------------

Edit a task
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

Now that we have hit your /entry/ folder we can enter a workspace, get our workspace calandar and and look at our tasks
::

	ws = client.getWorkSpaces()[0]
	calandar = ws.getCalandar()
	document = ws.getFolders()[0].getDocuments()[0] #get us the first document in the first folder in the first workspace
	task  = ws.getTasks()[0]
	
	task = task.editTask(title="title", description="description", CompletedBy = "2011-05-05T16:12:47",  attachments=[document])
	
Delete a task
```````````

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

Now that we have hit your /entry/ folder we can enter a workspace, get our workspace calandar and and look at our tasks
::

	ws = client.getWorkSpaces()[0]
	calandar = ws.getCalandar()
	task  = ws.getTasks()[0]
	task.delete() #remember deleting a task returns None so no need to store the return
	
Add a comment
```````````

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

Now that we have hit your /entry/ folder we can enter a workspace, get our workspace calandar and and look at our tasks
::

	ws = client.getWorkSpaces()[0]
	calandar = ws.getCalandar()
	task  = ws.getTasks()[0]
	task.addComment("Spam, ham and eggs") #remember adding a task comment returns None so no need to store the return
