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
from tkinter import IntVar, StringVar, BooleanVar, ttk, Frame


class Setting(object):
    def get_var(self, **kw):
        return self.VAR_KLASS(**kw)


class IntInRangeSetting(Setting):
    '''
    classdocs
    '''
    VAR_KLASS = IntVar

    def __init__(self, lower, upper):
        '''
        Constructor
        '''
        self.__lower = lower
        self.__upper = upper

    def get_value(self, var):
        return str(var.get())

    def get_input_widget(self, parent, var, edit_action):
        var.trace("w", edit_action)
        return ttk.Spinbox(
            parent,
            from_=self.lower,
            to=self.upper,
            textvariable=var
        )

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
    VAR_KLASS = StringVar

    class __SpinboxWithCheckButton(Frame):
        def __init__(self, parent, setting, var, edit_action):
            Frame.__init__(self, parent)
            checked = var.get() != "N"
            int_value = int(var.get()) if checked else setting.lower

            self.__int_var = IntVar(value=int_value)
            self.__int_var.trace("w", edit_action)
            self.__spin_box = ttk.Spinbox(
                self,
                from_=setting.lower,
                to=setting.upper,
                textvariable=self.__int_var
            )
            self.__spin_box.pack(side="right", fill="both")

            self.__boolean_var = BooleanVar(value=checked)
            self.__boolean_var.trace("w", edit_action)
            cb = ttk.Checkbutton(self, var=self.__boolean_var,
                                 command=lambda: self.__check())
            cb.pack(side="left")
            self.__check_button = cb
            self.__check()

        def __check(self):
            state = "disabled" if self.checked else "enabled"
            self.__spin_box.config(state=state)

        @property
        def checked(self):
            return not self.__boolean_var.get()

        @property
        def value(self):
            return self.__int_var.get()

    def get_value(self, _):
        return "N" if self.__widget.checked else str(self.__widget.value)

    def get_input_widget(self, parent, var, edit_action):
        self.__widget = FalseOrIntInRangeSetting.__SpinboxWithCheckButton(
            parent,
            self,
            var,
            edit_action
        )
        return self.__widget


class BoolSetting(Setting):
    '''
    classdocs
    '''
    VAR_KLASS = BooleanVar

    def get_value(self, var):
        return "Y" if var.get() else "N"

    def get_input_widget(self, parent, var, edit_action):
        var.trace("w", edit_action)
        return ttk.Checkbutton(parent, var=var)


class UnknownSetting(Setting):
    VAR_KLASS = StringVar

    def get_value(self, var):
        return var.get()

    def get_input_widget(self, parent, var, edit_action):
        return ttk.Entry(parent, textvariable=var)


class InputValidation():
    # must be kept in sync with the supported parameters in SETTINGS.TXT
    __input_validation = {
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

    @staticmethod
    def get(name):
        return InputValidation.__input_validation.get(name, UnknownSetting())
