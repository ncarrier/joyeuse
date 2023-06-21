'''
Created on 18 juin 2023

@author: nicolas
'''
import sys
import re
from joyeuse.settings.section import Section
from joyeuse.settings.sub_section import SubSection
from joyeuse.settings.parameter import Parameter


class Settings(object):
    '''
    classdocs
    '''
    SECTION_TITLE = u"^[0-9]\\. (.*)$"
    SEPARATION = u'^¨+$'
    SUB_SECTION_TITLE = u"^[0-9]\\.[0-9] .*$"
    PARAMETER = u"^([a-zA-Z]*):([0-9a-zA-Z]+) +<+$"

    def __compile_regexes(self):
        self.__section_title_re = re.compile(Settings.SECTION_TITLE,
                                             re.UNICODE)
        self.__separation_re = re.compile(Settings.SEPARATION, re.UNICODE)
        self.__sub_section_title_re = re.compile(Settings.SUB_SECTION_TITLE,
                                                 re.UNICODE)
        self.__parameter_re = re.compile(Settings.PARAMETER, re.UNICODE)

    def __is_section_title(self, line):
        return self.__section_title_re.match(line)

    def __is_separation(self, line):
        return self.__separation_re.match(line)

    def __is_sub_section_title(self, line):
        return self.__sub_section_title_re.match(line)

    def __is_parameter(self, line):
        return self.__parameter_re.match(line)

    def __init__(self, path):
        '''
        Constructor
        '''
        self.__path = path
        self.__sections = []
        self.__preamble = []

        self.__compile_regexes()

        # parse the settings file, creating and populating the sections
        section = None
        sub_section = None
        parameter = None
        with open(path, "r", newline='\r\n') as f:
            for line in f.readlines():
                line = line.strip()
                if self.__is_separation(line):
                    continue
                if self.__is_section_title(line):
                    section = Section(line)
                    self.__sections.append(section)
                    sub_section = None
                    parameter = None
                    continue

                if section is None:
                    self.__preamble.append(line)
                    continue

                # now we have encountered at least one section

                if self.__is_sub_section_title(line):
                    sub_section = SubSection(line)
                    parameter = None
                    section.add_subsection(sub_section)
                    continue

                match = self.__is_parameter(line)
                if match:
                    parameter = Parameter(match.group(1), match.group(2))
                    if sub_section is not None:
                        sub_section.add_parameter(parameter)
                    else:
                        section.add_parameter(parameter)
                    continue

                # we know we have a comment, let's see what to add it to
                if parameter is not None:
                    parameter.add_comment(line)
                    continue

                if sub_section is not None:
                    sub_section.add_comment(line)
                    continue

                section.add_comment(line)

    @property
    def sections(self):
        return self.__sections

    def save(self):
        with open(self.__path, "w") as f:
            f.write(str(self))

    def __str__(self):
        result = "".join([s + "\r\n" for s in self.__preamble])

        result += "".join([str(s) for s in self.__sections])

        return result


if __name__ == '__main__':
    # doesn't work, why?
    settings = Settings(sys.argv[1])

    settings.save()

    print(settings)
