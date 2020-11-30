# ds2mousefix WIP
Various fixes/workarounds for mouse input on dark souls 2 for linux

## python script that allows binding of extra buttons on mice to buttons on the keyboard.
  - ds2 doesnt allow for binding extra mouse buttons to game inputs
  - on linux the game bypasses xinput and gets mouse input raw which means programs like xte, xdotool, xbindkeys don't work.
  - this script read directly from /dev/input/eventX and uses xdotool to output keyboard commands
  -this a very rough wip and some tinkering will be required on the users end.
  
## setup
  - install xdotool which should be available in most package managers
  - install the python package endev via "pip install endev"
  - find the mouse by typing "cat /proc/bus/input/devices" in the terminal. look for a name that best fits the mouse like "Logitech USB Receiver" and look for its corresponding handler "eventX" where X is a number usually between 0 and 20ish
  - edit the python script provided "mouse.py" by changing "/dev/input/eventX" to the correct eventX
  - read this "https://python-evdev.readthedocs.io/en/latest/tutorial.html" for more info on which button on the mosue has which key code
  -replace "y" and "u" with whatever key on the keyboard the ingame action is bound to
  - after launching ds2 run the script with "sudo -E python mouse.py". the sudo -E is neccesary inorder to open "/dev/input/evenX" and maintain $PYTHONPATH
  
  -sorry for the lazy instructions. they are temporary as I may make the script a little more robust(crashes when mouse is unplugged) and user friendly.
  
