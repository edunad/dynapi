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

    def __init__(self, device):
        self.name = 'UNKNOWN'
        self.device = device
        self.initDevice()

    @abstractmethod
    def initDevice(self):
        pass

    @abstractmethod
    def onKeyPress(self, keyEvent):
        pass
