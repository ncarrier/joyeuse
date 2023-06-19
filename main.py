'''
Created on 18 juin 2023

@author: nicolas
'''
import sys
from joyeuse.settings.settings import Settings

if __name__ == '__main__':
    settings = Settings(sys.argv[1])

    settings.save()

    print(settings)
