#!/usr/bin/env python
try :
    import unicornhat as unicorn
except:
    Exception('unicornhat module not found, please run "sudo pip install unicornhat"')

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

    def isInsideScreen(self, x, y):
        return x < self.width and y < self.height and x >= 0 and y >= 0

    def isPixelAlreadySet(self, x, y, r, g, b):
        if not self.isInsideScreen(x,y):
            return True

        oldR, oldG, oldB = unicorn.get_pixel(x, y)
        return oldR == r and oldG == g and oldB == b

    def setPixel(self, x, y, r, g, b):
        if not self.isInsideScreen(x,y) or self.isPixelAlreadySet(x, y, r, g, b):
            return

        print("[SCREEN] Setting Pixel At " + str(x) + "," + str(y) + " | COLOR : " + str(r) + "," + str(g) + "," + str(b))
        unicorn.set_pixel(x, y, int(r), int(g), int(b))
        unicorn.show()

    def getPixel(self, x, y):
        if not self.isInsideScreen(x, y):
            return
        return unicorn.get_pixel(x, y)
