#!/usr/bin/env python

from gamePad.controllerBase import *
from evdev import InputDevice, categorize, ecodes, KeyEvent

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class ControllerManager(object):

    def __init__(self):
        self.devices = {}
        self.controllers = []

        #self.loadControllers()

    def loadControllers(self):
        self.devices = map(InputDevice,('/dev/input/event0','/dev/input/event1'))
        self.devices = {dev.fd: dev for dev in self.devices}
        for dev in devices.values():
            if '8Bitdo' in dev.name:
                self.controllers.append()
            else if 'USB,2-axis' in dev.name:
                self.controllers.append()

    @classmethod
    def think(self):
        print("Hello think")
