#!/usr/bin/env python

import unicornhat as unicorn

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class Screen(object):

    def __init__(self, rotation=180, brightness=0.3):
        self.rotation = rotation
        self.brightness = brightness

        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(rotation)
        unicorn.brightness(brightness)

        self.width, self.height = unicorn.get_shape()
        self.screenGrid = {}

    def isInsideScreen(self, x, y):
        return x > self.width or y > self.height or x < 0 or y < 0

    def setPixel(self, x, y, r, g, b):
        if not self.isInsideScreen(x,y):
            return

        unicorn.set_pixel(x, y, int(r), int(g), int(b))
        unicorn.show()

    def getPixel(self, x, y):
        if not self.isInsideScreen(x, y):
            return
        return unicorn.get_pixel(x, y)
