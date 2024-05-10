"""
Exercise 3: Sound reaction.

Get the current sound event and display:
- Happy face if the noise is “loud”
- Asleep face if noise is “quiet”
"""

from microbit import *


while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HAPPY)
    elif microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.ASLEEP)

    sleep(100)
    display.clear()
