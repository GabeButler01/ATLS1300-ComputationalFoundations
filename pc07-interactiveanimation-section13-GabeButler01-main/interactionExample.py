#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT???

@author: WHO ARE YOU??

WHAT DOES YOUR CODE DO???
"""

import turtle, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!

# click functions require TWO parameters
def clickCoord(x,y):
    '''When the user clicks, display the coordinates nearby'''
    turtle.goto(x,y) # go to the click location
    turtle.write("(" + str(x) + ", " + str(y) + ")") # print the coordinates as strings

# keypress functions have NO parameters
def changeBackgnd():
    '''When use presses a key, change the color of the background'''
    colors = ["lavender","darkseagreen","mistyrose","slateblue"]
    panel.bgcolor(random.choice(colors))
    
# ================ ANIMATION LOOP =========================
# Click interactions don't go inside the loop!

#These interactions are for the screen, NOT turtle...
panel.onclick(clickCoord) # when you click on the panel, move the turtle there
turtle.onkey(changeBackgnd,"b") #pass in the function and the letter assigned to the keypress

# For key presses ONLY, call BEFORE the animation loop!
panel.listen() # required to get the key press to work

# Loop is for animations
while running:
    
    # call functions and conditional statement to stop loop (if desired) 
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



