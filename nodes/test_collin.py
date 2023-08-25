import json
f = open("/Users/stevenbailey/UDI Development PG3/Nodeservers/udi-tuya-poly-cloud-api-v3/nodes/collin.json", "r")

#print(f.read())
#print(type(f.read()))

#f = json.dumps(f, indent=4)


for i in f[0]:
    print(i)