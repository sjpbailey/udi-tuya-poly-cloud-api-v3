"""
Polyglot v3 node server
Copyright (C) 2023 Steven Bailey
MIT License
Version 1.0.1 July 2023
"""
import asyncio
import udi_interface
import time
import json
import logging
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
    TUYA_LOGGER,)

LOGGER = udi_interface.LOGGER


class PirDNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, new_id, deviceid, apiAccessId, apiSecret, apiEndpoint):
        super(PirDNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.new_id = new_id
        self.deviceid = deviceid
        self.DEVICESW_ID = deviceid
        self.apiAccessId = apiAccessId
        self.ACCESS_ID = apiAccessId
        self.apiSecret = apiSecret
        self.ACCESS_KEY = apiSecret
        self.apiEndpoint = apiEndpoint
        self.API_ENDPOINT = apiEndpoint
        self.name = name
        self.DEVICE_NAME = name
        self.setDriver('ST', 1)
        

    def SwStat(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        time.sleep(2)
        self.BtStat(self)

        response1 = openapi.get(
            "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")
        LOGGER.info(self.name)
        LOGGER.info(response1)
        for i in response1['result'][0:1]:
            if i['value'] == True:
                #LOGGER.info('PIR Trip {}'.format(i['value']))
                self.setDriver('GV2', 1)
            elif i['value'] == False:
                #LOGGER.info('PIR Normal {}'.format(i['value']))
                self.setDriver('GV2', 0)
    
    def BtStat(self, command):
        API_ENDPOINT = self.API_ENDPOINT
        ACCESS_ID = self.ACCESS_ID
        ACCESS_KEY = self.ACCESS_KEY
        DEVICESW_ID = self.DEVICESW_ID
        DEVICE_NAME = self.DEVICE_NAME
        openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        openapi.connect()
        response1 = openapi.get(
            "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")
        LOGGER.info(DEVICE_NAME)
        LOGGER.info(response1)
        for i in response1['result'][1:2]:
            LOGGER.info(i['value'])
            self.setDriver('GV3', i['value'])
    
    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            self.SwStat(self)
            LOGGER.debug('shortPoll (node)')

    def query(self, command=None):
        self.SwStat(self)
        self.BtStat(self)
        self.reportDrivers()

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 2},
        {'driver': 'GV2', 'value': 0, 'uom': 2},
        {'driver': 'GV3', 'value': 0, 'uom': 51},
    ]

    id = 'pirmd'

    commands = {
        'QUERY': query
    }
