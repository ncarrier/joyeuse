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
import os
import string
from PIL import ImageTk

from joyeuse.settings.settings import Settings


class Cube(object):
    '''
    classdocs
    '''

    @staticmethod
    def __get_subdirs(a_dir):
        full_paths = [os.path.join(a_dir, name) for name in os.listdir(a_dir)]
        return [path for path in full_paths if os.path.isdir(path)]

    @staticmethod
    def __get_search_locations():
        return (
            # linux
            Cube.__get_subdirs(f"/media/{os.getlogin()}") +
            # windows
            [f"{d}" for d in string.ascii_uppercase if os.path.exists(f"{d}:")]
        )

    @staticmethod
    def get_cube():
        cube = None
        for loc in Cube.__get_search_locations():
            try:
                cube = Cube(loc)
                print(f"detected joyeuse in {loc}")
                break
            except (AttributeError, FileNotFoundError):
                pass

        return cube

    def __init__(self, path):
        '''
        Constructor
        '''
        self.__path = path
        self.__settings = Settings(f"{path}/Secrets/SETTINGS.txt")
        self.__icon = ImageTk.PhotoImage(file=fr"{path}/joyeuse.ico")

    @property
    def valid(self):
        return os.path.exists(f"{self.__path}/Secrets/SETTINGS.txt")

    @property
    def settings(self):
        return self.__settings

    @property
    def icon(self):
        return self.__icon
