
"""
Created on Mon Sep 13 21:44:36 2021

@author: Gabe Butler
"""

import math, turtle
turtle.colormode(255)
turtle.speed(10)
turtle.up()

# Circle background

circleRadii = [500,450,400,350,300,250,200,150,100,50]

greenValue = 20
x = (255, greenValue, 147)

turtle.color(x, x)

for radius in circleRadii:
    turtle.goto(0,(radius)*-1)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    greenValue = greenValue + 18
    x = (255, greenValue, 147)
    turtle.color(x, x)



# Funky spiral

#===Taken from https://canvas.colorado.edu/courses/75648/pages/parametric-patterns (Funky spiral)========#

turtle.color(0,204,204)

a = 24 # any number of your choice

b = 25 # any number of your choice

ANGLES = range(-1000,1000) # change this depending on your pattern!

for angle in ANGLES:
    angle = math.radians(angle) # overwrites input to radians (required!)
    X = angle - 1.6*math.cos(a*angle)
    Y = angle - 1.6*math.cos(b*angle)
#==========Original code below===========#
    x = X*20
    y = Y*20
    turtle.goto(x, y)
    turtle.down()
    
turtle.up()  

#===Taken from https://canvas.colorado.edu/courses/75648/pages/parametric-patterns (Funky spiral)========#
for angle in ANGLES:
    angle = math.radians(angle) # overwrites input to radians (required!)

    X = angle - 1.6*math.cos(a*angle)
    Y = angle - 1.6*math.cos(b*angle)
#==========Original code below===========#
    x = -X*20
    y = Y*20
    turtle.goto(x, y)    
    turtle.down()

turtle.done()