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
from enum import Enum, auto
import string


class Os(Enum):
    LINUX = auto()
    WINDOWS = auto()


class Compat(object):
    OS = Os.WINDOWS if os.name == "nt" else Os.LINUX
    newline = '\r\n' if OS == Os.LINUX else '\n'

    @staticmethod
    def __get_subdirs(a_dir):
        full_paths = [os.path.join(a_dir, name) for name in os.listdir(a_dir)]
        return [path for path in full_paths if os.path.isdir(path)]

    @staticmethod
    def get_os_mount_search_path():
        if Compat.OS == Os.LINUX:
            return Compat.__get_subdirs(f"/media/{os.getlogin()}")
        else:
            return [f"{d}:" for d in string.ascii_uppercase
                    if os.path.exists(f"{d}:")]
