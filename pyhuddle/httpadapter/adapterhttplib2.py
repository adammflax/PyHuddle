#import httplib2 - commented out as it would mean we'd have to bundle another module for this library for the sake of an example... not good
from .adapter import Adapter
from .caselessdictionary import CaselessDictionary
from ..api.huddleErrors import HandleCodeResponse

class adapterHttpLib2(Adapter):
    """
    an example of adapting the urlLib library to our common interface.
    The requests should return a dictionary of the headers (as a dictionary) and the body as bytes
    The library expects the http layer to check for normal status code errors, do this by parsing your response into
    the huddleErrors.handleResponseError class
	
	This module is commented out to avoid it erroring as it is dependent on external modules (httplib2)
    """

    def __init__(self):
        self._huddleErrors = HandleCodeResponse()

    def getRequest(self, url, header):
        """
        implementation of a get request
        """
        #h = httplib2.Http(".cache")
        #head, body = h.request(url, "GET", None, header)

        #response =  {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')}

        #self._huddleErrors.handleResponseError(response)
        #return response

    def deleteRequest(self, url, header):
        """
        implementation of a delete request
        """
        #h = httplib2.Http(".cache")
        #head, body = h.request(url, "DELETE", None, header)

        #response = {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')}

        #self._huddleErrors.handleResponseError(response)
        #return response

    def postRequest(self, url, header, body):
        """
        implementation of a post request
        """
        #h = httplib2.Http(".cache")
        #head, body = h.request(url, "POST", body, header)

        #response  = {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')}

        #self._huddleErrors.handleResponseError(response)
        #return response


    def putRequest(self, url, header, body):
        """
        implementation of a PUT request
        """
        #h = httplib2.Http(".cache")
        #head, body = h.request(url,"PUT", body, header)

        #response =  {"Headers" : CaselessDictionary(head), "Body" : body.decode('utf-8')}

        #self._huddleErrors.handleResponseError(response)
        #return response