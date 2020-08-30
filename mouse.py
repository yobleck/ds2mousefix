# https://thehackerdiary.wordpress.com/2017/04/21/exploring-devinput-1/
# https://www.kernel.org/doc/Documentation/input/input.txt
# https://python-evdev.readthedocs.io/en/latest/tutorial.html
# https://stackoverflow.com/questions/25346171/cant-import-module-when-using-root-user     sudo -E for running python
# cat /proc/bus/input/devices

"""
#for looking at raw input
import struct;
#mouse specific
#f = open("/dev/input/mouse1", "rb");
#f = open("/dev/input/by-id/usb-Logitech_USB_Receiver-mouse", "rb");
#event
f= open("/dev/input/event8", "rb");

while True:
    #mouse specific
    #data = f.read(3);
    #print(struct.unpack("3b",data));
    #event
    data = f.read(24);
    print(struct.unpack("4IHHI", data));
"""

import evdev, time, subprocess;

#logitech mouse specific
for x in [evdev.InputDevice(path) for path in evdev.list_devices()]:
    if(x.name == "Logitech USB Receiver" and x.phys == "usb-0000:2a:00.1-6/input0"): #change these to the name of your device (see line 5)
        device = evdev.InputDevice(x.path); #this may have to be searched for if eventX changes on reboot
print(device);
pressed = False;
while True:
    try:
        key = device.active_keys();
        if(len(key) > 0):
            pressed = True;
            if(key[0] == 275):
                subprocess.run(["xdotool", "keydown", "y"]);
            
            if(key[0] == 276):
                subprocess.run(["xdotool", "keydown", "u"]);
        elif(pressed == True):
            pressed = False;
            subprocess.run(["xdotool", "keyup", "y"]);
            subprocess.run(["xdotool", "keyup", "u"]);
    except:
        pass;
    time.sleep(0.05);
