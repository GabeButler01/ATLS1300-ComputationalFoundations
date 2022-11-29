#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:45:54 2021

@author: Erica, Hairong, Gabe

This code will create an animation with a 
ghost riding a skateboard. The ghost will
bounce between the left and ride side of 
the panel. When the ghost hits one side,
the panel will change to a random RGB color.

"""

# ====setting up libaries and turtle====

import turtle, random

turtle.colormode(255)
turtle.hideturtle()

panel = turtle.Screen()
turtle.bgcolor("purple")
w = 700
h = 500
panel.setup(width=w, height=h)

# ====defining and creating variables====

ghost = turtle.Turtle()
ghost.up()
ghost.goto(0,-110) # sending ghost to bottom of screen 
ghostImage = "giphy.gif"
ghostImageFlip = "giphyflip.gif"
panel.addshape(ghostImage)
panel.addshape(ghostImageFlip)

ghost.shape(ghostImage)
speed = 10

running = True

# ====defining and creating functions==== 

ghost.down()

for i in range(20):
    ghost.speed(i+1)

def randomColor():
    '''function will generate random RGB values'''
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    turtle.bgcolor(R, G, B)
    
# creating the animation loop
while running:
    ghost.up()
    ghost.forward(speed)
    xpos = ghost.xcor() # get x position
    
    if xpos >= w/2 - 100:
        ghost.right(180)
        ghost.shape(ghostImageFlip)
        randomColor()
        
        
    if xpos <= -1*w/2 + 100:
        ghost.right(180)
        ghost.shape(ghostImage)
        randomColor()

turtle.done()
    
    