#!/usr/bin/env python3

from classes.screen import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class ScreenManager(object):
    def __init__(self):
        self.screen = Screen();

    def think(self):
        pass

    def draw(self):
        self.screen.setPixel(0, 0, 255, 255, 0)
