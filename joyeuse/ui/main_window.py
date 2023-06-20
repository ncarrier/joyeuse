'''
Created on 19 juin 2023

@author: nicolas
'''
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
        self.__root.geometry("500x700")
        self.__root.minsize(600, 700)

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

        # load the parameters
        p_index = 0
        for p in sub_section.parameters:
            label = ttk.Label(sub_frame, text=f"{p.name} = {p.value}")
            label.grid(
                column=0,
                row=p_index,
                sticky=tkinter.W,
                padx=(3, 3),
                pady=(3, 3)
            )
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
            label = ttk.Label(frame, text=f"{p.name} = {p.value}")
            label.grid(
                column=0,
                row=p_index,
                sticky=tkinter.W,
                padx=(3, 3),
                pady=(3, 3)
            )
            p_index += 1

    def __load_cube_settings(self, settings):
        index = 0
        for s in settings.sections:
            self.__load_cube_section(s, index)
            index = index + 1

    def load_cube(self, cube):
        self.__load_cube_settings(cube.settings)

    def loop(self):
        self.__root.mainloop()
