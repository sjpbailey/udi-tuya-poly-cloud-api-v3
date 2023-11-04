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


# Node Server Controller Testing
# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call APIs from Tuya
# Get device information from all devices
response = openapi.get("/v1.0/iot-03/device-groups")#"/v1.0/users/az1610958067414WkfOO/devices")
# print(type(response))

# Save polling data sample
# current = {'timestamp': time.time(), 'devices': response}
response1 = json.dumps(response, indent=4)  # current, indent=4
print(response1)

# Writing to sample.json
# with open("sample.json", "w") as outfile:
#    outfile.write(str(response1))


############################### Device ID's ###################################
# PIR 'eb29412a460a068676g8cv'  # PIR Sensor 'eb5e5f786fffbf04b9ldxl' PIR senser = eb0689ecbb2914fdcffopt
DEVICELED_ID = 'eb0689ecbb2914fdcffopt'

"""# Switch Node
DEVICESW_ID = '68635610e8db84fff7ea'

# Switch Node
DEVICEPIR_ID = 'eb29412a460a068676g8cv'"""

# Node Server Node Light Testing
# API will be passed from controller
#openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
#openapi.connect()
#openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICELED_ID), commands)
response = openapi.get(
            "/v1.0/iot-03/devices/{}".format(DEVICELED_ID) + "/[{'code': 'battery_percentage', 'value': True}]/")  # DEVICE_ID



#response = openapi.get(
#            "/v1.0/devices/{}".format(DEVICELED_ID) + "/logs/")  # DEVICE_ID


#print(response1["colour_data_v2"])
print(response)



# do not run it just keeps going and going lol
"""starttime = time.time()
while True:
    print("tick")
    time.sleep(1.5 - ((time.time() - starttime) % 1.5))"""

#for i in response['result']:#[1:2]:
    #name = i['name']
    #model = i['model']
    #print(name)
#    print(i)#['value'])
    
#### Statuses
# response['result'][0:1] = {'code': 'pir', 'value': 'none'}, i["value"] = 'none'
# response['result'][1:2] = {'code': 'battery_percentage', 'value': 100}, i['value']) = 100%

#current errors FIX THESE PLEASE
"""thread-5
2023-07-08 00:46:24,020 Thread-5   udi_interface      ERROR    udi_interface:write: :
2023-07-08 00:46:24,020 Thread-5   udi_interface      ERROR    udi_interface:write: Traceback (most recent call last):
2023-07-08 00:46:24,020 Thread-5   udi_interface      ERROR    udi_interface:write: File "/usr/local/lib/python3.9/threading.py", line 980, in _bootstrap_inner
2023-07-08 00:46:24,020 Thread-5   udi_interface      ERROR    udi_interface:write: self.run()
2023-07-08 00:46:24,020 Thread-5   udi_interface      ERROR    udi_interface:write: File "/usr/local/lib/python3.9/threading.py", line 917, in run
2023-07-08 00:46:24,021 Thread-5   udi_interface      ERROR    udi_interface:write: self._target(*self._args, **self._kwargs)
2023-07-08 00:46:24,021 Thread-5   udi_interface      ERROR    udi_interface:write: File "/var/polyglot/pg3/ns/0021b9026486_9/nodes/tuya_pirDoor_node.py", line 84, in poll
2023-07-08 00:46:24,021 Thread-5   udi_interface      ERROR    udi_interface:write: self.SwStat(self)
2023-07-08 00:46:24,021 Thread-5   udi_interface      ERROR    udi_interface:write: File "/var/polyglot/pg3/ns/0021b9026486_9/nodes/tuya_pirDoor_node.py", line 43, in SwStat
2023-07-08 00:46:24,022 Thread-5   udi_interface      ERROR    udi_interface:write: API_ENDPOINT = self.API_ENDPOINT
2023-07-08 00:46:24,022 Thread-5   udi_interface      ERROR    udi_interface:write: AttributeError
2023-07-08 00:46:24,022 Thread-5   udi_interface      ERROR    udi_interface:write: :
2023-07-08 00:46:24,022 Thread-5   udi_interface      ERROR    udi_interface:write: 'PirDNode' object has no attribute 'API_ENDPOINT'"""

