# This file is part of Joyeuse.

# Joyeuse is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Joyeuse is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Joyeuse. If not, see <https://www.gnu.org/licenses/>.

import re
from joyeuse.misc.compat import Compat
from joyeuse.settings.item import Item


class Section(Item):
    '''
    classdocs
    '''
    SECTION_TITLE = u"^[0-9]\\. (.*)$"
    SEPARATION = u'^¨+$'

    def __init__(self, name):
        '''
        Constructor
        '''
        super().__init__(name)
        self.__sub_sections = []
        self.__parameters = []
        self.__separation_length = len(self.name)

    def add_parameter(self, parameter):
        self.__parameters.append(parameter)

    def add_subsection(self, sub_section):
        self.__sub_sections.append(sub_section)

    def __str__(self):
        result = f"{self._name}{Compat.newline}"
        result += self.__separation_length * '¨' + Compat.newline
        result += "".join([c + Compat.newline for c in self._comments])
        result += "".join([str(p) for p in self.__parameters])
        result += "".join([str(s) for s in self.__sub_sections])

        return result

    def set_separation_length(self, length):
        self.__separation_length = length

    @property
    def name(self):
        m = re.match(Section.SECTION_TITLE, self._name, re.UNICODE)

        return m.group(1).capitalize()

    @property
    def sub_sections(self):
        return self.__sub_sections

    @property
    def parameters(self):
        return self.__parameters
