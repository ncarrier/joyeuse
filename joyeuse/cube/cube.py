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
from PIL import ImageTk

from joyeuse.settings.settings import Settings


class Cube(object):
    '''
    classdocs
    '''

    def __init__(self, path):
        '''
        Constructor
        '''
        self.__settings = Settings(f"{path}/Secrets/SETTINGS.txt")
        self.__icon = ImageTk.PhotoImage(file=fr"{path}/joyeuse.ico")

    @property
    def settings(self):
        return self.__settings

    @property
    def icon(self):
        return self.__icon
