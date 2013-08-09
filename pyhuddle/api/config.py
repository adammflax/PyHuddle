import configparser

"""
Created on 08 August 2013
@author: Adam Flax
"""
class Config():
    """
    The config class reads the values stored in the config file specified by the constrcutor
    """
    config = configparser.ConfigParser()

    def __init__(self, location):
        self.config.read(location)







