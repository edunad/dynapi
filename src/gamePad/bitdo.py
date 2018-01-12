#!/usr/bin/env python
from baseController import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class BITDO(BaseController):
    def onKeyPress(self, keyEvent):
        print('BITDO HANDLE')
        super(BaseController, self).onKeyPress()
