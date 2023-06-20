'''
Created on 18 juin 2023

@author: nicolas
'''
import re


class SubSection(object):
    '''
    classdocs
    '''
    SUB_SECTION_TITLE = u"^[0-9]\\.[0-9] (.*)$"

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

    @property
    def name(self):
        m = re.match(SubSection.SUB_SECTION_TITLE, self.__name, re.UNICODE)

        return m.group(1).capitalize()

    @property
    def parameters(self):
        return self.__parameters

    @property
    def comments(self):
        return "\n".join([l for l in self.__comments if len(l) > 0])
