# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:04:30 2021

@author: Gabe Butler
"""

import random, turtle
turtle.colormode(255)

# setting up the panel
panel = turtle.Screen()
w = 1200
h = 400
panel.setup(width=w, height=h)

sky = ((random.randint(100,135)), random.randint(180,206), random.randint(200,255)) # sky color
panel.bgcolor(sky) # set background color to sky

# create turtle that will draw rainbow
rainbow = turtle.Turtle()
rainbow.speed(0)
rainbow.up()
ROYGBIV = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # list that will hold RGB values of ROYGBIV
rings = 250 # radius of circles that will create rainbow
y = -420 # y position of where rainbow will be drawn
x = 280 # x position of where rainbow will be drawn
count = 0 # needed to keep track of colors in for loop

# create a list of random rainbow colors (most common R, G, and B values that put the color into the correct family)
ROYGBIV[0] = random.randint(210,255) # red R
ROYGBIV[1] = random.randint(0,100) # red G
ROYGBIV[2] = random.randint(0,100) # red B

ROYGBIV[3] = 255 # orange R
ROYGBIV[4] = random.randint(70,200) # orange G
ROYGBIV[5] = random.randint(0,30) # orange B

ROYGBIV[6] = random.randint(200,255) # yellow R
ROYGBIV[7] = random.randint(200,240) # yellow G
ROYGBIV[8] = random.randint(0,100) # yellow B

ROYGBIV[9] = random.randint(0,160) # green R
ROYGBIV[10] = random.randint(100,255) # green G
ROYGBIV[11] = random.randint(0,140) # green B

ROYGBIV[12] = random.randint(50,160) # blue R
ROYGBIV[13] = random.randint(150,240) # blue G
ROYGBIV[14] = random.randint(220,255) # blue B

ROYGBIV[15] = random.randint(0,70) # indigo R
ROYGBIV[16] = random.randint(0,100) # indigo G
ROYGBIV[17] = random.randint(140,255) # indigo B

ROYGBIV[18] = random.randint(100,150) # violet R
ROYGBIV[19] = random.randint(0,100) # violet G
ROYGBIV[20] = random.randint(200,255) # violet B

# draw rainbow
for colors in range(7):
    rainbow.color(ROYGBIV[count], ROYGBIV[count+1], ROYGBIV[count+2])
    rainbow.up()
    rainbow.goto(x,y)
    rainbow.down()
    rainbow.begin_fill()
    rainbow.circle(rings)
    rainbow.end_fill()
    rings = rings - 20
    y = y + 20
    count = count + 3

# draw sky colored circle to make rainbow look like a rainbow
rainbow.color(sky)    
rainbow.up()
rainbow.goto(x,y)
rainbow.down()
rainbow.begin_fill()
rainbow.circle(rings)
rainbow.end_fill()

# create turtle that will draw cloud
cloud = turtle.Turtle()
cloud.color("white")
cloud.speed(0)
cloud.up()
cloud.hideturtle()

numberOfClouds = random.randint(0,6) # select random amount of clouds that will appear

# draw clouds
for clouds in range(0,numberOfClouds):
    cloud.goto(random.randint(-600,30), random.randint(-150,200))
    radius = random.randint(20,50)
    cloud.down()
    bump = random.randint(4,7)
    for bumps in range(0,bump):
        cloud.begin_fill()
        cloud.circle(radius)
        cloud.end_fill()
        cloud.up()
        cloud.right(360/bump)
        cloud.forward(10)
        cloud.down()
    cloud.right(90)
    cloud.forward(40)
    cloud.left(90)
    cloud.begin_fill()
    cloud.circle(25)
    cloud.end_fill()
    cloud.up()
    
turtle.done()
    