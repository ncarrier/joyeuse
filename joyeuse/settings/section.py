'''
Created on 18 juin 2023

@author: nicolas
'''
import re


class Section(object):
    '''
    classdocs
    '''
    SECTION_TITLE = u"^[0-9]\\. (.*)$"

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

    @property
    def name(self):
        m = re.match(Section.SECTION_TITLE, self.__name, re.UNICODE)

        return m.group(1).capitalize()

    @property
    def sub_sections(self):
        return self.__sub_sections

    @property
    def parameters(self):
        return self.__parameters

    @property
    def comments(self):
        return "\n".join([l for l in self.__comments if len(l) > 0])
