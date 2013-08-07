from io import StringIO
import mimetypes
import os
import uuid

__author__ = 'adam.flax'

class MultiPartFormRequest(object):
    """
    Used by both the folder and document class as both may need to do similar items for uploading/editing a file
    """

    def __init__(self, file):
        self.file = file
        self.name = file.name
        self.mime = mimetypes.guess_type(self.name)[0] or 'application/octet-stream'
        self.title, self.extension = os.path.splitext(self.name)
        self._binary = file.read()

    def encode_mutipart_form_data(self, boundary):
        """
        Takes file contents and returns how it should look like as encoded in a muti form upload.
        You should never have to call this method as the createDocument method will create the mutipart_form data for
        you

        >>>__encode_mutipart_form_data
        --IAmABoundaryStringHearMyRawr1
        Content-Disposition: form-data;name=files; filename="features.txt"
        Content-Type: text/plain

        OAuth partcan be plugged into any http request library
        can work out difference between a bad response and access token for refresh and request
        works out if a token has expried, if it has it refreshes it
        stores acecss tokens in file
        attempts to load access token from file before it requests one

        --IAmABoundaryStringHearMyRawr1--
        """

        data = StringIO()
        data.write('--%s\r\n' % boundary)
        data.write('Content-Disposition: form-data; name=IAmAHardCodedValue; filename="%s"\r\n' % self.name)
        data.write('Content-Type: %s\r\n' % self.mime)
        data.write('\r\n')
        data.write('%s\r\n'% self._binary)
        data.write('--%s--' % boundary)

        return data.getvalue()
    
    def create_Boundary_String(self):
        """
        Returns our boundaryString needed. The boundaryString should be a unique string NOT found in the document. You
        Should never need to call this method as it is only there to help __encode_muti_form_data

        >>>__createBoundaryString
        IAmABoundaryStringHearMyRawr1
        """
        return str(uuid.uuid4())