  
Api
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------
Api
```
class \ *api*\.\ **Api**\()
	This is implemented by all api classes. This is a base class which you should never have to call
	
	**__init__**\(self, client, link)
		*HuddleClient* client: An instance of the HuddleClient class
		
		*String* link: a URI pointing to our resource
	
	**_getRequest**\()
		performs a GET request to our resource and returns the body of the request.
		
	Properties:
	
	*String* selfLink: the URI of the resource
	
	*Resource* metaData: the meta data of the resource


Config
``````
class \ *config*\.\ **Config**\()
	This class is responseable for managing your configuration file which should be in the form of a .ini file
	
	**__init__**\(self, location)
		*String* location: the location of your configuration file

Create_multipart_form_request
`````````````````````````````
class \ *create_multipart_form_request*\.\ **MultiPartFormRequest**\()
	This class creates the request needed for a multi part form request which is needed for when you upload a document to Huddle.
	
	**__init__**\(self, file)
		*File* a file opened with binary reading i.e if you are rading from a file do it like this ``open("file path", "rb")``
		
	**create_boundary_string**\()
		returns a boundary string. This boundary strings found in your header and in the body need to be the same. Calling this method again will generate a new boundary string so make sure you save your boundary string
		
	**encode_multipart_form_data**\(self, boundary)
		*String* boundary: the boundary string to use, this needs to be a unique string not found in the body of your file. Generate this with the ``create_boundary_string`` method
		
		this method will return as string the body needed for a multi_part_form_request upload
		
	Properties:
	
	*File* file: the file we are creating the request for
	
	*String* mime: the mime type of the file, if it can't find it it will default to ``application/octet-stream``
	
	*String* title: the name of the file
	
	*String* extension: the extention of the file
	
.. warning:: You should never need to use this class. The entire point of this library is to abstract away from the wire protocol. It is here for completeness only.
	
	
Huddle_Client
````````````
class \ *huddle_client*\.\ **HuddleClient**\()
	This class initalizes our connection to the huddle Api. This class also hits /entry/
	
	**__init__**\(self, token, adapter, config)
		*TokenHandler* token: an instance of the token handler class
		
		*Adapter* adapter: an instance of the the http adapter we should use
		
		*Config* config: an instance of the Config class
	
	**getWorkspaces**\()
		returns all of your workspaces as a list of workspace objects
		
	**createBaseHeader**\()
		used by all api requests as all api requests as basis for their HTTP headers as they all have some headers in common such as all of them need an AuthorizationHeader
		
	**getUrlFromHeaderLink**\()
		returns the url in a link header.
		
	Properties:
	
	*HyperLinkResource* metaData: Returns the meta data for hitting /entry/
	
	*User* user: The user object of the user running your application

HandleCodeResponse
`````````````
class \ *Huddle_errors*\.\ **HandleCodeResponse**\()

	Makes sure that we did not recieve a bad response back from the server. If we did it will throw the appropriate error. This is useful as certain api methods will try and react to these errors being thrown. 
	
	**CheckForErrors**\(response)
		checks our response for error codes and throws errors if we get a bad response. A bad response is defined as any error that doesn't start with a 1,2 or a 3.
	
		The errors that can get thrown are found below
		
		+--------------------------+----------------------------------------------------------------+
		|Name                      |    Description                                                 |
		+==========================+================================================================+
		|HuddleBadRequestError     | Occurs when we get a 400 back from the server                  |
		+--------------------------+----------------------------------------------------------------+
		|HuddleAuthenticationError | Occurs when we get a 401 back from the server                  |
		+--------------------------+----------------------------------------------------------------+
		|HuddleForbiddenError      | Occurs when we get a 403 back from the server                  |
		+--------------------------+----------------------------------------------------------------+
		|HuddleNotFoundError       | Occurs when we get a 404 back from the server                  |
		+--------------------------+----------------------------------------------------------------+
		|HuddleConflictError       | Occurs when we get a 409 back from the server                  |
		+--------------------------+----------------------------------------------------------------+
		|HuddleGoneError           | Occurs when we get a 410 back from the server                  |
		+--------------------------+----------------------------------------------------------------+
		| HuddleBadResponseError   | Occurs when we get a bad response that is any other error code |
		+--------------------------+----------------------------------------------------------------+

Hyperlink_Resource
``````````````````
class \ *resource*\.\ **HyperLinkResource**\(Resource)
	
	All parts of the api that use hypermedia controls will use this resource as a base
		
	**getLink**\(self, rel)
		*String* rel: the name of the URI you are trying to find e.g. "self" to get the resources own URI
		
		 Returns the URI of the link you are trying to find when you give its relative name. This will return None if it cannot find the resource
		 
	**getLinkIndex**\(self, rel)
		*String* rel: the name of the URI you are trying to find e.g. "self" to get the resources own URI
		
		Returns what number index in the Link list the link is. If it cannot find the link it will return -1

	Properties:
	
	*String* selfLink : the url of this resource
	
	*List* graveyard : a list of resources belonging to this resource that have been deleted
	
Non_Hyperlink_Resource
``````````````````````
class \ *resource*\.\ **NonHyperLinkResource**\(Resource)

	All parts of the api that do not use hypermedia controls will use this resource as a base

	Properties:
	*String* selfLink : the url of this resource
.. note:: this class has no new methods

Resource
````````
class \ *resource*\.\ **Resource**\()

	This class implemented by Hyperlink and Non_Hyperlink Resource. You should never call this class it is simply the base class

	**__init__**\(self, jsonData)
		*String* / *Dict<String, String>* jsonData: The json data of the resource, this can either be as a dictionary or as a string
	
	**getTitle**\(self)
		returns the name of the resource as a *String* for instance if you have a folder called "Spam" it would return "Spam"
		
	**getDescription**\(self)
		returns the description of the resource as a *String* for instance if your description of a folder was "Spam, Ham and Eggs" it would return "Spam, Ham and Eggs"
		
	Properties:
	
	*Dict<String, String>* jsonObj: a dictionary of the meta data of our resource
		
	.. note:: resources descriptions can be empty do not always expect a description back. If the description is empty you will be returned an empty *String*

Tutorials
----------------

examples
````````
Get a list of all workspaces ::

	config = Config("config.ini").config 	#grab our config info
	adapter = HttpAdapterHttpUrlLib() 	#pick a http library to use
	tokenHandler = HandleAccessToken(adapter, config) 	#get our token
	client = HuddleClient(tokenHandler, adapter, config) #all api requests need to start with this. This allows us to hit /entry

	
These 4 lines are needed at the start of any script. They are effectively the setting up of the library. This involves
 * loading your PyHuddle settings
 * choosing an HTTP adapter to use
 * getting an access token
 * talking to huddle and hitting /entry/

Now that we have hit your /entry/ folder we can ask for a list of all our workspaces ::	
	
	workspaceList = client.getWorkSpaces()

	for(ws in workspaceList):
		print(ws.metaData.getTitle())