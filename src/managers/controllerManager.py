#!/usr/bin/env python3

from gamePad.bitdo import *
from gamePad.buffalo import *
from gamePad.gamepad import *

import asyncio
import evdev

"""
#################
# The Functions #
######################################
## Global file with all the functions.
######################################
"""

class ControllerManager(object):

    def __init__(self):
        self.controllers = []
        self.loadControllers()

    async def controllerLoop(self, controller):
        async for event in controller.device.async_read_loop():
            controller.onKeyPress(event)

    def loadControllers(self):
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for dev in devices:
            controller = self.getDeviceFromName(dev)
            print('[REGISTER DEVICE] ' + controller.name)

            # Store controller
            self.controllers.append(controller)

            # Register events
            asyncio.ensure_future(self.controllerLoop(controller))

        loop = asyncio.get_event_loop()
        loop.run_forever()

    def getDeviceFromName(self, dev):
        if '8Bitdo' in dev.name:
            return BITDO(dev)
        elif 'USB,2-axis' in dev.name:
            return BUFFALO(dev)
        elif 'usb gamepad' in dev.name:
            return GAMEPAD(dev)

    def think(self):
        pass
