  
Calandar
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------
Calandar
````````

class \ *calandar*\.\ **Calandar**\(api.Api)
	An api class for performing operations with Huddle calandars
	
	**__init__**\(self, client, calandarLink)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our calandar resource
	
	**refresh**\()
		as all api objects are immutable they will not update. If for some reason you wish to force it to update you can do so by calling the refresh method. This will return a Calandar object of the resource but with 
		updated meta data.
		
	**getTasks**\()
		returns a list of tasks (as Task objects) for all tasks in the calandar
		
	**createTask**\(self, title, description=None, status="NotStarted", plannedStartDate=None, completedDate=None, completedBy=None, updatedDate=None, attachments=[]):
	
		*String* title: The title of the task, this is the only mandatory field
		
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
		
		creates a task and if it succeeds, returns a task object 
		
		.. note:: please remember api objects are immutable so if you create a task and call ``GetTasks()`` you will not see the changes unless you refresh first
		
		.. seealso:: see  foo on the document api to find out how to get documents to attach to the task
Tutorials
----------------

Get a list of all tasks
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
	
	for task in ws.getTasks():
		print(task.metaData.getTitle())
	
Create a new task
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

Now that we have hit your /entry/ folder we can enter a workspace, get our workspace calandar and create a task
::

	ws = client.getWorkSpaces()[0]
	document = ws.getFolders()[0].getDocuments()[0] #get us the first document in the first folder in the first workspace
	calandar = ws.getCalandar()
		
	task = calandar.createTask("title", description="description", CompletedBy = "2011-05-05T16:12:47",  attachments=[document])