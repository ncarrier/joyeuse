'''
Created on 19 juin 2023

@author: nicolas
'''
from tkinter import Tk
from tkinter import ttk


class MainWindow(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__root = root = Tk()
        root.title("Joyeuse")
        self.__notebook = nb = ttk.Notebook(root)

        # TODO move in 3rd position
        self.__settings = settings = ttk.Frame(nb)
        nb.add(settings, text='Paramètres')

        self.__tutorials = tutorials = ttk.Frame(nb)
        nb.add(tutorials, text='Tutoriels')

        self.__music = music = ttk.Frame(nb)
        nb.add(music, text='Musiques / histoires')

        self.__sounds = sounds = ttk.Frame(nb)
        nb.add(sounds, text='Bruitages')

        nb.pack(expand=1, fill="both")

    def __load_cube_sub_section(self, frame, sub_section, index):
        sub_frame = ttk.LabelFrame(frame, text=sub_section.name)
        sub_frame.grid(row=index, column=0)

        # load the parameters
        p_index = 0
        for p in sub_section.parameters:
            ttk.Label(sub_frame, text=f"{p.name} = {p.value}").grid(column=0,
                                                                    row=p_index)
            p_index += 1


    def __load_cube_section(self, section, index):
        frame = ttk.LabelFrame(self.__settings, text=section.name)
        frame.grid(row=index, column=0)

        # load the sub-sections
        ss_index = 0
        for ss in section.sub_sections:
            self.__load_cube_sub_section(frame, ss, ss_index)
            ss_index += 1

        # load the parameters
        p_index = ss_index
        for p in section.parameters:
            ttk.Label(frame, text=f"{p.name} = {p.value}").grid(column=0,
                                                                row=p_index)
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
