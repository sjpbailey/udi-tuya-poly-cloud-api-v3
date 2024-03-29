"""
Polyglot v3 node server
Copyright (C) 2023 Steven Bailey
MIT License
This node server polls Tuya TreatLife LED's and Switches for
API control via GET and POST
Version 3.0.1 Jun 2023
Version 3.0.1 Jun 2023
"""
import udi_interface
import time
import json
from tuya_connector import (
    TuyaOpenAPI,)

from nodes import tuya_robotvac_node
from nodes import tuya_pulsar_node
from nodes import tuya_pir_node
from nodes import tuya_pir2_node
from nodes import tuya_pirDoor_node
from nodes import tuya_relay_node
from nodes import tuya_relay_node_3
from nodes import tuya_switch_node
from nodes import tuya_switch_dimmer_node
from nodes import tuya_light_node
from nodes import tuya_light_node_rgb
from nodes import tuya_light_node_v1
from nodes import tuya_light_SL20_white
from nodes import tuya_air_circulator
from nodes import tuya_curtain_node
from nodes import tuya_watersensor_node
from nodes import tuya_valve_node

LOGGER = udi_interface.LOGGER
Custom = udi_interface.Custom


class TuyaController(udi_interface.Node):
    id = 'ctl'
    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2},
        {'driver': 'GV0', 'value': 0, 'uom': 56},
    ]

    def __init__(self, polyglot, parent, address, name):
        super(TuyaController, self).__init__(polyglot, parent, address, name)
        self.poly = polyglot
        self.count = 0
        self.n_queue = []
        self.Parameters = Custom(polyglot, 'customparams')
        self.Notices = Custom(polyglot, 'notices')
        # subscribe to the events we want
        polyglot.subscribe(polyglot.CUSTOMPARAMS, self.parameterHandler)
        polyglot.subscribe(polyglot.STOP, self.stop)
        polyglot.subscribe(polyglot.START, self.start, address)
        polyglot.subscribe(polyglot.ADDNODEDONE, self.node_queue)
        # start processing events and create add our controller node
        polyglot.ready()
        self.poly.addNode(self)

    def node_queue(self, data):
        self.n_queue.append(data['address'])

    def wait_for_node_done(self):
        while len(self.n_queue) == 0:
            time.sleep(0.1)
        self.n_queue.pop()

    def parameterHandler(self, params):
        self.Parameters.load(params)
        default_apiAccessId = "apiAccessId"
        default_apiSecret = "apiSecret"
        default_apiEndpoint = "apiEndpoint"
        default_apiMq = "apiMq"
        default_apiUid = "apiUid"
        default_apiRegion = "apiRegion"

        self.apiAccessId = self.Parameters.apiAccessId
        if self.apiAccessId is None:
            self.apiAccessId = default_apiAccessId
            LOGGER.error('check_params: apiKey not defined in customParams, please add it.  Using {}'.format(
                default_apiAccessId))
            self.AccessId = default_apiAccessId
        
        #if  self.AccessId == default_apiAccessId:   
        #   self.Notices['accessid'] = 'ACCESS ID must be configured.'

        self.apiSecret = self.Parameters.apiSecret
        if self.apiSecret is None:
            self.apiSecret = default_apiSecret
            LOGGER.error('check_params: apiSecret not defined in customParams, please add it.  Using {}'.format(
                default_apiSecret))
            self.apiSecret = default_apiSecret
        
        #if  self.apiSecret == default_apiSecret:   
        #   self.Notices['secret'] = 'API SECRET must be configured.'

        self.apiEndpoint = self.Parameters.apiEndpoint
        if self.apiEndpoint is None:
            self.apiEndpoint = default_apiEndpoint
            LOGGER.error('check_params: apiEndpoint not defined in customParams, please add it.  Using {}'.format(
                default_apiEndpoint))
            self.apiRegion = default_apiEndpoint
        
        #if  self.apiRegion == default_apiEndpoint:   
            #self.Notices['apiend'] = 'API ENDPOINT must be configured, make sure you have the right country.'

        self.apiMq = self.Parameters.apiMq
        if self.apiMq is None:
            self.apiMq = default_apiMq
            LOGGER.error('check_params: apiMq not defined in customParams, please add it.  Using {}'.format(
                default_apiMq))
            self.apiMq = default_apiMq
        
        #if  self.apiMq == default_apiMq:   
        #    self.Notices['apimq'] = 'API MQ must be configured, make sure you have the right country.'

        self.apiUid = self.Parameters.apiUid
        if self.apiUid is None:
            self.apiUid = default_apiUid
            LOGGER.error('check_params: apiUid not defined in customParams, please add it.  Using {}'.format(
                default_apiMq))
            self.apiUid = default_apiUid
        
        #if  self.apiUid == default_apiUid:   
        #    self.Notices['apiuid'] = 'API UID must be configured.'

        self.apiRegion = self.Parameters.apiRegion
        if self.apiRegion is None:
            self.apiRegion = default_apiRegion
            LOGGER.error('check_params: apiRegion not defined in customParams, please add it.  Using {}'.format(
                default_apiMq))
            self.apiRegion = default_apiRegion
        
        #if  self.apiRegion == default_apiRegion:   
        #    self.Notices['apiregion'] = 'API REGION must be configured, make sure you have the right country.'
            

    def start(self):
        self.poly.setCustomParamsDoc()
        self.poly.updateProfile()
        time.sleep(2)
        self.createNodes()

    def createNodes(self):
        LOGGER.info("Gathering Devices Please be Patient")
        # Init openapi and connect
        openapi = TuyaOpenAPI(
            self.apiEndpoint, self.apiAccessId, self.apiSecret)
        openapi.connect()
        # Get device information from all devices
        response = openapi.get("/v1.0/users/" + self.apiUid + "/devices")
        # Save polling data sample
        response1 = json.dumps(response, indent=4)  # current, indent=4
        LOGGER.info(response1)
        LOGGER.info('\n''Devices Sorted for ADD Node''\n')
        for i in response['result']:
            name = i['name']
            deviceid = i['id']
            id1 = deviceid[-7:].lstrip('.')
            address = id1
            LOGGER.info('Name')
            LOGGER.info(i['name'])
            LOGGER.info('ID')
            LOGGER.info(i['id'])
            LOGGER.info('Status')
            LOGGER.info(i['status'][0]['value'])
            # Incrementing addressing for Node Server ID
            LOGGER.info(i['id'])
            deviceid = i['id']
            id1 = deviceid[-7:].lstrip('.')
            new_id = id1
            LOGGER.info('Address')
            LOGGER.info(address)
            model = i['model']
            LOGGER.info(model)
            online = i['online']
            LOGGER.info('online')
            LOGGER.info(online)
            """if i['model'] == "PIR-wifi-V01" or i['product_name'] == "PIR Sensor " or i['product_name'] == "PIR " or i['product_name'] == "PIR Motion Detector Alarm" or i['product_name'] == "PIR senser":
                LOGGER.info('Device Type')
                LOGGER.info("PIR")
                LOGGER.info('\n')
                node = tuya_pir_node.PirNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "AW201_CBU" or i['product_name'] == "Contact Sensor":
                LOGGER.info('Device Type')
                LOGGER.info("PIR")
                LOGGER.info('\n')
                node = tuya_pirDoor_node.PirDNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()            
            elif i['model'] == "SS01S(\u4e0d\u5206\u8d1f\u8f7d)\u4e50\u946b" or i['model'] == "\u5f00\u5173(\u84dd\u7259+Wi-Fi)" or i['model'] == "SS01S\uff08\u706b\u7ebf\u8d1f\u8f7d\u7ebf\u4e0d\u5206\u7248\u672c\uff09BK\u7248\u672c":
                LOGGER.info('Device Type')
                LOGGER.info("SWITCH")
                LOGGER.info('\n')
                node = tuya_switch_node.SwitchNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "\u706f\u5e26\u63a7\u5236\u5668\uff08BK\uff09":
                LOGGER.info('Device Type')
                LOGGER.info("LED-V1")
                LOGGER.info('\n')
                node = tuya_light_node_v1.LightNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiRegion)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "SL10" or i['product_name'] == "Merkury BW904 Smart Bulb":
                LOGGER.info('Device Type')
                LOGGER.info("LED-V2")
                LOGGER.info('\n')
                node = tuya_light_node_rgb.LightNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiRegion)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['product_name'] == "120V A19 9W SMART BULB":
                LOGGER.info('Device Type')
                LOGGER.info("LED-V2")
                LOGGER.info('\n')
                node = tuya_light_node.LightNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiRegion)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "DS01C(\u91cf\u4ea7\uff09":
                LOGGER.info('Device Type')
                LOGGER.info("SWITCH Dimmer")
                LOGGER.info('\n')
                node = tuya_switch_dimmer_node.SwitchNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "TY-DIY-S04":
                LOGGER.info('Device Type')
                LOGGER.info("Relay")
                LOGGER.info('\n')
                node = tuya_relay_node.RelayNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "AHR-085" or i['product_id'] == "pxi0drurxccaahyr":
                LOGGER.info('Device Type')
                LOGGER.info("Relay3")
                LOGGER.info('\n')
                node = tuya_relay_node_3.RelayNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "\u5f00\u5173(\u84dd\u7259+Wi-Fi)" or i['product_name'] == "Mini Smart Plug" or i['product_id'] == "0g1fmqh6d5io7lcn":
                LOGGER.info('Device Type')
                LOGGER.info("SWITCH")
                LOGGER.info('\n')
                node = tuya_switch_node.SwitchNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "SS01S\uff08\u706b\u7ebf\u8d1f\u8f7d\u7ebf\u4e0d\u5206\u7248\u672c\uff09BK\u7248\u672c" or i['model'] == "SP10" or i['product_name'] == "Smart Socket":
                LOGGER.info('Device Type')
                LOGGER.info("SWITCH")
                LOGGER.info('\n')
                node = tuya_switch_node.SwitchNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()            
            elif i['model'] == "PIR-wifi-V01":
                LOGGER.info('Device Type')
                LOGGER.info("PIR")
                LOGGER.info('\n')
                node = tuya_pir_node.PirNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "BR151R":
                LOGGER.info('Device Type')
                LOGGER.info("Robot Vacuum")
                LOGGER.info('\n')
                node = tuya_robotvac_node.RobvacNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiRegion)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['product_name'] == "Smart Bulb-SL20":
                LOGGER.info('Device Type')
                LOGGER.info("LED-V2-White")
                LOGGER.info('\n')
                node = tuya_light_SL20_white.LightNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiRegion)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "AF1S" or i['product_name'] == "Air circulator":
                LOGGER.info('Device Type')
                LOGGER.info("Air Circulator")
                LOGGER.info('\n')
                node = tuya_air_circulator.AirCirNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiRegion)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "HC700TY" or i['product_name'] == "CURTAIN SYSTEM":
                LOGGER.info('Device Type')
                LOGGER.info("Curtain")
                LOGGER.info('\n')
                node = tuya_curtain_node.CurtainNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiRegion)
                self.poly.addNode(node)
                self.wait_for_node_done()"""
            if i['model'] == "TY-DIY-S04":
                LOGGER.info('Device Type')
                LOGGER.info("Relay")
                LOGGER.info('\n')
                node = tuya_relay_node.RelayNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiUid)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "1.0.1" or i['product_id'] == "k2h8vkj98fhvnpiv":
                LOGGER.info('Device Type')
                LOGGER.info("PIR2")
                LOGGER.info('\n')
                node = tuya_pir2_node.PirNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i["product_id"] == "upgcbody" or i["product_id"] == "js34cuma":
                LOGGER.info('Device Type')
                LOGGER.info("LEAK SENSOR")
                LOGGER.info('\n')
                node = tuya_watersensor_node.WaterSenNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            elif i['model'] == "ARD-100+" or i['product_id'] == "nguto5atyd2xxnap":
                LOGGER.info('Device Type')
                LOGGER.info("VALVE")
                LOGGER.info('\n')
                node = tuya_valve_node.valveNode(
                    self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint)
                self.poly.addNode(node)
                self.wait_for_node_done()
            else:
                LOGGER.info("OTHER DEVICE")
        #time.sleep(.5)
        #self.pulsar()
        
    def pulsar(self):
        pass
        LOGGER.info("Add Pulsar")
        address = "pulsa_1"
        name = "Pulsar"
        new_id = "pul_1"
        deviceid = "pulse01"
        LOGGER.info('Device Type')
        LOGGER.info("Pulsar")
        LOGGER.info('\n')
        node = tuya_pulsar_node.PullNode(self.poly, self.address, address, name, new_id, deviceid, self.apiAccessId, self.apiSecret, self.apiEndpoint, self.apiMq)
        self.poly.addNode(node)
        self.wait_for_node_done()

    def remove_notices_all(self, command):
        self.Notices.clear()    

    def delete(self):
        LOGGER.info('Delete Tuya Controller.')

    def stop(self):
        self.poly.stop()
        LOGGER.debug('NodeServer stopped.')
        nodes = self.poly.getNodes()
        for node in nodes:
            if node != 'controller':   # but not the controller node
                nodes[node].setDriver('ST', 0, True, True)

    def noop(self, command):
        LOGGER.info('Discover not implemented')

    id = 'tuya'

    commands = {
        'REMOVE_NOTICES_ALL': remove_notices_all,
        'DISCOVER': noop
        }
