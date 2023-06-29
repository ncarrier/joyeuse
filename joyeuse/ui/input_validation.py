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


class IntInRangeSetting(object):
    '''
    classdocs
    '''

    def __init__(self, lower, upper):
        '''
        Constructor
        '''
        self.__lower = lower
        self.__upper = upper

    @property
    def lower(self):
        return self.__lower

    @property
    def upper(self):
        return self.__upper


class FalseOrIntInRangeSetting(IntInRangeSetting):
    '''
    classdocs
    '''


class BoolSetting(object):
    '''
    classdocs
    '''


# must be kept in sync with the supported parameters in the SETTINGS.TXT file
input_validation = {
    "volumeMax": IntInRangeSetting(10, 100),
    "volumePlayFixed": FalseOrIntInRangeSetting(10, 100),
    "volumeOn": IntInRangeSetting(10, 100),
    "volumeOff": IntInRangeSetting(10, 100),
    "nightMode": BoolSetting(),
    # No bounds described in doc, so 1 and 10 are arbitrary
    "nightModeNbFiles": IntInRangeSetting(1, 10),
    "seriesMode": BoolSetting(),
    # No bounds described in doc, so 1 and 10 are arbitrary
    "seriesModeNbFiles": IntInRangeSetting(1, 10),
    "inactivityTimeout": IntInRangeSetting(1, 30),
    "babyStartup": IntInRangeSetting(1, 3),
    "sensitivityStartup": IntInRangeSetting(1, 8),
    "shakeSensitivity": IntInRangeSetting(1, 3),
    "tripleTapActive": BoolSetting(),
    "customFavorites": BoolSetting(),
    "randomMode": BoolSetting()
}
