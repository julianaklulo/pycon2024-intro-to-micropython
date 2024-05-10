"""
Exercise 2: Move the pixel.

Display a pixel at coordinate (2, 2) and make it move based on
the accelerometer values:
- Read x and y axis
- Increase or decrease the coordinates based on the the values read
- Show the pixel at the new coordinates

Tip: don't forget to clear the pixel before showing it at the
new coordinates.
"""

from microbit import *


x, y = 2, 2

while True:
    display.set_pixel(x, y, 0)

    if accelerometer.get_x() > 0:
        x = min(x + 1, 4)
    else:
        x = max(x - 1, 0)

    if accelerometer.get_y() > 0:
        y = min(y + 1, 4)
    else:
        y = max(y - 1, 0)

    display.set_pixel(x, y, 9)
    sleep(100)
