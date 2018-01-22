#!/usr/bin/env python3
from .baseController import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class BITDO(BaseController):
    def initDevice(self):
        self.name = '8BITDO controller'

    def onKeyPress(self, keyEvent):
        print(keyEvent)
