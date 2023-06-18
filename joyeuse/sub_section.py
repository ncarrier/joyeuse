'''
Created on 18 juin 2023

@author: nicolas
'''


class SubSection(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.__name = name
        self.__parameters = []
        self.__comments = []

    def add_comment(self, comment):
        self.__comments.append(comment)

    def add_parameter(self, parameter):
        self.__parameters.append(parameter)

    def __str__(self):
        result = f"{self.__name}\r\n"

        result += "".join([c + "\r\n" for c in self.__comments])
        result += "".join([str(p) for p in self.__parameters])

        return result
