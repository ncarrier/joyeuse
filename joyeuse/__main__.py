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

import sys
from .ui.main_window import MainWindow
from .cube.cube import Cube
from .i18n.i18n import I18n

if getattr(sys, "frozen", False):
    import pyi_splash

def usage(status):
    print(_("Usage: joyeuse [/path/to/joyeuse]"))
    sys.exit(status)


def main():
    I18n.init()
    if len(sys.argv) not in [1, 2]:
        usage(1)

    if len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help", "-?"]:
        usage(0)

    window = MainWindow()
    cube = None
    if len(sys.argv) == 2:
        Cube.add_extra_location(sys.argv[1])
    window.load_cube(cube)

    if getattr(sys, "frozen", False):
        pyi_splash.close()
    window.loop()


if __name__ == '__main__':
    main()
