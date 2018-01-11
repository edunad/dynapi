#!/usr/bin/env python

from classes import *
from managers/screenManager import *
from managers/gameManager import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class Core(object):
    def __init__(self):
        print(managers)
        self.screenManager = ScreenManager()
        self.gameMamager = GameManager()

    def run(self):
        self.screenManager.draw()

if __name__ == '__main__':
    core = Core()
    core.run()


import pkgutil
import sys


def load_all_modules_from_dir(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name
                        ).load_module(full_package_name)
            print module


load_all_modules_from_dir('Foo')
