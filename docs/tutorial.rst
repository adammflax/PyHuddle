Tutorials
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.


Create your own way to get an access token
----------------
By default the HandleAccessToken object will attempt to perform 3 legged OAuth by OOB. If you wish to change how the OAuth Flow works you can parse in your own function to the constructor of this object. In this tutorial we will
change the flow by getting an access token with a password profile rather then by using 3 legged OAuth.

This request is done by sending a POST request to Huddles server which contains:
 * your clientId
 * your client Secret
 * your username 
 * your password 
 
::
 
		def createAccessTokenReplacement(self):
			header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
			url = self._config['OAUTH2ENDPOINT']['huddleAccessTokenServer']

			body = {"grant_type": "password",
					"client_id": self._config['OAUTH2']['clientID'],
					"redirect_uri": self._config['OAUTH2']['redirectUri'],
					"username": self._config['OAUTH2']['username'],
					"password" : self._config['OAUTH2']['password]}

			response  = self._request.postRequest(url, header, parse.urlencode(body)) 
			responseBody = json.loads(response['Body'])

			try:
				oauthToken = token.Token(responseBody)
			except TypeError as e:
				print ("Bad response when requesting a token " + str(response))
				sys.exit()

			return oauthToken
			
In the first part of our function we simply perform a post request to the server with those details url encoded. If everything goes well the server should respond with a JSON response that looks like::

	HTTP/1.1 200 OK
	Content-Type: application/json
	Cache-Control: no-store

	{
	   "access_token":"S1AV32hkKG",
	   "expires_in":300,
	   "refresh_token":"8xLOxBtZp8"
	}
 
Finally we try and parse that json response into our token object which we then return. Please note that it is expected that this function returns a token object

So if we want to use this new function rather then OOB we call the HandleAccessTokenObject like this ::

	token = HandleAccessToken(request, config, createToken=createAccessTokenReplacement)


Get a list of all your workspaces
----------------

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

Now that we have hit your /entry/ folder we can ask for a list of all our workspaces ::	
	
	workspaceList = client.getWorkSpaces()

	for(ws in workspaceList):
		print(ws.metaData.getTitle())

Upload a file to a folder
----------------
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

Now that we have hit your /entry/ folder we can enter a workspace, jump to a folder and upload a file to it 
::

	ws = client.getWorkSpaces()[0]
	folder = ws.getFolders()[0]
	
	with open('file.txt', 'rb') as f:
		document = folder.createDocument(f, "this is a description of the document)
		
	print(document.metaData.getTitle())

Create a new task
----------------
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
	calandar = ws.getCalandar()
	
	task = calandar.createTask("title, "description")
	

	for a full list of arguments for createTask check the documentation for the calendar object