'''
Created on Jun 19, 2023

@author: ncarrier
'''
from joyeuse.settings.settings import Settings


class Cube(object):
    '''
    classdocs
    '''

    def __init__(self, path):
        '''
        Constructor
        '''
        self.__settings = Settings(f"{path}/Secrets/SETTINGS.txt")

    @property
    def settings(self):
        return self.__settings
