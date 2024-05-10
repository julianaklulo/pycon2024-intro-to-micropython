# Introduction to MicroPython: getting started with BBC micro:bit

Repository with the code and slides for my [tutorial](https://us.pycon.org/2024/schedule/presentation/4/) at PyCon US 2024.

# Description
In this tutorial you'll learn how to use the resources of the BBC micro:bit, an open source embedded device that lets you control electronic components using MicroPython. Some of the components you'll learn to use in this tutorial include:

* Push buttons
* 5x5 LED matrix
* Accelerometer sensor
* Radio communication.

The goal of the tutorial is to implement a version of the Battleship game that can be controlled using the accelerometer sensor.

# Resources
This repository contains all the code avaiable in the slides, as well as the code for the exercises and projects.

## Cheat Sheet
The file [cheat_sheet.py](cheat_sheet.py) has code examples for all the components we'll use in the tutorial.

## Exercises
The answers to the exercises are available in the folder [exercises](exercises).

**I trust you to try to solve the exercises on your own before checking the answers. If you have any questions, feel free to ask me during the tutorial.**

## Projects
The tutorial has two projects: a single-player version and a multiplayer version of the Battleship game.

### Single-player Battleship
Use the template files available in the folder [battleship-single-player](battleship-single-player) to fill the gaps during the tutorial.

* [Template 1](battleship-single-player/template_1.py): Study the class `Ship`
* [Template 2](battleship-single-player/template_2.py): Fill the `shoot`method in class `Player`
* [Template 3](battleship-single-player/template_3.py): Complete the class `Game`

The final code for the single-player version of the game is available in the file [single-player-complete.py](battleship-single-player/single_player_complete.py).

### Multi-player Battleship
Use the template files available in the folder [battleship-multiplayer](battleship-multiplayer) to fill the gaps during the tutorial.

* [Template 1](battleship-multiplayer/template_1.py): Complete the multiplayer aspects of the class `Game`

The final code for the multi-player version of the game is available in the file [multiplayer-complete.py](battleship-multiplayer/multiplayer_complete.py).

### Slides
The slides for this tutorial are available in the file [slides.pdf](slides.pdf).
