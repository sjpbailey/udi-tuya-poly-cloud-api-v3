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


class LightNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, new_id, deviceid, apiAccessId, apiSecret, apiEndpoint, apiRegion):
        super(LightNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.new_id = new_id
        self.deviceid = deviceid
        self.DEVICELED_ID = deviceid
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

    # Light On
    def setSwOn(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICELED_ID = self.DEVICELED_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_led', 'value': True}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
        time.sleep(.1)
        self.SwStat(self)

    # Light Off
    def setSwOff(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICELED_ID = self.DEVICELED_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        commands = {'commands': [{'code': 'switch_led', 'value': False}]}
        openapi.post(
            '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
        time.sleep(.1)
        self.SwStat(self)


    # Set Modes
    def modeOn(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICELED_ID = self.DEVICELED_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.modeOn = int(command.get('value'))
        self.setDriver('GV4', self.modeOn)
        # Colour
        if self.modeOn == 0:
            commands = {'commands': [{'code': 'work_mode', 'value': 'colour'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            LOGGER.info('Colour')
            time.sleep(.1)
            self.SwStat(self)
        # Scene
        elif self.modeOn == 1:
            commands = {'commands': [{'code': 'work_mode', 'value': 'scene'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            LOGGER.info('Scene')
            time.sleep(.1)
            self.SwStat(self)
        elif self.setClr == 15:
            commands = {'commands': [{'code': 'work_mode', 'value': 'white'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            LOGGER.info('White Colour')
            time.sleep(.1)
            self.SwStat(self)
        elif self.modeOn == 2:
            commands = {'commands': [{'code': 'work_mode', 'value': 'music'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            time.sleep(.5)
            self.SwStat(self)
        else:
            pass
        

    """# Set Color
    def setClr(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICELED_ID = self.DEVICELED_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        self.setClr = int(command.get('value'))
        self.setDriver('GV5', self.setClr)
        
        # Soft White
        if self.setClr == 0:
            LOGGER.info('colour_data_v2')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":0,\"s\":1000,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (255, 0, 0)
            LOGGER.info('Red High')
            time.sleep(.1)
            self.SwStat(self)
        # Red Low
        if self.setClr == 1:
            LOGGER.info('colour_data_v2')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":0,\"s\":1000,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (255, 0, 0)
            LOGGER.info('Red Low')
            time.sleep(.1)
            self.SwStat(self)
        # Orange High
        elif self.setClr == 2:
            LOGGER.info('colour_data_V2' 'Orange')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":29,\"s\":1000,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (255, 127, 0)
            LOGGER.info('Orange High')
            time.sleep(.1)
            self.SwStat(self)
        # Orange low
        elif self.setClr == 3:
            LOGGER.info('colour_data_V2' 'Orange')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":29,\"s\":1000,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (255, 127, 0)
            LOGGER.info('Orange Low')
            time.sleep(.1)
            self.SwStat(self)    
        # Yellow High
        elif self.setClr == 4:
            LOGGER.info('colour_data_v2' 'Yellow')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":47,\"s\":1000,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (255, 200, 0)
            LOGGER.info('Yellow High')
            time.sleep(.1)
            self.SwStat(self)
        # Yellow Low
        elif self.setClr == 5:
            LOGGER.info('colour_data_v2' 'Yellow')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":47,\"s\":1000,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (255, 200, 0)
            LOGGER.info('Yellow Low')
            time.sleep(.1)
            self.SwStat(self)
        # Green High
        elif self.setClr == 6:
            LOGGER.info('colour_data_v2' 'green')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":120,\"s\":1000,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (0, 255, 0)
            LOGGER.info('Green High')
            time.sleep(.1)
            self.SwStat(self)
        # Green Low
        elif self.setClr == 7:
            LOGGER.info('colour_data_v2' 'green')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":120,\"s\":1000,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (0, 255, 0)
            LOGGER.info('Green Low')
            time.sleep(.1)
            self.SwStat(self)
        # Blue High
        elif self.setClr == 8:
            LOGGER.info('colour_data_v2' 'Blue')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":240,\"s\":1000,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (0, 0, 255)
            LOGGER.info('Blue High')
            time.sleep(.1)
            self.SwStat(self)
        # Blue Low
        elif self.setClr == 9:
            LOGGER.info('colour_data_v2' 'Blue')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":240,\"s\":1000,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (0, 0, 255)
            LOGGER.info('Blue Low')
            time.sleep(.1)
            self.SwStat(self)
        # Indigo High
        elif self.setClr == 10:
            LOGGER.info('colour_data_v2' 'Indigo')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":243,\"s\":547,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (46, 43, 95)
            LOGGER.info('Indigo High')
            time.sleep(.1)
            self.SwStat(self)
        # Indigo Low
        elif self.setClr == 11:
            LOGGER.info('colour_data_v2' 'Indigo')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":243,\"s\":547,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (46, 43, 95)
            LOGGER.info('Indigo Low')
            time.sleep(.1)
            self.SwStat(self)
        # Violet High
        elif self.setClr == 12:
            LOGGER.info('colour_data_v2' 'Violet')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":272,\"s\":1000,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (139, 0, 255)
            LOGGER.info('Violet High')
            time.sleep(.1)
            self.SwStat(self)
        # Violet Low
        elif self.setClr == 13:
            LOGGER.info('colour_data_v2' 'Violet')
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":272,\"s\":1000,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            # (139, 0, 255)
            LOGGER.info('Violet low')
            time.sleep(.1)
            self.SwStat(self)
        # White WorkMode
        elif self.setClr == 14:
            commands = {'commands': [{'code': 'work_mode', 'value': 'white'}]}
            #commands = {'commands': [
            #    {'code': 'colour_data_v2', 'value': '{\"h\":118,\"s\":45,\"v\":10}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            LOGGER.info('White')
            time.sleep(.1)
            self.SwStat(self)
            # White Colour
        elif self.setClr == 15:
            #commands = {'commands': [{'code': 'work_mode', 'value': 'white'}]}
            commands = {'commands': [
                {'code': 'colour_data_v2', 'value': '{\"h\":118,\"s\":45,\"v\":1000}'}]}
            openapi.post(
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            LOGGER.info('White Colour')
            time.sleep(.1)
            self.SwStat(self)
        else:
            pass"""

    # Led Level
    def setDim(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICELED_ID = self.DEVICELED_ID
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
                '/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
            self.setDriver('GV3', percent)
            LOGGER.info('Dimmer Setpoint = ' + str(percent) + ' Level')

    def SwStat(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICELED_ID = self.DEVICELED_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()

        response1 = openapi.get(
            "/v1.0/iot-03/devices/{}".format(DEVICELED_ID) + "/status/")  # DEVICE_ID
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
        {'driver': 'GV3', 'value': 0, 'uom': 51, 'name': 'Light Level'},
        {'driver': 'GV4', 'value': 0, 'uom': 25, 'name': 'Light Command'},
        #{'driver': 'GV5', 'value': 0, 'uom': 25, 'name': 'Light Colour'},

    ]

    id = 'lightsl20'

    commands = {
        'LGTON': setSwOn,
        'LGTOF': setSwOff,
        #'LGTCL': setClr,
        #'LGTCFLIP': setclrflip,
        'MODE': modeOn,
        'STLVL': setDim,
        'QUERY': query,
    }

