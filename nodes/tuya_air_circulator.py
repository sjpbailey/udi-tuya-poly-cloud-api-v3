"""
Polyglot v3 node server
Copyright (C) 2023 Steven Bailey
MIT License
Version 3.0.1 Jun 2023
"""
import asyncio
import colorsys
import udi_interface
import time
import json
from tuya_bulb_control import Bulb
from tuya_connector import (
    TuyaOpenAPI,)


LOGGER = udi_interface.LOGGER


class AirCirNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, new_id, deviceid, apiAccessId, apiSecret, apiEndpoint, apiRegion):
        super(AirCirNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.new_id = new_id
        self.deviceid = deviceid
        self.DEVICEAIR_ID = deviceid
        self.apiAccessId = apiAccessId
        self.ACCESS_ID = apiAccessId
        self.apiSecret = apiSecret
        self.ACCESS_KEY = apiSecret
        self.apiEndpoint = apiEndpoint
        self.API_ENDPOINT = apiEndpoint
        self.apiRegion = apiRegion
        self.API_REGION = apiRegion
        self.SwStat(self)
        self.setDriver('ST', 1)
        # LOGGER.info('{name}\n{id_new}\n{ip}\n{key}\n'.format(
        # name=name, id_new=id_new, ip=ip, key=key,))

    # Fan On
    def setSwOn(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEAIR_ID = self.DEVICEAIR_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch', 'value': True}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
        time.sleep(.1)
        self.SwStat(self)

    # Fan Off
    def setSwOff(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEAIR_ID = self.DEVICEAIR_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch', 'value': False}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
        time.sleep(.1)
        self.SwStat(self)


    # Set Modes
    def modeOn(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEAIR_ID = self.DEVICEAIR_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.modeOn = int(command.get('value'))
        self.setDriver('GV4', self.modeOn)
        # Colour
        if self.modeOn == 0:
            commands = {'commands': [{'code': 'mode', 'value': 'fresh'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            LOGGER.info('Colour')
            time.sleep(.1)
            self.SwStat(self)
        else:
            pass
        # Scene
        """elif self.modeOn == 1:
            commands = {'commands': [{'code': 'work_mode', 'value': 'scene'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            LOGGER.info('Scene')
            time.sleep(.1)
            self.SwStat(self)
        
        ### Future
        # Music
        elif self.modeOn == 2:
            commands = {'commands': [{'code': 'work_mode', 'value': 'music'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            time.sleep(.5)
            self.SwStat(self)"""
        

    # Set Fan
    def setFan(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEAIR_ID = self.DEVICEAIR_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.setClr = int(command.get('value'))
        self.setDriver('GV5', self.setClr)
        
        # Speed 1
        if self.setClr == 0:
            LOGGER.info('Speed 1')
            commands = {'commands': [{'code': "fan_speed", 'value': '1'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            # (255, 0, 0)
            LOGGER.info('Speed 1')
            time.sleep(.1)
            self.SwStat(self)
        # Speed 2
        elif self.setClr == 1:
            LOGGER.info('Speed 2')
            commands = {'commands': [{'code': "fan_speed", 'value': '1'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            # (255, 0, 0)
            LOGGER.info('Speed 2')
            time.sleep(.1)
            self.SwStat(self)
        # Speed 3
        elif self.setClr == 2:
            LOGGER.info('Speed 3')
            commands = {'commands': [{'code': "fan_speed", 'value': '1'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            # (255, 0, 0)
            LOGGER.info('Speed 3')
            time.sleep(.1)
            self.SwStat(self)
        # Speed 4
        elif self.setClr == 3:
            LOGGER.info('Speed 4')
            commands = {'commands': [{'code': "fan_speed", 'value': '1'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            # (255, 0, 0)
            LOGGER.info('Speed 4')
            time.sleep(.1)
            self.SwStat(self)
        else:
            pass

    """# Led Level
    def setDim(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEAIR_ID = self.DEVICEAIR_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.SwStat(self)

        ivr_one = 'percent'
        percent = int(command.get('value'))

        def set_percent(self, command):
            percent = int(command.get('value')*10)
        if percent < 1 or percent > 100:
            LOGGER.error('Invalid Level {}'.format(percent))
        else:
            commands = {'commands': [
                {'code': 'bright_value_v2', 'value': int(percent)*10}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICEAIR_ID), commands)
            self.setDriver('GV3', percent)
            LOGGER.info('Dimmer Setpoint = ' + str(percent) + ' Level')"""

    def SwStat(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICEAIR_ID = self.DEVICEAIR_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        response1 = openapi.get(
            "/v1.0/iot-03/devices/{}".format(DEVICEAIR_ID) + "/status/")  # DEVICE_ID
        LOGGER.info(response1)
        for i in response1['result'][0:1]:
            # LOGGER.info(i['value'])
            if i['value'] == True:
                self.setDriver('GV2', 1)
            elif i['value'] == False:
                self.setDriver('GV2', 0)
        for i in response1['result'][2:3]:
            #self.setDriver('GV3', i['value']/10)
            LOGGER.info(i['value']/10)

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            self.SwStat(self)
            self.query(self)
            LOGGER.debug('shortPoll (node)')

    def query(self, command=None):
        self.SwStat(self)
        self.reportDrivers()

    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2, 'name': 'Online'},
        {'driver': 'GV2', 'value': 0, 'uom': 2, 'name': 'Switch Status'},
        #{'driver': 'GV3', 'value': 0, 'uom': 51, 'name': 'Light Level'},
        {'driver': 'GV4', 'value': 0, 'uom': 25, 'name': 'Light Command'},
        {'driver': 'GV5', 'value': 0, 'uom': 25, 'name': 'Fan Speed'},

    ]

    id = 'aircir'

    commands = {
        'LGTON': setSwOn,
        'LGTOF': setSwOff,
        'LGTCL': setFan,
        #'LGTCFLIP': setclrflip,
        'MODE': modeOn,
        #'STLVL': setDim,
        'QUERY': query,
    }


