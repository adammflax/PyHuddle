__author__ = 'adam.flax'

"""
This is the class we wish to use for http requests.
In this library we wish that you could plug in any http library into the project and it will work
Therefore you may need to create your on httpAdapter class
There is an example of this already which I have done for the httpLib2 library

Each method should return a dict of {Headers : <header keys + values>, Body: body<Bytes>}
The library will automatically try and convert the body response into utf-8 for you so return the content as bytes

The library expects the http layer to check for normal status code errors, do this by parsing your response into
the huddleErrors.handleResponseError class
"""

class Adapter(object):
    def getRequest(self, url, header):
        """
        The url should be type string
        you should expect the headers to be type dict {"Content:type" : "value", "Accept" : "value"}
        """
        raise NotImplementedError("Unimplemented abstract method")

    def postRequest(self, url, header, body):
        """
        The url should be type string
        you should expect the headers to be type dict {"Content:type" : "value", "Accept" : "value"}
        The body should be of type string
        """
        raise NotImplementedError("Unimplemented abstract method")

    def deleteRequest(self, url, header):
        """
        The url should be type string
        you should expect the headers to be type dict {"Content:type" : "value", "Accept" : "value"}
        """
        raise NotImplementedError("Unimplemented abstract method")

    def putRequest(self, url, header):
        """
        The url should be type string
        you should expect the headers to be type dict {"Content:type" : "value", "Accept" : "value"}
        The body should be of type string
        """
        raise NotImplementedError("Unimplemented abstract method")

