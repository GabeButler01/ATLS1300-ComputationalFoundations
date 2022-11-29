#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Gabe Butler
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.speed(0)

#space helmet
turtle.pensize(15)
turtle.goto(-15,0)
turtle.circle(135)


#laser
turtle.up()
turtle.goto(111, -90)
turtle.color(255,0,0)
turtle.down()
turtle.pensize(7)
turtle.goto(220,-100)

#alien
turtle.up()
turtle.goto(250, -80)
alienGreen = (108,196,23)
turtle.color("black", alienGreen)
turtle.pensize(3)
turtle.begin_fill()
turtle.down()
#alien body
turtle.forward(70)
turtle.right(45)
turtle.forward(40)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.goto(250, -80)
turtle.end_fill()
#left arm
turtle.up()
turtle.goto(230,-105)
turtle.down()
turtle.goto(220,-120)
#right arm
turtle.up()
turtle.goto(350,-109)
turtle.down()
turtle.goto(360,-124)
#left leg
turtle.up()
turtle.goto(270,-150)
turtle.down()
turtle.goto(270,-160)
#right leg
turtle.up()
turtle.goto(305,-150)
turtle.down()
turtle.goto(305,-160)
#alien face
turtle.up()
turtle.goto(260,-100)
turtle.down()
turtle.circle(4)

turtle.up()
turtle.goto(310,-100)
turtle.down()
turtle.circle(4)

turtle.up()
turtle.goto(270,-120)
turtle.down()
turtle.goto(300,-120)

#alien standing platform
turtle.up()
turtle.goto(400,-160)
turtle.color("black", "gray")
turtle.pensize(1)
turtle.down()
turtle.begin_fill()
turtle.goto(240,-160)
turtle.goto(240,-247)
turtle.goto(400,-247)
turtle.goto(400,-160)
turtle.end_fill()

#jeff the astronaut title
turtle.up()
turtle.goto(0,290)
turtle.write("Jeff Spazos", font=("Ariel",
                                    50, "normal"), align="center")

turtle.goto(0,-330)
turtle.write("THE DESTROYER!", font=("Ariel",
                                    50, "normal"), align="center")

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
