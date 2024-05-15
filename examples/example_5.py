"""
Example 5: Teleporting duck.

Create a teleporting duck:
- Choose a partner and define a radio group
- Send “duck” when the device is shaken
- Display a duck when “duck” is received
"""
from microbit import *
import radio

GROUP = 0  # Define a group number with a partner

radio.on()
radio.config(group=GROUP)

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        radio.send("duck")
    if radio.receive() == "duck":
        display.show(Image.DUCK)
    sleep(100)
