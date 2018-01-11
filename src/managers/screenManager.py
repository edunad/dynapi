#!/usr/bin/env python

from classes import *

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
        print "Hello World"

    @staticmethod
    def draw():
        print "Hello World"
