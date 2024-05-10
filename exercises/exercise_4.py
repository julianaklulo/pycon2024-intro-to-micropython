"""
Exercise 4: Teleporting duck.

Create a teleporting duck:
- Choose a partner and define a radio group
- Send “duck” when the device is shaken
- Display a duck when “duck” is received

Tip: clear the display before sending the duck
"""

from microbit import *
import radio


GROUP = 23

radio.on()
radio.config(group=GROUP)

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        radio.send("duck")
    if radio.receive() == "duck":
        display.show(Image.DUCK)
    sleep(100)
