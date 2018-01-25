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
    def defineController(self):
        self.name = '8BITDO controller'
        
        self.keys['buttons'] = {
            'Y': 308,
            'X': 307,
            'A': 304,
            'B': 305,
            'R1': 311,
            'L1': 310,
            'START': 315,
            'SELECT': 314
        }

        self.keys['arrows'] = [
            {'id': 'UP', 'value': 0, 'code': 1, 'reset': 127},
            {'id': 'DOWN', 'value': 255, 'code': 1, 'reset': 127},
            {'id': 'LEFT', 'value': 255, 'code': 0, 'reset': 127},
            {'id': 'RIGHT', 'value': 0, 'code': 0, 'reset': 127},
        ]
