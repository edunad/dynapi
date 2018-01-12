#!/usr/bin/env python
import sys

import managers.screenManager
import managers.gameManager

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

    def run(self):
        self.screenManager.draw()

if __name__ == '__main__':
    core = Core()
    core.run()
