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

from tkinter import Tk
from tkinter import ttk
from idlelib.tooltip import Hovertip
import tkinter
from joyeuse.cube.cube import Cube
from joyeuse.ui.input_validation import InputValidation


class MainWindow(object):
    '''
    classdocs
    '''
    __period = 1  # in seconds

    def __init__(self):
        '''
        Constructor
        '''
        self.__cube = None
        self.__root = Tk(className='joyeuse')
        self.__setup_window()

    def __unload_cube(self):
        self.__notebook.destroy()
        self.__cube = None

    def __joyeuse_detector(self):
        if self.__cube:
            if not self.__cube.valid:
                self.__unload_cube()
        else:
            cube = Cube.get_cube()
            if cube:
                self.load_cube(cube)

        self.__root.after(1000 * self.__period, self.__joyeuse_detector)

    def __setup_window(self):
        self.__root.title("Joyeuse")
        self.__root.resizable(False, False)

    def __setup_notebook(self):
        self.__notebook = notebook = ttk.Notebook(self.__root)
        notebook.pack(
            side=tkinter.TOP,
            anchor=tkinter.NW,
            fill=tkinter.BOTH,
            expand=1,
            padx=(6, 6),
            pady=(6, 0)
        )
        self.__setup_tabs(notebook)

    def __setup_tabs(self, notebook):
        self.__settings = settings = ttk.Frame(notebook)
        self.__settings.pack(
            fill=tkinter.BOTH,
            expand=True,
            anchor=tkinter.CENTER
        )
        notebook.add(settings, text='Paramètres')

        notebook.pack(expand=1, fill="both")

    def __load_cube_sub_section(self, frame, sub_section, index):
        sub_frame = ttk.LabelFrame(frame, text=sub_section.name)
        sub_frame.grid(row=index, column=0, sticky=tkinter.EW,
                       padx=(6, 6), pady=(6, 6))
        if len(sub_section.comments) > 0:
            Hovertip(sub_frame, sub_section.comments)

        # load the parameters
        p_index = 0
        for p in sub_section.parameters:
            self.__load_parameter(sub_frame, p, p_index)
            p_index += 1

    def __get_input_widget(self, frame, parameter, edit_action):
        validation_obj = InputValidation.get(parameter.name)

        return validation_obj.get_input_widget(frame, parameter.var,
                                               edit_action)

    def __load_parameter(self, frame, parameter, index):
        label = ttk.Label(frame, text=parameter.name)
        label.grid(
            column=0,
            row=index,
            sticky=tkinter.W,
            padx=(3, 3),
            pady=(3, 3)
        )
        widget = self.__get_input_widget(
            frame,
            parameter,
            lambda a, b, c: self.__cube.settings.save()
        )
        widget.grid(column=1, row=index, sticky=tkinter.EW, pady=3, padx=3)
        if len(parameter.comments) > 0:
            Hovertip(label, parameter.comments)
            Hovertip(widget, parameter.comments)

    def __load_cube_section(self, section, index):
        frame = ttk.LabelFrame(self.__settings, text=section.name)
        frame.grid(
            row=index,
            column=0,
            sticky=tkinter.EW,
            padx=(6, 6),
            pady=(6, 6)
        )
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

    def __load_cube_settings(self, settings):
        index = 0
        for s in settings.sections:
            self.__load_cube_section(s, index)
            index = index + 1

    def load_cube(self, cube):
        if cube is not None:
            self.__cube = cube
            self.__setup_notebook()
            self.__load_cube_settings(cube.settings)
            self.__root.iconphoto(True, cube.icon)
        self.__joyeuse_detector()

    def loop(self):
        self.__root.mainloop()
