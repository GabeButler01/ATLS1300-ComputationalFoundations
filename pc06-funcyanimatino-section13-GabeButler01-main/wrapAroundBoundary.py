#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:20:00 2021

@author: Gabe Butler

A wraparound boundary, demonstrated with a ghost moving left
to right against a black background. Ghost crosses a boundary
10 times before stopping.
Ghost also will randomly float up and down
"""

import turtle, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================
ghost = turtle.Turtle(shape="circle")
size = 4
running = True # while loop conditional
step = 0.1 # increment of ball movement (controls speed of ghost), slow down ghsot
count = 0 # edge crossingcounter, to determin when to stop animating
crosses = 10 # number of edge crosses to stop after

# import and set image as turtle shape
ghostImg = "ghostgif.gif" # turtle library ONLY works with gifs!
panel.addshape(ghostImg) # save the image to the panel so it knows what to draw
ghost.shape(ghostImg) # change the turtle shape to the saved image

ghost.up() # we're not drawing, anymore

# ================ FUNCTION DEFINITION =========================
def fly():
    '''Make ghost randomly float up and down'''
    ghost.left(random.randint(0,2))
    ghost.forward(0.03)
    ghost.right(random.randint(0,2))
    ghost.forward(0.03)
# ================ ANIMATION LOOP =========================
while running:
    fly()
    ghost.forward(step) # move ghost
    xpos = ghost.xcor() # get x position
    
    if xpos >= w/2:
        # check if it crosses the RIGHT edge
        ghost.goto(-w/2,0) # move it to the left edge
        count += 1 # keep track of the crossing
        
    if count > crosses:
        # check if we've made the intened number of crosses
        running= False    
        
    panel.update() # update the window with everything drawn in a single frame
    
# CLEANUP
turtle.done()



