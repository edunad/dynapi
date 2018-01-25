#!/usr/bin/env python3

from gamePad.bitdo import *
from gamePad.buffalo import *
from gamePad.gamepad import *
from events import Events

import asyncio
from concurrent.futures import ProcessPoolExecutor

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
        self.events = Events(('onKeyDown', 'onKeyUp'))

        self.loadControllers()

    async def controllerLoop(self, controller):
        async for event in controller.device.async_read_loop():
            print(event)
            controller.onKeyPress(event)

    def loadControllers(self):
        self.loop = asyncio.get_event_loop()
        executor = ProcessPoolExecutor(1)

        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        controllerId = 1

        for dev in devices:
            controller = self.getDeviceFromName(dev)
            controller.id = controllerId
            print('[REGISTER DEVICE] ' + controller.name + ' -> ID : ' + str(controllerId))

            # Store controller
            self.controllers.append(controller)

            # Register events
            asyncio.ensure_future(self.loop.run_in_executor(executor, self.controllerLoop(controller)))
            controllerId = controllerId + 1


        loop.run_forever()
        print('done')

    def inputHandler(self, data):
        if data['pressed'] :
            self.events.onKeyDown(data)
        else:
            self.events.onKeyUp(data)

    def getDeviceFromName(self, dev):
        if '8Bitdo' in dev.name:
            return BITDO(dev, self.inputHandler)
        elif 'USB,2-axis' in dev.name:
            return BUFFALO(dev, self.inputHandler)
        elif 'usb gamepad' in dev.name:
            return GAMEPAD(dev, self.inputHandler)

    def think(self):
        pass
