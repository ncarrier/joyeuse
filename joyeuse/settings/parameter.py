'''
Created on 18 juin 2023

@author: nicolas
'''


class Parameter(object):
    '''
    classdocs
    '''

    def __init__(self, name, value):
        '''
        Constructor
        '''
        self.__name = name
        self.__value = value
        self.__comments = []

    def add_comment(self, comment):
        self.__comments.append(comment)

    def __str__(self):
        result = f"{self.__name}:{self.__value} {30 * '<'}\r\n"

        result += "".join([c + "\r\n" for c in self.__comments])

        return result

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value
