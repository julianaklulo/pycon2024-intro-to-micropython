"""
Exercise 1: Buttons and arrows.

Show an arrow poiting to the direction of the button that is pressed:
- If button_a is pressed, show an arrow pointing to left
- If button_b is pressed, show an arrow pointing to right
"""

from microbit import *


while True:
    if button_a.is_pressed():
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        display.show(Image.ARROW_E)
    sleep(100)
    display.clear()
