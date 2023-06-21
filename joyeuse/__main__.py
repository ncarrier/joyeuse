import sys
from .ui.main_window import MainWindow
from .cube.cube import Cube


def main():
    window = MainWindow()
    cube = Cube(sys.argv[1])
    window.load_cube(cube)

    window.loop()


if __name__ == '__main__':
    main()
