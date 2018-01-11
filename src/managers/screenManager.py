#!/usr/bin/env python

import classes.screen

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
    def think():
        print("Hello think")

    @staticmethod
    def draw():
        print("Hello draw")