""" Thread-9
2023-07-08 00:46:26,049 Thread-9   udi_interface      ERROR    udi_interface:write: :
2023-07-08 00:46:26,049 Thread-9   udi_interface      ERROR    udi_interface:write: Traceback (most recent call last):
2023-07-08 00:46:26,049 Thread-9   udi_interface      ERROR    udi_interface:write: File "/usr/local/lib/python3.9/threading.py", line 980, in _bootstrap_inner
2023-07-08 00:46:26,050 Thread-9   udi_interface      ERROR    udi_interface:write: self.run()
2023-07-08 00:46:26,050 Thread-9   udi_interface      ERROR    udi_interface:write: File "/usr/local/lib/python3.9/threading.py", line 917, in run
2023-07-08 00:46:26,050 Thread-9   udi_interface      ERROR    udi_interface:write: self._target(*self._args, **self._kwargs)
2023-07-08 00:46:26,050 Thread-9   udi_interface      ERROR    udi_interface:write: File "/var/polyglot/pg3/ns/0021b9026486_9/nodes/tuya_pir_node.py", line 70, in poll
2023-07-08 00:46:26,051 Thread-9   udi_interface      ERROR    udi_interface:write: self.SwStat(self)
2023-07-08 00:46:26,051 Thread-9   udi_interface      ERROR    udi_interface:write: File "/var/polyglot/pg3/ns/0021b9026486_9/nodes/tuya_pir_node.py", line 43, in SwStat
2023-07-08 00:46:26,051 Thread-9   udi_interface      ERROR    udi_interface:write: API_ENDPOINT = self.API_ENDPOINT
2023-07-08 00:46:26,051 Thread-9   udi_interface      ERROR    udi_interface:write: AttributeError
2023-07-08 00:46:26,051 Thread-9   udi_interface      ERROR    udi_interface:write: :
2023-07-08 00:46:26,051 Thread-9   udi_interface      ERROR    udi_interface:write: 'PirNode' object has no attribute 'API_ENDPOINT'
"""


#### PIR
"""{
            "active_time": 1686981690,
            "biz_type": 0,
            "category": "pir",
            "create_time": 1686981690,
            "icon": "smart/icon/ay15554925906369PM9S/131d393c8aa546206ffcf603f38ceb54.png",
            "id": "eb29412a460a068676g8cv",
            "ip": "98.41.236.33",
            "lat": "37.7200",
            "local_key": "~M0kO};;9R$d'wqL",
            "lon": "-121.4700",
            "model": "PIR-wifi-V01",
            "name": "PIR",
            "online": false,
            "owner_id": "33161067",
            "product_id": "o1l76njefmksbgkk",
            "product_name": "PIR",
            "status": [
                {
                    "code": "pir",
                    "value": "none"
                },
                {
                    "code": "battery_percentage",
                    "value": 100
                }
            ],
            "sub": false,
            "time_zone": "-07:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1687288443,
            "uuid": "8390601eff14128c"
        },

    {
            "active_time": 1688118544,
            "biz_type": 0,
            "category": "pir",
            "create_time": 1688118544,
            "icon": "smart/icon/ay1524194438166Zg2hZ/162545442419b6b47e132.jpg",
            "id": "eb5e5f786fffbf04b9ldxl",
            "ip": "98.41.236.33",
            "lat": "37.7200",
            "local_key": ")pV=i/M$Xz>bFHEN",
            "lon": "-121.4700",
            "model": "",
            "name": "PIR Master",
            "online": true,
            "owner_id": "33161067",
            "product_id": "tuadvwloutnzat2p",
            "product_name": "PIR Sensor ",
            "status": [
                {
                    "code": "pir",
                    "value": "none"
                },
                {
                    "code": "battery_percentage",
                    "value": 100
                }
            ],
            "sub": false,
            "time_zone": "-07:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1688118945,
            "uuid": "7c864f922baac602"
        },
        
    for i in response['result']:
            name = i['name']
            deviceid = i['id']
            id1 = deviceid[-7:].lstrip('.')
            address = id1
            product_name = i['product_name']
            #print('Name')
            #print(i['name'])
            #print('ID')
            #print(i['id'])
            print(i['product_name'])
            #print('Status')
            #print(i['status'][0]['value'])
            
            # Incrementing addressing for Node Server ID
            print(i['id'])
            deviceid = i['id']
            id1 = deviceid[-7:].lstrip('.')
            new_id = id1
            print('Address')
            print(address)
            model = i['model']
            print(model)
            product_name = i['product_name']
            print(product_name),
        {
            "active_time": 1688675193,
            "biz_type": 0,
            "category": "pir",
            "create_time": 1688675193,
            "icon": "smart/icon/ay1562583874631k02Aw/490e26f4b6e3bb27fc60e8e1ebc013ac.jpg",
            "id": "eb0689ecbb2914fdcffopt",
            "ip": "98.41.236.33",
            "lat": "37.7200",
            "local_key": "8.1*Fe*GBKYPVx?^",
            "lon": "-121.4700",
            "model": "CT60W_CBU_NL",
            "name": "PIR new gate",
            "online": true,
            "owner_id": "33161067",
            "product_id": "rp9akkjbohm7xdwe",
            "product_name": "PIR senser",
            "status": [
                {
                    "code": "pir",
                    "value": "none"
                },
                {
                    "code": "battery_percentage",
                    "value": 100
                }
            ],
            "sub": false,
            "time_zone": "-07:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1688675255,
            "uuid": "273734ea16f8e280"
        },"""
