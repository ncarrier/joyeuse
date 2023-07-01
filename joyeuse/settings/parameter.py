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
from joyeuse.ui.input_validation import InputValidation
from joyeuse.misc.compat import Compat


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
        self.__validation = InputValidation.get(name)
        self.__var = self.__validation.get_var(value=value)

    def add_comment(self, comment):
        self.__comments.append(comment)

    def __str__(self):
        result = f"{self.__name}:{self.value} {30 * '<'}{Compat.newline}"

        result += "".join([c + Compat.newline for c in self.__comments])

        return result

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        value = self.__validation.get_value(self.__var)
        return value

    @property
    def comments(self):
        return "\n".join([c for c in self.__comments if len(c) > 0])

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var):
        self.__var = var
