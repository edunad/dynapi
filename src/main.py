#!/usr/bin/env python
import sys

from managers.screenManager import *
from managers.gameManager import *
from managers.controllerManager import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class Core(object):
    def __init__(self):
        self.screenManager = ScreenManager()
        self.gameMamager = GameManager()
        self.controllerManager = ControllerManager()

    def run(self):
        self.screenManager.draw()

if __name__ == '__main__':
    core = Core()
    core.run()
