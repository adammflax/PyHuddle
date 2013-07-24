"""
Contains a collection of classes that extend Exception. These errors are thrown when we get some kind of bad response
from the api. E.g. if we attempted to perforn an api task with out an oauth2 token the api would throw a
HuddleAuthenticationError. It is a good idea in your http adapter class to parse the response into HandleCodeResponse
class before you return the response. If you do this basic errors can be caught straight away. As the api methods them
selves do not have any error handling for bad requests/responses
"""
from math import floor

__author__ = 'adam.flax'

class HuddleBadResponseError(Exception):

    def __init__(self, statusCode, body):

        self.statusCode = statusCode
        self.body = body
        Exception.__init__(self, statusCode, body)

    def __str__(self):
        return "%s(%s)" % (self.statusCode, self.body)


class HuddleBadRequestError(HuddleBadResponseError):

    def __init__(self, body):
        HuddleBadResponseError.__init__(self, "400", body)

class HuddleAuthenticationError(HuddleBadResponseError):

    def __init__(self, body):
        HuddleBadResponseError.__init__(self, "401", body)

class HuddleForbiddenError(HuddleBadResponseError):

    def __init__(self, body):
        HuddleBadResponseError.__init__(self, "403", body)

class HuddleNotFoundError(HuddleBadResponseError):

    def __init__(self, body):
        HuddleBadResponseError.__init__(self, "404", body)

class HuddleConflictError(HuddleBadResponseError):
    def __init__(self, body):
        HuddleBadResponseError.__init__(self, "409", body)

class HuddleGoneError(HuddleBadResponseError):
    def __init__(self, body):
        HuddleBadResponseError.__init__(self, "410", body)

class HandleCodeResponse(object):

    def handleResponseError(self, response):
        code = int(response['Headers']['status'])
        typeOfCode = code // 100

        if typeOfCode != 1 and typeOfCode != 2 and typeOfCode != 3:
            if code == 400:
                e = HuddleBadRequestError(response['Body'])
                raise e
            if code == 401:
                e = HuddleAuthenticationError(response['Body'])
                raise e
            if code == 403:
                e = HuddleForbiddenError(response['Body'])
                raise e
            if code == 404:
                e =  HuddleNotFoundError(response['Body'])
                raise e
            if code == 409:
                e =  HuddleConflictError(response['Body'])
                raise e
            if code == 410:
                e =  HuddleGoneError(response['Body'])
                raise e
            else:
                e =  HuddleBadResponseError(response['Headers']['status'], response['Body'])
                raise e
        return None