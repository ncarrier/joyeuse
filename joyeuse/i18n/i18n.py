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
import gettext
import os

from joyeuse.__version__ import __title__ as appname


class I18n(object):
    @staticmethod
    def init(languages=None):
        module_dir = os.path.dirname(__file__)
        localedir = f"{module_dir}/locales"
        en_i18n = gettext.translation(appname, localedir, fallback=True,
                                      languages=languages)
        en_i18n.install()
