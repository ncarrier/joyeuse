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
from textwrap import wrap


class Item(object):
    COLUMNS = 80

    def __init__(self, name):
        '''
        Constructor
        '''
        self._name = name
        self._comments = []

    def add_comment(self, comment):
        self._comments.append(comment)

    @property
    def comments(self):
        comments = ["\n".join(wrap(c, Item.COLUMNS))
                    for c in self._comments
                    if len(c) > 0]

        return "\n".join(comments)

    @property
    def name(self):
        return self._name
