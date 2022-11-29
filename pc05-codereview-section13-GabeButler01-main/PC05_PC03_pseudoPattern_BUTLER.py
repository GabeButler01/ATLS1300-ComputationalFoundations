
"""
Created on Mon Sep 13 21:44:36 2021

@author: Gabe Butler
Edited by: Gabe Butler

Draws pink circle gradient background (dark to light) and parametric spiral
Edit: Spiral will be black to blue gradient

"""

import math, turtle
turtle.colormode(255)
turtle.speed(0) # no more animation
turtle.up()

# Circle background

radius = 500 # actively change radius instead of having list

greenValue = 20 # will update to create gradient
x = (255, greenValue, 147) # turtle color
turtle.color(x, x)

for i in range(10):
    turtle.goto(0,(radius)*-1)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    
    greenValue += 18 # use addition assignment
    x = (255, greenValue, 147)
    turtle.color(x, x)
    
    radius -= 50 # w/o list of radius, the radius will update inside for loop


# Funky spiral

# Modified from https://canvas.colorado.edu/courses/75648/pages/parametric-patterns (Funky spiral)

a = 24 
b = 25

ANGLES = range(-1000,1000)

count = 0 # track # of for loop runs to create spiral gradient

# start turtle as black but slowly update blue value to 255
blue = 0
turtle.color(0,0,blue)

for angle in ANGLES:
    angle = math.radians(angle)
    X = angle - 1.6*math.cos(a*angle)
    Y = angle - 1.6*math.cos(b*angle)
    x = X*20
    y = Y*20
    turtle.goto(x, y)
    turtle.down()
    count += 1
    
    if count % 8 == 0: # for loop runs 2000 times, so 2000/255 = 7.84
        blue += 1
        turtle.color(0,0,blue)

turtle.up()  

# Inverse of previous x-value (very similar but can't be combined into one loop)

count2 = 0
blue2 = 0
turtle.color(0,0,blue2)

# Modified from https://canvas.colorado.edu/courses/75648/pages/parametric-patterns (Funky spiral)
for angle in ANGLES:
    angle = math.radians(angle)
    X = angle - 1.6*math.cos(a*angle)
    Y = angle - 1.6*math.cos(b*angle)
    x = -X*20
    y = Y*20
    turtle.goto(x, y)    
    turtle.down()
    count2 += 1
    
    if count2 % 8 == 0: # for loop runs 2000 times, so 2000/255 = 7.84
        blue2 += 1
        turtle.color(0,0,blue2)

turtle.done()

'''
1. The code quality already was pretty good before edits (everything worked fine and was well commented + organized)
2. Optimization by using addition/subtraction assigment
3. Clearly seperates elements of code (circles and spirals), already was pretty DRY (no obvious tedious code), efficiently drew shapes with as few lines as possible
Upgrade: When originally writing this code, I wanted the spirals to have a gradient but I ended up getting a bad color sequence.
However, I was able to use an if statement to slowly increase the rgB value and achieved a black to blue gradient.
'''