OAuth2
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------

HandleAccessToken
`````````````
class \ *handle_access_token*\.\ **HandleAccessToken**\()

	This class is response for retriving access tokens and managing them.

	**__init__**\(self, adapter, config, createToken=None)
		*Adapter* adapter: an instance of the the http adapter we should use
		
		*Config* config: an instance of the Config class
		
		*Function* createToken: an optional function which if used will define the flow for OAuth2 (By default it will do 3 legged OAuth OOB).

	**HandleAccessToken**\(self)
		returns an access token from memory. If the access token does not exist it will call the createToken function to get it. If the token has expired it will refresh it 
		
	**RefreshAccessToken**\(self)
		refreshes an existing access token from memory if we get a good response back from the server the refreshed token is returned.
		
	**CreateAccessTokenReplacement**\(self)
		the default function that is called to get an access token from the server. This will only be called if you do not specify a function to use in the constructor. This function
		returns an access token by performing 3 legged OAuth by out of band.
		
	Properties:
	
	*Token* oauthToken: a token object which stores the access token for the user

.. seealso:: see foo on how to create an adapter.
.. seealso:: see  foo on setting up your config file for pyHuddle.
.. seealso:: see foo on making a custom createToken function.

OAuth
`````````````
class  \ *handle_access_token*\.\ **OAuth**\()

	This class has all the requests needed for oauth2 such as refreshing or getting a token. 

	**__init__**\(self, adapter, config, createToken=None)
		*Adapter* adapter: an instance of the the http adapter we should use
		
		*Config* config: an instance of the Config class
		
		*Function* createToken: an optional function which if used will define the flow for OAuth2 (By default it will do 3 legged OAuth OOB).
	
	**ObtainAccessTokenBy3LeggedOAuth**\(self, auth_code)
		*String* auth_code : An authorization code used in the 3 legged OAuth process. For details on how to get an authorization code check out how 3 legged oAuth works
		
		sends a POST request to the server to get an access token by exchanging it for an auth code. 
		
	**RefreshAccessToken**\(self, token)
		*Token* token: A token object that would of been created in the HandleAccessToken's GetAccessToken method
		
		sends a POST request to the server that exchanges an access token for another access token. We may need to do this as access tokens in Huddle expire every 20 minutes
		
.. warning:: You should never have to use or worry about this class as it is invoked by the HandleAccessToken Class. It is here for completeness only.
.. seealso:: see foo on how to create an adapter.
.. seealso:: see  foo on setting up your config file for pyHuddle.
.. seealso:: see foo on making a custom createToken function.

Token
`````````````
class  \ *token*\.\ **Token**\()
	This class stores an access tokens and has methods around making retrival of specific data easier.
	
	**__init__**\(self, json)
		*Dict(String, String)* json: This is the json response that came back from the server after getting an access token. This response needs to be turned into json by using ``json.loads()`` The json response should look like this::

				{
				   "access_token":"S1AV32hkKG",
				   "expires_in":300,
				   "refresh_token":"8xLOxBtZp8"
				}				 
		
	**IsExpired**\(self)
		returns True or False depending on if the token has expired
		
	**GetAccessToken**\(self)
		returns the Access Token as a string
		
	**GetRefreshToken**\(self)
		returns the Refresh Token as a string
		
	**GetExpiry**\(self)
		returns the duration of the access token in seconds
		
	Properties:
	
	*String* json: the json representation of our access token, refresh token and expires_in

.. note:: You should never have to call the getRefreshToken method as this is handled by the HandleAccessToken class. It is here for completeness only.
.. note:: You should never have to call the getExpiry method as you should be using the isExpiredMethod to check if the token has expired or not. It is here for completeness only.
Tutorials
--------

Examples
````````
PyHuddle abstracts most of the OAuth protocol away. Generally all you need to do is initialize the HandleAccessToken class and parse it into the HuddleClient object. This is because PyHuddle will do the rest for you. This can be seen below::

	tokenHandler = HandleAccessToken(adapter, config) 	#get our token
	client = HuddleClient(tokenHandler, adapter, config) #all api requests need to start with this. This allows us to hit /entry
	
Sometimes you may want to change the OAuth flow to get an access token. This will mostly be done in systems in which it is unsuitable for the user to paste in an auth code into the application such as websites. Check out
the tutorial page on how to do this.

.. seealso:: see  foo on setting up your config file for pyHuddle.

Create your own way to get an access token
`````````````````````````````````````````
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
				oauthToken = Token(responseBody)
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


