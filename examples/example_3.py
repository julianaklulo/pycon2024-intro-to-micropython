"""
Example 3: Accelerometer gestures.

Show an arrow pointing to the direction of the accelerometer gesture.
"""
from microbit import *

while True:
    gesture = accelerometer.current_gesture()

    if gesture == "up":
        display.show(Image.ARROW_N)
    elif gesture == "down":
        display.show(Image.ARROW_S)
    elif gesture == "left":
        display.show(Image.ARROW_W)
    elif gesture == "right":
        display.show(Image.ARROW_E)

    sleep(100)
    display.clear()
