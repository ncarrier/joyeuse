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


class Log(object):
    LOG_LABEL = None

    @classmethod
    def set_log_label(cls, log_label):
        cls.LOG_LABEL = log_label

    @classmethod
    def log(cls, message):
        if cls.LOG_LABEL is not None:
            cls.LOG_LABEL.config(text=message)
        print(message)
