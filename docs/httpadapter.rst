HttpAdapter
===============
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.

Module Interface
----------------

Adapter
`````````````
class \ *adapter*\.\ **Adapter**\()

	This class is used as adapter for HTTP libraries. Look at the wrapper/adapter pattern for more information. By using an adapter we can allow developers to use any library the wish
	
	**GetRequest**\(self, url, header)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		sends a GET request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>
		
	**DeleteRequest**\(self, url, header)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		sends a DELETE request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>

	**PostRequest**\(self, url, header, data)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		*String* data: the data to send to the request
		
		sends a POST request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>

	**PutRequest**\(self, url, header, data)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		*String* data: the data to send to the request
		
		sends a PUT request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>
		
.. warning:: This class does not have an implementation. Its only use is to be inheritied by other adapters to make sure they have the methods needed
.. seealso:: see  foo on creating your own adapter

Caseless_Dictionary
`````````````
class \ *caseless_dictionary*\.\ **CaselessDictionary**\()
	This class is a wrapper around pythons ``dictionary`` class. This class can perform the same operations as a normal dictionary. The only difference between this and the ``dictionary`` class is that when it comes to retrieval keys are case insensitive.
	The reason for this class is that according to the HTTP specification headers are case insensitive so we can never be sure what case the headers we get will be like.

Adapter_Urllib
`````````````
class \ *adapter_urllib*\.\ **AdapterHttpUrlLib**\(Adapter)

	This class is an adapter implementation for the urllib3 library
	
	**GetRequest**\(self, url, header)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		sends a GET request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>
		
	**DeleteRequest**\(self, url, header)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		sends a DELETE request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>

	**PostRequest**\(self, url, header, data)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		*String* data: the data to send to the request
		
		sends a POST request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>

	**PutRequest**\(self, url, header, data)
		*String* url: The url for the request to get sent to
		
		*Dict(String, String)* header: The headers for the HTTP request
		
		*String* data: the data to send to the request
		
		sends a PUT request to the server returns the response as a {Headers : CaselessDict<String, String>, String : Body>
		
Examples
--------
Create your own adapter
```````````````````````
PyHuddle has been developed in a way which allows you to use any http library with it. In this tutorial we will create a new adapter using the httplib2 library.

Your adapter must have the following methods inside it::

    def getRequest(self, url, header):
        raise NotImplementedError("Unimplemented abstract method")
		
    def deleteRequest(self, url, header):
        raise NotImplementedError("Unimplemented abstract method")

    def postRequest(self, url, header, data):
        raise NotImplementedError("Unimplemented abstract method")

    def putRequest(self, url, header, data):
        raise NotImplementedError("Unimplemented abstract method")

Your adapter must perform the following tasks. 

	* It must send the given request to the server. You should expect to deal with the following arguments <string> url, <Caseless Dictionary> headers, <string> body
	* It must create a response key value object of {"Headers" :<Caseless Dictionary>Headers, "Body" : <String>response}
	* It **should** cache the responses
	* Your adapter must then parse the response to the HuddleErrors Object. This objects responseability is to generate an error if we get an error code back from the server. This is important as some of the api requests will look out for particular errors. For instance if we upload a new version of a document we lock the existing document first. If the lock fails we should expect to see a HuddleConflictError being thrown.
	* It should then return the response key value
	

The responses we get back server are going to be different depending on the request. However you should expect to have to deal with the following headers. 


+---------------+----------------------------------------------+
|Name           |  Description                                 |
+===============+==============================================+
|Content-Type   |The specific content type of the response.    |
+---------------+----------------------------------------------+
|Status         |The status code returned by the response      |
+---------------+----------------------------------------------+
|Last-Modified  |The last modified time of the resource.       |
+---------------+----------------------------------------------+
|Link           |Signals a related resource or operation.      |
+---------------+----------------------------------------------+
|Location       |The URI that the new resource can be found at.| 
+---------------+----------------------------------------------+

Bearing all of this in mind we can now write our adapter for the HttpLib2 adapter::

	class adapterHttpLib2(Adapter):
		def __init__(self):
			self._huddleErrors = HandleCodeResponse()

		def getRequest(self, url, header):
			h = httplib2.Http(".cache") #allows us to cache our responses
			head, body = h.request(url, "GET", None, header) #get our headers and body data from the servers response

			response =  {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')} #parse our response data into the format PyHuddle Expects to see

			self._huddleErrors.CheckForErrors(response) #check for errors
			return response

		def deleteRequest(self, url, header):
			h = httplib2.Http(".cache") #allows us to cache our responses
			head, body = h.request(url, "DELETE", None, header) #get our headers and body data from the servers response

			response = {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')} #parse our response data into the format PyHuddle Expects to see

			self._huddleErrors.CheckForErrors(response) #check for errors
			return response

		def postRequest(self, url, header, body):
			h = httplib2.Http(".cache") #allows us to cache our responses
			head, body = h.request(url, "POST", body, header) #get our headers and body data from the servers response

			response  = {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')} #parse our response data into the format PyHuddle Expects to see

			self._huddleErrors.CheckForErrors(response) #check for errors
			return response


		def putRequest(self, url, header, body):
			h = httplib2.Http(".cache") #allows us to cache our responses
			head, body = h.request(url, "PUT", body, header) #get our headers and body data from the servers response

			response =  {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')} #parse our response data into the format PyHuddle Expects to see

			self._huddleErrors.CheckForErrors(response) #check for errors
			return response