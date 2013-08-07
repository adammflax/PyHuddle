import urllib
from .adapter import Adapter
from .caseless_dictionary import CaselessDictionary
from ..api.huddle_errors import HandleCodeResponse

class AdapterHttpUrlLib(Adapter):
    """
    an example of adapting the urlLib library to our common interface.
    The requests should return a dictionary of the headers (as a dictionary) and the body as bytes
    The library expects the http layer to check for normal status code errors, do this by parsing your response into
    the huddleErrors.handleResponseError class
    """

    def __init__(self):
        self._huddleErrors = HandleCodeResponse()

    def getRequest(self, url, header):
        """
        implementation of a get request
        """
        req = urllib.request.Request(url, headers=header)
        f = urllib.request.urlopen(req)

        newBody = f.read().decode('utf-8')
        newHeader = dict(f.info())
        newHeader['status'] = f.status

        response  = {"Headers" : CaselessDictionary(newHeader), "Body" : newBody}

        self._huddleErrors.handleResponseError(response)
        return response

    def deleteRequest(self, url, header):
        """
        implementation of a delete request
        """
        req = urllib.request.Request(url, headers=header, method='DELETE')
        f = urllib.request.urlopen(req)

        newBody = f.read().decode('utf-8')
        newHeader = dict(f.info())
        newHeader['status'] = f.status

        response  = {"Headers" : CaselessDictionary(newHeader), "Body" : newBody}

        self._huddleErrors.handleResponseError(response)
        return response

    def postRequest(self, url, header, body):
        """
        implementation of a post request
        """

        body = body.encode('utf-8')

        req = urllib.request.Request(url, data=body, headers=header)
        f = urllib.request.urlopen(req)

        newBody = f.read().decode('utf-8')
        newHeader = dict(f.info())
        newHeader['status'] = f.status

        response  = {"Headers" : CaselessDictionary(newHeader), "Body" : newBody}

        self._huddleErrors.handleResponseError(response)
        return response


    def putRequest(self, url, header, body):
        """
        implementation of a PUT request
        """

        body = body.encode('utf-8')

        req = urllib.request.Request(url, data=body, headers=header, method='PUT')

        f = urllib.request.urlopen(req)

        newBody = f.read().decode('utf-8')
        newHeader = dict(f.info())
        newHeader['status'] = f.status

        response  = {"Headers" : CaselessDictionary(newHeader), "Body" : newBody}

        self._huddleErrors.handleResponseError(response)
        return response