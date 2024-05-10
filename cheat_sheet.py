"""
Cheat sheet with all the commands and functions that are useful for this tutorial.

For more in-depth information, please refer to the official documentation in
the Python editor (https://python.microbit.org/) or the official MicroPython
documentation (https://microbit-micropython.readthedocs.io/en/latest/).
"""

# ***** Display *****
from microbit import *

# Display an image
display.show(Image.HEART)

# Display custom image
display.show(Image("00990:" "00900:" "00900:" "99999:" "09990"))

# Scroll text
display.scroll("PyCon US")

# Set pixels
display.set_pixel(0, 0, 9)

# Clear display
display.clear()


# ***** Push Buttons *****
from microbit import *

# Check if button A was pressed
if button_a.was_pressed():
    pass

# Check if button B was pressed
if button_b.was_pressed():
    pass

# Check if button A is pressed
if button_a.is_pressed():
    pass

# Check if button B is pressed
if button_b.is_pressed():
    pass

# Get how many times button A was pressed
quantity = button_a.get_presses()

# Get how many times button B was pressed
quantity = button_b.get_presses()


# ***** Speaker *****
from microbit import *
import music, speech, audio

# Play pre-defined music
music.play(music.POWER_UP)

# Create your own music - Format: '{note}{octave}:{duration}'
music.play(
    [
        "G4:2",
        "A4:2",
        "B4:4",
        "D5:4",
        "D5:4",
        "B4:4",
        "C5:4",
        "C5:4",
        "r:2",
        "G4:2",
        "A4:2",
        "B4:4",
        "D5:4",
        "D5:4",
        "C5:4",
        "B4:8",
    ]
)

# Text to speech
speech.say("Hello, PyCon!")

# Play expressive sounds
audio.play(sound.YAWN)


# ***** Michophone *****
from microbit import *

# SoundEvent can be LOUD or QUIET

# Read current event
event = microphone.current_event()

# Get the sound history as a tuple
history = microphone.get_events()

# Get sound level (0-255)
level = microphone.sound_level()


# ***** Accelerometer *****
from microbit import *

# Read acceleration in each axis
x = accelerometer.get_x()
y = accelerometer.get_y()
z = accelerometer.get_z()

# Read pre-defined current gesture
gesture = accelerometer.is_gesture("face up")

# Read pre-defined past gesture
gesture = accelerometer.was_gesture("shake")


# ***** Radio *****
import radio

# Turn on the radio
radio.on()

# Set the radio group and power
# Group: 0-255, Power: 0-7 (signal intensity)
radio.config(group=23, power=7)

# Receive a message from the group
message = radio.receive()

# Send a message to the group
radio.send("PyCon US")
