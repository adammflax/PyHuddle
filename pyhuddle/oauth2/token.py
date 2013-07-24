__author__ = 'adam.flax'

from datetime import datetime, timedelta

class Token(object):
    def __init__(self, json):
        """
        requires a json response in the form of  {  "access_token":"S1AV32hkKG",   "expires_in":300,   "refresh_token":"8xLOxBtZp8"}
        and stores it in this object. This object is useful as it can tell you if your token has expired or not
        """
        #check to see if our token json is valid
        if "expires_in" not in json:
            raise TypeError("The json is not in a valid form of a token as it does not contain an expires_in")
        if "access_token" not in json:
            raise TypeError("The json is not in a valid form of a token as it does not contain an access_token")
        if "refresh_token" not in json:
            raise TypeError("The json is not in a valid form of a token as it does not contain an refresh_token")

        self.json = json
        self.expiryTime = datetime.now() + timedelta(seconds=self.getExpiry())

    def isExpired(self):
        """
        returns true if the token has expired. Otherwise it will return false
        """
        return True if (datetime.now() > self.expiryTime) else False

    def getAccessToken(self):
        return self.json.get('access_token')

    def getRefreshToken(self):
        return  self.json.get('refresh_token')

    def getExpiry(self):
        return  self.json.get('expires_in')




