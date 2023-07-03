"""
A simple Tkinter example demonstrating colour change and state switching.
Only two buttons:
    toggle_status_btn - Turning ON or OFF the light bulb.
    change_colour_btn - Opens a window with a palette.
"""
import time
import colorsys
import json
from typing import NoReturn
from tkinter import Tk, Button, colorchooser
from tuya_bulb_control import Bulb

# Office 'ebfc16d57ed374932cjqfk' # 804076608caab5d8ff58 # Garage 'ebfd4f4263bb769d99zjkq' sconce eb64341be3d433d8615eib
bulb = Bulb(
    client_id="txejpdfda9iwmn5cg2es",
    secret_key="46d6072ffd724e0ba5ebeb5cc6b9dce9",
    device_id="ebfc16d57ed374932cjqfk",
    region_key="us",
)
#bulb.turn_on()
#time.sleep(1)
current_colour = json.loads(bulb.current_value("colour_data_v2"))
# Conversion current HSV to RGB
current_colour = colorsys.hsv_to_rgb(
    h=current_colour["h"] /360,
    s=current_colour["s"] /1000,
    v=current_colour["v"] /1000)
current_colour = tuple(map(lambda x: int(x * 255), current_colour))
print("Current")
print(current_colour)


for i in current_colour:
    r = 255
    g = 255
    b = 255
    #print(i)
    #print('    %s (%d,%d,%d)' % (i, r, g, b))

"""Colors = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0], "green": [
            0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95], "violet": [139, 0, 255], "white": [255, 255, 255]} "green": [0, 128, 0]}"""

### Set Dimmer
dim = 1

if dim < 2:
    dim = 2
dimmer = 100*1/(dim)
rainbow = {"red": [r/dimmer, g/dimmer, b/dimmer],}
#print(current_colour)
for x in range(2):
    for i in rainbow:
        r = rainbow[i][0]
        g = rainbow[i][1]
        b = rainbow[i][2]
        #time.sleep(2)
        #print('    %s (%d,%d,%d)' % (i, r, g, b))
        new_colour = (r, g, b)
        # print(new_colour)
        # Convert RGB coordinates to int
        new_colour = tuple(map(lambda x: int(x), new_colour))
        #print(new_colour)
        # Set colour ✨
        bulb.set_colour_v2(new_colour)
