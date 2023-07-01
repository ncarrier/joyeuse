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


class SubSection(Item):
    '''
    classdocs
    '''
    SUB_SECTION_TITLE = u"^[0-9]\\.[0-9] (.*)$"

    def __init__(self, name):
        '''
        Constructor
        '''
        super().__init__(name)
        self.__parameters = []

    def add_parameter(self, parameter):
        self.__parameters.append(parameter)

    def __str__(self):
        result = f"{self._name}{Compat.newline}"

        result += "".join([c + Compat.newline for c in self._comments])
        result += "".join([str(p) for p in self.__parameters])

        return result

    @property
    def name(self):
        m = re.match(SubSection.SUB_SECTION_TITLE, self._name, re.UNICODE)

        return m.group(1).capitalize()

    @property
    def parameters(self):
        return self.__parameters
