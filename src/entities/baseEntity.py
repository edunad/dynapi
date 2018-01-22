#!/usr/bin/env python3

from managers.gameManager import *
from abc import ABCMeta, abstractmethod

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class BaseEntity(object):
    __metaclass__ = ABCMeta

    def __init__(self, id=-1, sprite='#000'):
        self.id = id
        self.sprite = sprite

    @abstractmethod
    def onDamage(self):
        return "ENTITY DAMAGE CALL"

    @abstractmethod
    def update(self):
        return "ENTITY UPDATE CALL"

    @abstractmethod
    def draw(self):
        return "ENTITY DRAW CALL"
