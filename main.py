#!/usr/bin/env python3
'''
Created on 18 juin 2023

@author: nicolas
'''
import sys
from joyeuse.ui.main_window import MainWindow
from joyeuse.cube.cube import Cube

if __name__ == '__main__':
    window = MainWindow()
    cube = Cube(sys.argv[1])
    window.load_cube(cube)

    window.loop()
