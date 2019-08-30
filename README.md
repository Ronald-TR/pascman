# PASCMAN ᗧ ⚇

![version](https://img.shields.io/badge/pascman-v0.0.6-brightgreen.svg)

Using the native Python Curses library to create a simple plain text pacman that eat every text that you want :D

![pascman-example](https://github.com/Ronald-TR/pascman/blob/master/docs/pascman.gif)

*No external dependencies, just **python native code*** :snake:

## Installation

`pip install pascman`

and that's all! :snake:

## Usage commands
On terminal:

    pascman <flags|args> (optional) # or 
    python -m pascman <flags|args>

Type --help and you will see all the commands descriptions
```bash

pascman --help                                       

usage: main.py [-h] [--file [FILE]] [--aggressive] [--mask [MASK]]

Eat every text with pycman!! :D

optional arguments:
  -h, --help            show this help message and exit
  --file [FILE], -f [FILE]
                        path to a file
  --aggressive, -g      just an alias for --mask=*FUCK*OFF*
  --mask [MASK], -m [MASK]
                        choose the trace that pacman will be leave
```
Basically, are three options: 

`--file <path to a text file>`

`--aggressive or just -g <displays *FUCK*OFF*> in pacman trace`

`--mask <here, you set the trace, be creative>`

If you dont set a --file or a --mask, you will play a small example with the default options.

## Game commands

a -- left

d -- right

w -- up

s -- down

and:

CTRL+C -- quit

Only **AWSD** key inputs are allowed into the game curse screen.

Enjoy! :D
