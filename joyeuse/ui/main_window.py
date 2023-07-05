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

from tkinter import Tk, ttk, font
import tkinter
from joyeuse.cube.cube import Cube
from joyeuse.misc.log import Log
from joyeuse.ui.settings_tab import SettingsTab
from joyeuse.ui.tutorials_tab import TutorialsTab
from joyeuse.__version__ import __title__ as appname


class MainWindow(object):
    '''
    classdocs
    '''
    __period = 1  # in seconds, used by joyeuse detector and save debouncer

    def __init__(self):
        '''
        Constructor
        '''
        self.__cube = None
        self.__after_identifier = None
        self.__root = Tk(className=appname)
        self.__welcome_message = _("Plug in your Joyeuse :)")
        self.__setup_window()

    def __unload_cube(self):
        self.__notebook.destroy()
        self.__cube = None

    def __joyeuse_detector(self):
        if self.__cube:
            if not self.__cube.valid:
                self.__root.minsize(0, 0)
                self.__unload_cube()
                self.__log_label.config(text=self.__welcome_message)
                # reset geometry, if it was change by hand
                self.__root.geometry("")
                self.__root.resizable(False, False)
        else:
            cube = Cube.get_cube()
            if cube:
                self.load_cube(cube)

                # restrict min size to what's necessary to display all
                self.__root.update()
                self.__root.minsize(self.__root.winfo_width(),
                                    self.__root.winfo_height())
                self.__root.resizable(True, True)

        self.__root.after(1000 * self.__period, self.__joyeuse_detector)

    def __setup_window(self):
        self.__root.title(appname.capitalize())
        self.__root.resizable(False, False)

        self.__log_label = tkinter.Label(self.__root, anchor=tkinter.W,
                                         text=self.__welcome_message)
        self.__log_label.pack(
            side=tkinter.BOTTOM,
            fill=tkinter.X,
            padx=(6, 6),
            pady=(6, 6)
        )
        ft = font.nametofont(self.__log_label["font"]).actual()
        ft = (ft["family"], ft["size"] - 2, "italic")
        self.__log_label.config(font=ft)
        Log.set_log_label(self.__log_label)

        separator = ttk.Separator(self.__root, orient='horizontal')
        separator.pack(fill=tkinter.X, side=tkinter.BOTTOM)

        spacer_label = tkinter.Label(self.__root, font=(0))
        spacer_label.pack(
            side=tkinter.BOTTOM,
            fill=tkinter.BOTH,
            expand=True
        )

    def __setup_notebook(self):
        self.__notebook = notebook = ttk.Notebook(self.__root)
        notebook.pack(
            side=tkinter.TOP,
            anchor=tkinter.NW,
            fill=tkinter.BOTH,
            expand=1,
            padx=(6, 6),
            pady=(6, 6)
        )
        self.__setup_tabs(notebook)

    def __setup_tabs(self, notebook):
        self.__tutorials = tutorials = TutorialsTab(notebook)
        tutorials.pack(fill=tkinter.BOTH, expand=True)
        tutorials.columnconfigure(0, weight=1)
        notebook.add(tutorials, text=_("Tutorials"))

        self.__settings = settings = SettingsTab(
            notebook,
            lambda a, b, c: self.__save_scheduler()
        )
        settings.pack(fill=tkinter.BOTH, expand=True)
        settings.columnconfigure(0, weight=1)
        notebook.add(settings, text=_("Parameters"))

        notebook.pack(expand=1, fill="both")

    def __do_save(self):
        self.__cube.settings.save()
        self.__after_identifier = None

    def __save_scheduler(self):
        if self.__after_identifier is not None:
            self.__root.after_cancel(self.__after_identifier)

        self.__after_identifier = self.__root.after(1000 * self.__period,
                                                    self.__do_save)

    def load_cube(self, cube):
        if cube is not None:
            self.__cube = cube
            self.__setup_notebook()
            self.__settings.load_cube_settings(cube.settings)
            self.__tutorials.load_cube_tutorials(cube.tutorials)
            self.__root.iconphoto(True, cube.icon)
        self.__joyeuse_detector()

    def loop(self):
        self.__root.mainloop()
