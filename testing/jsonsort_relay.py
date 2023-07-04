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


# from file
# f = open('sample.json')
# response = json.load(f)
# list = json.dumps(devices, indent=4)


# Node Server Controller Testing
# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call APIs from Tuya
# Get device information from all devices
response = openapi.get("/v1.0/users/az1610958067414WkfOO/devices")
# print(type(response))

# Save polling data sample
# current = {'timestamp': time.time(), 'devices': response}
response1 = json.dumps(response, indent=4)  # current, indent=4
print(response1)

# Writing to sample.json
# with open("sample.json", "w") as outfile:
#    outfile.write(str(response1))

############################### Device ID's ###################################
"""# 'ebe097c0407da32084kvtr'  # 'ebfc16d57ed374932cjqfk' # 804076608caab5d8ff58
DEVICELED_ID = 'ebe097c0407da32084kvtr'

# Switch Node
DEVICESW_ID = '68635610e8db84fff7ea'

# Switch Node
DEVICEPIR_ID = 'eb29412a460a068676g8cv'"""



#### Four Channel Relay Json Model Number-"TY-DIY-S04"
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

"""response1 = openapi.get(
    "/v1.0/iot-03/devices/{}".format(DEVICESW_ID) + "/status/")  # DEVICE_ID
for i in response1['result'][3:4]:
    print(i['value'])
    if i['value'] == True:
        print('gotya')"""

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

