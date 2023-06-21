'''
Created on 18 juin 2023

@author: nicolas
'''
from tkinter import StringVar


class Parameter(object):
    '''
    classdocs
    '''

    def __init__(self, name, value):
        '''
        Constructor
        '''
        self.__name = name
        self.__comments = []
        self.__var = StringVar(value=value)

    def add_comment(self, comment):
        self.__comments.append(comment)

    def __str__(self):
        result = f"{self.__name}:{self.value} {30 * '<'}\r\n"

        result += "".join([c + "\r\n" for c in self.__comments])

        return result

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__var.get()

    @property
    def comments(self):
        return "\n".join([l for l in self.__comments if len(l) > 0])

    @property
    def var(self):
        return self.__var
