__author__ = 'adam.flax'

import configparser

class Config:
    """
    The config class reads the values stored in the config file specified by the constrcutor
    """
    config = configparser.ConfigParser()

    def __init__(self, location):
        self.config.read(location)







