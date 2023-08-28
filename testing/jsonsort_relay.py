# Custom Parameters Call
from tuya_connector import (
    TuyaOpenAPI,)
import time
import json
import colorsys
from tuya_bulb_control import Bulb

ACCESS_ID = "txejpdfda9iwmn5cg2es"
ACCESS_KEY = "46d6072ffd724e0ba5ebeb5cc6b9dce9"
API_ENDPOINT = "https://openapi.tuyaus.com/"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"
API_REGION = "us"
API_UID = "az1610958067414WkfOO"

# from file
# f = open('sample.json')
# response = json.load(f)
# list = json.dumps(devices, indent=4)
# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

#response = openapi.get("/v1.0/users/az1610958067414WkfOO/devices")
# print(type(response))
DEVICELED_ID = '68635610e8db84fff7ea'

# Node Server Controller Testing


# Call APIs from Tuya

"""response = openapi.get("/v1.0/users/" + API_UID + "/devices")#DEVICELED_ID) #"/devices")
#
#print(response)
for i in response['result']:
    #print(i)
    print(i['name'])
    print(i['online'])
# Writing to sample.json
# with open("sample.json", "w") as outfile:
#    outfile.write(str(response1))"""

response = openapi.get("/v1.0/iot-03/devices/{}".format(DEVICELED_ID) + "/status/")
# Save polling data sample
# current = {'timestamp': time.time(), 'devices': response}
response1 = json.dumps(response, indent=4)  # current, indent=4
#print(response1)


############################### Device ID's ###################################
# WiFi switch-4CH'68635610e8db84fff7ea'


"""# Switch Node
DEVICESW_ID = '68635610e8db84fff7ea'

# Switch Node
DEVICEPIR_ID = 'eb29412a460a068676g8cv'"""


"""response1 = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICELED_ID) + "/online/")  # DEVICE_ID
print(response1)
for i in response1:#['result']:
    print(i)
    #if i['value'] == True:
    #    print('gotya')"""

"""# Need to GET switch status Query NS
print('\n''GET Response Switch Statuses''\n')
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()
response1 = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")  # DEVICE_ID
print(response1)
for i in response1['result'][0:1]:
    # print(i)
    print(i['value'])
# print("\n")
# print(response1)"""


#### Statuses
# response1['result'][0:1] = relay One
# response1['result'][1:2] = relay two
# response1['result'][2:3] = relay three
# response1['result'][3:4] = relay four

#### Commands Four Channel Relay Json Model Number-"TY-DIY-S04"
"""commands = {'commands': [{'code': 'switch_1', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_1', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
commands = {'commands': [{'code': 'switch_2', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_2', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
commands = {'commands': [{'code': 'switch_3', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_3', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
commands = {'commands': [{'code': 'switch_4', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
# print(response)
time.sleep(2)
commands = {'commands': [{'code': 'switch_4', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
print(response)
time.sleep(2)
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICESW_ID), commands)
response = openapi.get("/v1.0/devices/{}".format(DEVICESW_ID))  # DEVICE_ID
print(response)"""


"""{
    "result": [
        {
            "active_time": 1687404896,
            "biz_type": 0,
            "category": "kg",
            "create_time": 1687404896,
            "icon": "smart/icon/ay1525015673758Ghvpg/2587b975a6b0645e83559835ef7c7eef.png",
            "id": "68635610e8db84fff7ea",
            "ip": "98.41.236.33",
            "lat": "",
            "local_key": "#r0>b64A>a7<w_O:",
            "lon": "",
            "model": "TY-DIY-S04",
            "name": "WiFi switch-4CH",
            "online": true,
            "owner_id": "33161067",
            "product_id": "waq2wj9pjadcg1qc",
            "product_name": "WiFi switch-4CH",
            "status": [
                {
                    "code": "switch_1",
                    "value": false
                },
                {
                    "code": "switch_2",
                    "value": false
                },
                {
                    "code": "switch_3",
                    "value": false
                },
                {
                    "code": "switch_4",
                    "value": false
                },
                {
                    "code": "countdown_1",
                    "value": 0
                },
                {
                    "code": "countdown_2",
                    "value": 0
                },
                {
                    "code": "countdown_3",
                    "value": 0
                },
                {
                    "code": "countdown_4",
                    "value": 0
                },
                {
                    "code": "switch",
                    "value": false
                }
            ],
            "sub": false,
            "time_zone": "-08:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1687404903,
            "uuid": "68635610e8db84fff7ea"
        },"""

