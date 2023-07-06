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
# Contact Sensor 'eb1a6a7a7f7a5caebcgick 
DEVICELED_ID = 'eb1a6a7a7f7a5caebcgick'

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
            "/v1.0/iot-03/devices/{}".format(DEVICELED_ID) + "/status/")  # DEVICE_ID
#print(response1)
print(response)
for i in response['result']:
    print(i)


"""for i in response["result"][0:1]:
    print(i["code"])
    print(i["value"])
    if i["value"] == True:
        print("Opened Door")
    if i["value"] == False:
        print("Door Closed")"""




# do not run it just keeps going and going lol
"""starttime = time.time()
while True:
    print("tick")
    time.sleep(1.5 - ((time.time() - starttime) % 1.5))"""


"""for i in response['result']:
    name = i['name']
    model = i['model']
    print(name)
    print(model)"""




# Door Contact Sensor
""""result" [{
            "active_time": 1688442261,
            "biz_type": 0,
            "category": "mcs",
            "create_time": 1688442261,
            "icon": "smart/icon/ay1562583874631k02Aw/051a2210ea3db49d307a52778aabe00e.jpg",
            "id": "eb1a6a7a7f7a5caebcgick",
            "ip": "98.41.236.33",
            "lat": "37.7200",
            "local_key": "nPfNk[`]QtP}h?Ln",
            "lon": "-121.4700",
            "model": "AW201_CBU",
            "name": "Contact Sensor Test",
            "online": True,
            "owner_id": "33161067",
            "product_id": "5clcipazwycf176m",
            "product_name": "Contact Sensor",
            "status": [
                {
                    "code": "doorcontact_state",
                    "value": False
                },
                {
                    "code": "battery_percentage",
                    "value": 100
                }
            ],
            "sub": False,
            "time_zone": "-07:00",
            "uid": "az1610958067414WkfOO",
            "update_time": 1688442508,
            "uuid": "965c3d67e81e3106"
        },]


for i in ['result']:
    name = i['name']
    model = i['model']
    print(name)
    print(model)"""
    
"""for i in response['result']:
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
            print(product_name)"""    


# PIR
############################### Device ID's ###################################
"""# 'ebe097c0407da32084kvtr'  # 'ebfc16d57ed374932cjqfk' # 804076608caab5d8ff58
DEVICELED_ID = 'ebe097c0407da32084kvtr'

# Switch Node
DEVICESW_ID = '68635610e8db84fff7ea'

# Switch Node
DEVICEPIR_ID = 'eb29412a460a068676g8cv'"""

# Node Server Node Light Testing
# API will be passed from controller
#openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
#openapi.connect()



# do not run it just keeps going and going lol
"""starttime = time.time()
while True:
    print("tick")
    time.sleep(1.5 - ((time.time() - starttime) % 1.5))"""

"""for i in response['result']:
    name = i['name']
    model = i['model']
    print(name)
    print(model)"""


# PIR
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
        },"""

"""{
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
        },"""