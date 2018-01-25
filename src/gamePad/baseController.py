#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod
import evdev

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class BaseController(object):
    __metaclass__ = ABCMeta

    def __init__(self, device, handler):
        self.name = 'UNKNOWN'
        self.id = -1
        self.device = device
        self.inputHandler = handler
        self.DEBUG_MODE = False

        self.keys = {
            'buttons': {},
            'arrows': []
        }
        self.pressingArrows = {};

        # Get keys and name
        self.defineController()

    @abstractmethod
    def defineController(self):
        pass

    def onKeyPress(self, keyEvent):
        if self.DEBUG_MODE :
            print(keyEvent)

        if keyEvent.type == 1:
            # Handle buttons
            for btnKey in self.keys['buttons']:
                if self.keys['buttons'][btnKey] == keyEvent.code:
                    pressed = keyEvent.value == 1
                    self.inputHandler({'key': btnKey, 'pressed': pressed})

        elif keyEvent.type == 3:
            # Handle arrows
            for arrow in self.keys['arrows']:
                if arrow['code'] == keyEvent.code:
                    if arrow['value'] == keyEvent.value:
                        self.inputHandler({'cntId': self.id, 'key': arrow['id'], 'pressed': True})
                        self.pressingArrows[arrow['id']] = True
                    elif keyEvent.value == arrow['reset'] and arrow['id'] in self.pressingArrows:
                        self.inputHandler({'cntId': self.id, 'key': arrow['id'], 'pressed': False})
                        del self.pressingArrows[arrow['id']]
