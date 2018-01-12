#!/usr/bin/env python

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

    @staticmethod
    def think(self):
        print("Hello think")

    @staticmethod
    def draw(self):
        self.screen.setPixel(0, 0, 255, 255, 0)
        print("Hello draw")
