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
from joyeuse.settings.item import Item


class Parameter(Item):
    '''
    classdocs
    '''
    def __init__(self, name, value, suffix):
        '''
        Constructor
        '''
        super().__init__(name)
        self.__value = value
        self.__validation = InputValidation.get(name)
        self.__var = self.__validation.get_var(value=value)
        self.__suffix = suffix

    def __str__(self):
        result = f"{self.name}:{self.value} {self.__suffix}{Compat.newline}"

        result += "".join([c + Compat.newline for c in self._comments])

        return result

    @property
    def value(self):
        value = self.__validation.get_value(self.__var)
        return value

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var):
        self.__var = var
