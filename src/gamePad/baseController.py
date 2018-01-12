#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class BaseController(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def onKeyPress(self, keyEvent):
        print('AUCH')
        #pass
