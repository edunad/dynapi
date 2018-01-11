#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from baseEntity import *

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class Player(BaseEntity):
    def draw(self):
        super(BaseEntity, self).draw()
