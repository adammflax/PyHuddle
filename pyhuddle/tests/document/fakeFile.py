from msilib.schema import File

__author__ = 'adam.flax'

class FakeFile:

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def read(self):
        return self.content