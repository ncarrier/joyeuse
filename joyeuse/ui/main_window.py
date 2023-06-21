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


class MainWindow(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__root = Tk()
        self.__setup_window()
        self.__setup_notebook()

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
        # TODO move in 3rd position
        self.__settings = settings = ttk.Frame(notebook)
        self.__settings.pack(
            fill=tkinter.BOTH,
            expand=True,
            anchor=tkinter.CENTER
        )
        notebook.add(settings, text='Paramètres')

        self.__tutorials = tutorials = ttk.Frame(notebook)
        notebook.add(tutorials, text='Tutoriels')

        self.__music = music = ttk.Frame(notebook)
        notebook.add(music, text='Musiques / histoires')

        self.__sounds = sounds = ttk.Frame(notebook)
        notebook.add(sounds, text='Bruitages')

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
            label = ttk.Label(sub_frame, text=p.name)
            label.grid(
                column=0,
                row=p_index,
                sticky=tkinter.W,
                padx=(3, 3),
                pady=(3, 3)
            )
            p.var.trace("w", lambda a, b, c: self.__cube.settings.save())
            entry = ttk.Entry(sub_frame,
                              textvariable=p.var)
            entry.grid(column=1, row=p_index, sticky=tkinter.EW, pady=3,
                       padx=3)
            if len(p.comments) > 0:
                Hovertip(label, p.comments)
                Hovertip(entry, p.comments)
            p_index += 1

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
            label = ttk.Label(frame, text=p.name)
            label.grid(
                column=0,
                row=p_index,
                sticky=tkinter.W,
                padx=(3, 3),
                pady=(3, 3)
            )
            entry = ttk.Entry(frame,
                              textvariable=p.var)
            p.var.trace("w", lambda a, b, c: self.__cube.settings.save())
            entry.grid(column=1, row=p_index, sticky=tkinter.EW, pady=3,
                       padx=3)
            if len(p.comments) > 0:
                Hovertip(label, p.comments)
                Hovertip(entry, p.comments)
            p_index += 1

    def __load_cube_settings(self, settings):
        index = 0
        for s in settings.sections:
            self.__load_cube_section(s, index)
            index = index + 1

    def load_cube(self, cube):
        self.__cube = cube
        self.__load_cube_settings(cube.settings)

    def loop(self):
        self.__root.mainloop()
