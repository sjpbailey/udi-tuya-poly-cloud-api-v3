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

# Light Strip 'ebe097c0407da32084kvtr' # 804076608caab5d8ff58 # garage 'ebfd4f4263bb769d99zjkq' sconce eb64341be3d433d8615eib
bulb = Bulb(
    client_id="txejpdfda9iwmn5cg2es",
    secret_key="46d6072ffd724e0ba5ebeb5cc6b9dce9",
    device_id="eb64341be3d433d8615eib",
    region_key="us",
)

current_colour = json.loads(bulb.current_value("colour_data_v1"))
#print('incoming color HSL')
#print(current_colour)
#print(type(current_colour))
#bulb.set_colour_v2(current_colour)
# Conversion current HSV to RGB
current_colour = colorsys.hsv_to_rgb(
    h=current_colour["h"] /360,
    s=current_colour["s"] /1000,
    v=current_colour["v"] /1000)
current_colour = tuple(map(lambda x: int(x * 255), current_colour))
print("Current")
print(current_colour)

"""Colors = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0], "green": [
            0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95], "violet": [139, 0, 255], "white": [255, 255, 255]}"""
### Set Color
h= 255
s= 0
v= 119
### Set Dimmer
dim = 1
if dim < 2:
    dim = 2
dimmer = 100*1/(dim)

rainbow = {"red": [h/dimmer, s/dimmer, v/dimmer],}

print(current_colour)

for x in range(2):
    for i in rainbow:
        r = rainbow[i][0]
        g = rainbow[i][1]
        b = rainbow[i][2]
        time.sleep(2)
        #print('    %s (%d,%d,%d)' % (i, r, g, b))
        new_colour = (r, g, b)
        # print(new_colour)
        # Convert RGB coordinates to int
        new_colour = tuple(map(lambda x: int(x), new_colour))
        #print(new_colour)
        # Set colour ✨
        # For Version 2 # set_colour_v2(new_color)
        bulb.set_colour(new_colour)







"""for i in current_colour:
    print(i)
# Convert the current RGB to format 0-255
#current_colour = tuple(map(lambda x: int(x * 255), current_colour))
for i in current_colour:
    pass
    #print(i)"""
"""rainbow = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0], "green": [
            0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95], "violet": [139, 0, 255], "white": [255, 255, 255]}"""
"""new_bright = 10
if new_bright < 2:
    new_bright = 2
new_bright1 = 100*1/(new_bright)


new_colour = [255/new_bright1, 0/new_bright1, 0/new_bright1] 
#new_colour = (h,l,s)#new_level)
new_colour = tuple(map(lambda x: int(x), new_colour))
print('new color RGB')
print(new_colour)
# Set colour ✨
bulb.set_colour_v2(new_colour)

#whi_vlv = 10
#bulb.set_bright_v2(whi_vlv)
#new_colour = [255, 0, 0] """

# Convert the current RGB to format 0-255
"""current_colour = tuple(map(lambda x: int(x), current_colour))
print('current color RGB')
print(current_colour)
current_colour = json.loads(bulb.current_value("colour_data_v2"))
new_colour = [current_colour]    #[255, 0, 0]  # v
# print(new_colour)
# Convert RGB coordinates to int
new_colour = tuple(map(lambda x: int(x), new_colour))
print('new color output')
print(new_colour)
# Set colour ✨
bulb.set_colour_v2(new_colour)
time.sleep(1)"""





# print("current color rgb")
# print(current_colour)
# Convert the current RGB to format 0-255
#current_colour = tuple(map(lambda x: int(x), current_colour))
#print('current color RGB')





# print(current_colour)
# Get new RGB colour
#new_level = 1
#bulb.set_bright_v2(new_level)
#print(bulb.current_value())

#"scene" "colour" "white" "scene_1" "scene_2-4"
#bulb.set_work_mode("scene_1")

# Set colour ✨
#bulb.set_colour_v2(new_colour)
#time.sleep(1)



"""new_level = 100
bulb.set_colour_temp_v2(new_level)
time.sleep(1)

#bulb.set_temp_value_v2(new_level)
time.sleep(1)

#bulb.set_bright_v2(new_level)
#print(bulb.current_value())
bulb.turn_off(new_level)
time.sleep(1)
bulb.turn_on(new_level)
time.sleep(1)"""



"""print(bulb.functions())

def toggle_status(button) -> NoReturn:
    # Turn ON or OFF
    bulb.set_toggle()

    # Change button text
    button["text"] = "ON" if button["text"] == "OFF" else "OFF"


def init_ui() -> NoReturn:
    # Switch button
    toggle_status_btn = Button(
        text="ON"
        if not bulb.current_value("switch_led")
        else "OFF",  # Text depends on state
        width=20,
        command=lambda: toggle_status(toggle_status_btn),
    )
    # Colour selection button
    change_colour_btn = Button(
        text="Change colour", width=20, command=change_colour)

    # Positioning the buttons
    toggle_status_btn.pack(side="left", padx=5, pady=5, ipady=6)
    change_colour_btn.pack(side="right", padx=5, pady=5, ipady=6)


if __name__ == "__main__":
    tk = Tk()
    tk.title("Colour change example")
    init_ui()
    tk.mainloop()"""
