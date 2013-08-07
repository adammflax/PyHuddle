import io
import unittest
from pyhuddle.api.create_mutipart_form_request import UploadFile
from pyhuddle.tests.document.fakeFile import FakeFile

__author__ = 'adam.flax'

class WhenWeSendFileToUploadFile(unittest.TestCase):

    def setUp(self):
        file = FakeFile("test.txt", "content")
        self._result = UploadFile(file)

        data = io.StringIO()
        data.write('--%s\r\n' % "fake")
        data.write('Content-Disposition: form-data; name=name=IAmAHardCodedValue; filename="%s"\r\n' % "test.txt")
        data.write('Content-Type: %s\r\n' % "text/plain")
        data.write('\r\n')
        data.write('%s\r\n'% "content")
        data.write('--fake--')

        self.validResponse = data.getvalue()


    def test_CheckForValidTitle(self):
        self.assertEqual(self._result.name, "test.txt")

    def test_CheckForValidMime(self):
        self.assertEqual(self._result.mime, "text/plain")

    def test_CheckForValidEncodedData(self):
        self.assertEqual(self._result.encode_mutipart_form_data("fake"), self.validResponse)

if __name__ == '__main__':
    unittest.main()

