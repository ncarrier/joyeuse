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
import glob
from PIL import ImageTk

from joyeuse.settings.settings import Settings
from joyeuse.misc.log import Log
from joyeuse.misc.compat import Compat
from joyeuse.cube.info import Info


class Cube(object):
    '''
    classdocs
    '''
    EXTRA_LOCATIONS = []

    @staticmethod
    def __get_search_locations():
        return (
            # passed by parameter
            Cube.EXTRA_LOCATIONS +
            # os specific
            Compat.get_os_mount_search_path()
        )

    @staticmethod
    def get_cube():
        cube = None
        for loc in Cube.__get_search_locations():
            try:
                cube = Cube(loc)
                Log.log(f"Detected joyeuse in {loc}")
                break
            except (AttributeError, FileNotFoundError):
                pass

        return cube

    @classmethod
    def add_extra_location(cls, location):
        cls.EXTRA_LOCATIONS.append(location)

    def __init__(self, path):
        self.__path = path
        self.__settings = Settings(f"{path}/Secrets/SETTINGS.txt")
        self.__icon = ImageTk.PhotoImage(file=fr"{path}/joyeuse.ico")
        self.__info = Info(f"{path}/Secrets/info.js")

    @property
    def valid(self):
        return os.path.exists(f"{self.__path}/Secrets/SETTINGS.txt")

    @property
    def settings(self):
        return self.__settings

    @property
    def tutorials(self):
        return glob.glob(f"{self.__path}/Secrets/Tutos vidéo/*.mp4")

    @property
    def icon(self):
        return self.__icon
