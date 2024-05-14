"""
Example 2: Accelerometer and arrows.

Show an arrow pointing to the direction of the accelerometer values:
- If the current gesture is “up”, show an arrow pointing north
- If the current gesture is “down”, show an arrow pointing south
- If the current gesture is “left”, show an arrow pointing west
- If the current gesture is “right”, show an arrow pointing east
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
