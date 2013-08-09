  
Comments
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------
Comments
````````

class \ *comments*\.\ **Comments**\(api.Api)
	An api class for performing operations with Huddle's document comments
	
	**__init__**\(self, client, DocumentCommentLink)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our document comment resource
		
		**refresh**\()
			as all api objects are immutable they will not update. If for some reason you wish to force it to update you can do so by calling the refresh method. This will return a comments object of the resource but with 
			updated meta data.
			
		**getComments**\()
			returns a list of all comments in the documentComments
			
		**createComment**\(self, content, replyToID = None)
			*String* content: the comment its self, this needs to be less then 2049 characters
			*Int* replyToId: the id of the message you are replying to
			
			creates a comment, this returns a new comment object
			
		**deleteComment**\(self, index)
			*Int* index: the position is of the comment in the list
			
			Delets a comment, this returns a new comment object of the new data
		
		
	
Tutorials
----------------

Get a list of all comments, make a new comment then delete the comment
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
	comments = document.getComments()
	
	for comment in comments.getComments():
		print(comment.metaData.getTitle())
		
	comments.createComment("foo")
	comments.deleteComment(0)