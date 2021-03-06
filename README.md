# Overview

## Purpose

My purpose in developing this software is to practice using different libraries together (e.g `threading`, `socket`, `arcade`). I wanted to learn how to create a peer to peer connection. I also wanted to learn how to use the Python Arcade game framework. I also wanted to make a digital version-of-sorts of the board game Captain Sonar ([rules](https://www.matagot.com/IMG/pdf/SONAR_RULES_EN_lr.pdf))

## Description

This is a digital version-of-sorts of the board game Captain Sonar, an realtime game of submarine warfare ([rules](https://www.matagot.com/IMG/pdf/SONAR_RULES_EN_lr.pdf)). It is to be run on two computers. It uses a peer to peer connection to send and receive information about actions that the submarines are taking. 

*NOTE: I have a **white** and a **black** computer that I used in developing and testing this software. There will be references to **white**/**black** on this page. Those computers are what I am referring to*

## How to Run

On both the white and black computer:

* Run main.py
* You will see this prompt: `white or black computer? [w, b] > `
* Enter: `w` for white or `b` for black
* Click the new window that opens
* You might have to wait a little bit

### Error the Terminal when Attempting to Run?

On both the white and black computer try this:

* Trash the terminal and exit the game window
* Wait a little while
* Then retry running

## How to Play

### Objective

You must be the last sub alive (i.e. with at least one heart).

You can take damage from the reactor overheating, or from getting hit by a torpedo.

### Radio and Targeting

The red mark and trail show the movement of the enemy. You may use W, A, S, D or UP, DOWN, LEFT, RIGHT keys to move the red mark + trail. You want to use the knowledge of where they have been to try to line up where they are.

If you choose to fire a torpodo, **it will fire at the red mark**.

### Torpedo

To fire a torpedo, select the **crosshair button** and then select **MARK!**.

Your sub can fire a torpedo at the ememy, damaging them. If you hit around them (i.e. one spot in the N, S, E, W, NE, SE, SW, or NW direction), then you deal one heart of damage. If you hit them at their location, then you deal two hearts of damage.

### Movement and Reactor

To move, select a **valid direction** and then select **MARK!**.

Moving causes your torpedo to charge up.

Move to avoid the reactor overheating. 

The reactor will tick up throughout the game. If the reactor is at three and ticks again, it will go back to zero, but you will take damage. The reactor must be at at least one in order for you to move.

#### Valid Directions

You may **not** select a direction that would cause you to more **into an island**, **into your own trail**, or **outside of the play area**.

## Demo

Here is a demonstration of the software.

[Software Demo Video](https://youtu.be/miNvWQY6qdo)

# Network Communication

I used a **peer to peer** with **TCP** format for the networking side of this program. Each computer runs a server socket and a client socket. The server socket runs on a separate thread (`RadioOpperator` class) and is bound to **port 1500**. The client socket is within the `RedOctoberGame` class and is bound to **port 1501** and connects to port 1500 on the other computer. See a visual guide below on the peer to peer setup...

<img src="https://github.com/mbower00/The-Hunt-for-Red-October-Arcade/blob/master/assets/socket_visual.png" width="360" height="180" alt="Visual showing the peer to peer connection. Can be found here: https://github.com/mbower00/The-Hunt-for-Red-October-Arcade/blob/master/assets/socket_visual.png">

The messages sent between the computers are in the format of a JSON string encoded to bytes. Here is an example of a message that might be sent:

`{'position': [250.0, 190.0], 'move_log': [0, 20.0], 'torpedo_position': None}`

If we just received this, we could tell a number of things about our opponent...
* The opponent just moved North
    * From a positive value in the *y* position for the value of `'move_log'`
* The opponent is at coordinate: `[250.0, 190.0]`
    * From the value of `'position'` 
* The opponent did not fire a torpedo
    * From the value of `'torpedo_position'` is `None`)

# Development Environment

## Tools

* **Visual Studio Code** - A code editor with extensions that I used
* **Aseprite** - A pixel art engine
* **Coolors** - A color palette generator 

## Language 

* **Python** - I used the Python programming language for this project. Python is a language that has many libraries which helped me in the development of this software.
* **Markdown** 

## Libraries

* **arcade** - A game framework which has, among other things, the capability of pulling up a window with images that can move around.
* **socket** - A helpful library for providing a connection between two computers
* **threading** - A helpful library that I used to create a thread for a socket, so that it can be run apart from the main program. I used it to create a lock. 
* **json** - a helpful library for JSON and the conversion from a Python Dictionary to JSON.
* **random** - helpful for getting numbers
* **dataclasses** - Not sure if I am/need to be using this, but I pip installed it as part of an [Arcade tutorial](https://realpython.com/arcade-python-game-framework/)
* **PyObjC arcade** - Not sure if I am/need to be using this, but I pip installed it as part of an [Arcade tutorial](https://realpython.com/arcade-python-game-framework/)

# Useful Websites

* [realpython](https://realpython.com/python-sockets/)
* [realpython](https://realpython.com/arcade-python-game-framework/)
* [realpython](https://realpython.com/instance-class-and-static-methods-demystified/)
* [realpython](https://realpython.com/platformer-python-arcade/)
* [stackoverflow](https://stackoverflow.com/questions/23267305/python-sockets-peer-to-peer)
* [stackoverflow](https://stackoverflow.com/questions/10672419/class-constants-in-python)
* [docs.python](https://docs.python.org/3/reference/compound_stmts.html#with)
* [docs.python](https://docs.python.org/3.6/library/socket.html)
* [docs.python](https://docs.python.org/3/library/json.html)
* [w3schools](https://www.w3schools.com/python/python_inheritance.asp)
* [w3schools](https://www.w3schools.com/python/python_classes.asp)
* [api.arcade](https://api.arcade.academy/en/latest/)
* [api.arcade](https://api.arcade.academy/en/latest/examples/sprite_move_keyboard.html?highlight=input%20key)
* [api.arcade](https://api.arcade.academy/en/stable/api/drawing_utilities.html)
* [api.arcade](https://api.arcade.academy/en/latest/api/physics_engines.html)
* [api.arcade](https://api.arcade.academy/en/stable/_modules/arcade/drawing_support.html#color_from_hex_string)
* [geeksforgeeks](https://www.geeksforgeeks.org/python-strings-decode-method/)
* [geeksforgeeks](https://www.geeksforgeeks.org/python-interconversion-between-dictionary-and-bytes/)
* [geeksforgeeks](https://www.geeksforgeeks.org/difference-between-__sizeof__-and-getsizeof-method-python/)
* [coolors](https://coolors.co/143b49-9e342b-e79805-e5dada-02040f)
* [delftstack](https://www.delftstack.com/howto/python/python-b-in-front-of-string/)
* [delftstack](https://www.delftstack.com/howto/python/static-class-python/)
* [tutorialspoint](https://www.tutorialspoint.com/Peer-to-Peer-Computing)
* [mathcs](https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html)
* [markdownguide](https://www.markdownguide.org/cheat-sheet/)
* [markdownguide](https://www.markdownguide.org/basic-syntax/#images-1)
* [markdownguide](https://www.markdownguide.org/hacks/#image-size)
* [SONAR_RULES (not name of site)](https://www.matagot.com/IMG/pdf/SONAR_RULES_EN_lr.pdf)
* [wikipedia](https://en.wikipedia.org/wiki/Torpedo#/media/File:Mark_8_torpedo_in_Germanton_Park.jpg)

# Future Work

* Make the island configuration change.
* Sometimes, a couple reactor sprites seem to jump down and the back up (FIX THIS). 
* Add mines that the player can drop and detonate to damage the opponent
* Add a max range to the torpedo
* Add the capability of hitting your own ship if detonations are too close.
* Add a way to restart the game in the program
