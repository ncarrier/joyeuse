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
from tkinter import Label, Frame, LabelFrame, EW, W, E
from idlelib.tooltip import Hovertip

from joyeuse.ui.input_validation import InputValidation


class SettingsTab(Frame):
    def __init__(self, parent, on_change_handler):
        Frame.__init__(self, parent)
        self.__on_change_handler = on_change_handler

    @staticmethod
    def __get_input_widget(frame, parameter, edit_action):
        validation_obj = InputValidation.get(parameter.name)

        return validation_obj.get_input_widget(frame, parameter.var,
                                               edit_action)

    def __load_parameter(self, frame, parameter, index):
        label = Label(frame, text=parameter.name)
        label.grid(
            column=0,
            row=index,
            sticky=W,
            padx=(3, 3),
            pady=(3, 3)
        )
        widget = SettingsTab.__get_input_widget(
            frame,
            parameter,
            self.__on_change_handler
        )
        widget.grid(column=1, row=index, sticky=E, pady=3, padx=3)
        if len(parameter.comments) > 0:
            Hovertip(label, parameter.comments)
            Hovertip(widget, parameter.comments)

    def __load_cube_sub_section(self, frame, sub_section, index):
        sub_frame = LabelFrame(frame, text=sub_section.name)
        sub_frame.grid(
            row=index,
            column=0,
            sticky=EW,
            padx=(6, 6),
            pady=(6, 6)
        )
        sub_frame.columnconfigure(0, weight=1)
        sub_frame.columnconfigure(1, weight=1)
        if len(sub_section.comments) > 0:
            Hovertip(sub_frame, sub_section.comments)

        # load the parameters
        p_index = 0
        for p in sub_section.parameters:
            self.__load_parameter(sub_frame, p, p_index)
            p_index += 1

    def __load_cube_section(self, section, index):
        frame = LabelFrame(self, text=section.name)
        frame.grid(
            row=index,
            column=0,
            sticky=EW,
            padx=(6, 6),
            pady=(6, 6)
        )
        frame.columnconfigure(0, weight=1)
        if len(section.comments) > 0:
            Hovertip(frame, section.comments)

        # load the sub-sections
        ss_index = 0
        for ss in section.sub_sections:
            self.__load_cube_sub_section(frame, ss, ss_index)
            ss_index += 1

        # load the parameters
        p_index = ss_index
        for p in section.parameters:
            self.__load_parameter(frame, p, p_index)
            p_index += 1

    def load_cube_settings(self, settings):
        index = 0
        for s in settings.sections:
            self.__load_cube_section(s, index)
            index = index + 1
