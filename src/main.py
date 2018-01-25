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
        self.gameManager = GameManager()
        self.controllerManager = ControllerManager()
        self.controllerManager.events.onKeyUp += self.keyUpTest

    def keyUpTest(self, data):
        print('key up event! HUZAH')
        print(data)

    def think(self):
        self.gameManager.think()
        self.screenManager.think()
        self.controllerManager.think()

    def draw(self):
        self.gameManager.draw()
        self.screenManager.draw()

    def run(self):
        while True:
            self.think()
            self.draw()


if __name__ == '__main__':
    core = Core()
    core.run()
