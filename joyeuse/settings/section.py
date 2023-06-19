'''
Created on 18 juin 2023

@author: nicolas
'''


class Section(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.__name = name
        self.__sub_sections = []
        self.__comments = []
        self.__parameters = []

    def add_parameter(self, parameter):
        self.__parameters.append(parameter)

    def add_subsection(self, sub_section):
        self.__sub_sections.append(sub_section)

    def add_comment(self, comment):
        self.__comments.append(comment)

    def __str__(self):
        result = f"{self.__name}\r\n"
        result += len(self.__name) * '¨' + "\r\n"
        result += "".join([c + "\r\n" for c in self.__comments])
        result += "".join([str(p) for p in self.__parameters])
        result += "".join([str(s) for s in self.__sub_sections])

        return result
