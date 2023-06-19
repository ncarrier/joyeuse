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

        self.__tutorials = tutorials = ttk.Frame(nb)
        nb.add(tutorials, text='Tutoriels')

        self.__music = music = ttk.Frame(nb)
        nb.add(music, text='Musiques / histoires')

        self.__settings = settings = ttk.Frame(nb)
        nb.add(settings, text='Paramètres')

        ttk.Label(settings, text="Hello World!").grid(column=0, row=0)
        ttk.Button(settings, text="Quit",
                   command=root.destroy).grid(column=1, row=0)

        self.__sounds = sounds = ttk.Frame(nb)
        nb.add(sounds, text='Bruitages')

        nb.pack(expand=1, fill="both")

    def loop(self):
        self.__root.mainloop()
