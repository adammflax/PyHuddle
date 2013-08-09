  
Users
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------
User
````````

class \ *user*\.\ **User**\(api.Api)
	An api class for performing operations with Huddle's task resource
	
	**__init__**\(self, client, userLink)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our user resource
		
	**getFriends**\(workspace=None)
		*Workspace* workspace: the workspace to get your friends list from. If you do not specify a workspace it will instead get it from all your workspaces
		
		returns a list of useers as a list of user objects where each user is a user from your friendslist.
		
Tutorials
----------------

Add a friend
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
	user = client.user
	for friend in user.getFriends(ws):
		print(friend.metaData.getTitle())

