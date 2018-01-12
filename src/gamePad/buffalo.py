#!/usr/bin/env python
from baseController import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class BUFFALO(BaseController):
    def onKeyPress(self, keyEvent):
        print('BUFFALO HANDLE')
        super(BaseController, self).onKeyPress()
