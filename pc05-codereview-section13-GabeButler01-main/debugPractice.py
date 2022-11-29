#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 09:39:40 2021

@author: sazamore and Gabe Butler

This script (code that performs actions) will help you learn how to debug 
your code, or someone else's! Run the code and read the error report
and try to find the error. 

                        There are 6 bugs in this code. 
                     *** 1 bug will not throw a error! ***

Errors come up as the code executes, so bugs earlier in the code will throw 
errors first. Look for typos, indentation and capitalization mistakes!

Later, we'll use the code to investigate how to work with if statements.
You may use parts of code in your programming challenges, but please
cite it ("Borrowed/modified from Dr. Z's code.")
"""
import turtle, random


# ================ set up ======================
turtle.colormode(255) # accept RGB color values between 0 and 255
#turtle.tracer(0)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# ================ define variables =============
queenBlue = (87, 117, 144)
palette = [(243, 202, 64),(242, 165, 65),(240, 138, 75),(215, 138, 118)]
# from coolors.co colors are:
    # maize crayola
    # yellow orange
    # mango tango
    # middle red

# choose colors to work with (changes with each run of the code)
color1 = random.choice(palette)
color2 = random.choice(palette)
# NameError (palette spelled incorrectly)
color3 = random.choice(palette)    

squiggles = turtle.Turtle(visible=False) # make a turtle invisible from the start!

# ================== do tasks ===================
# NameError (capitalization of B was not there, making it not indicate the variable)
panel.bgcolor(queenBlue) # set background color
squiggles.color(color1) # set the first color of the line
squiggles.speed(10) # fast turtle!
squiggles.width(6) # lets make it thicc

# draw squiggles
# Silent error (if starting with a negative number, you must indicate when the range will end (0))
for i in range(-500,0):
    squiggles.forward(random.randint(4,9)) #move forward some random amount
    # IndentationError (needed to be lined up with for loop indentation)
    squiggles.left(random.randint(-70,70))
    
    # get x position of the turtle
    pos = squiggles.pos() # this is a tuple: (x,y)
    if pos[0] < 0:
        # on the left side  of the screen? Choose color 2
        squiggles.color(color2)
    # TypeError (pos["1"] won't do anything)
    elif -200 < pos[1] < 200:
        squiggles.color(color3)
    # SyntaxError (colon needed to be added)
    else:
        # otherwise, back to color 1
        squiggles.color(color1)
        
turtle.done()
