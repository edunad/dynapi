#!/usr/bin/env python3
from .baseController import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class BUFFALO(BaseController):
    def initDevice(self):
        self.name = 'Buffalo controller'

    def onKeyPress(self, keyEvent):
        print(keyEvent)
