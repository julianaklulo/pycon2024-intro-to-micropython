"""
Example 1: Buttons and images.

Show an image based on the button pressed:
- If button_a is pressed, show a happy face
- If button_b is pressed, show a sad face
"""
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)

    sleep(100)
    display.clear()
