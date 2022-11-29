
'''
ATLS 1300
Author: Dr. Z
Spirograph example

READ FIRST! 

How to borrow code

    1. You MUST create a comment that says what the code you're borrowing does
    and where you got it from (ATLS1300 example code). 
    2. You MAY NOT copy this code or use this code as start code. 
    Only take what you need.
    3. Copy the sections between the ======= lines (lines 32-45, and/or, 
                                                    lines 51-70)
    And paste it in your code! 
    
    Do not take what you do not understand!
'''

import math, turtle #import the libraries of commands that you'd like to use
turtle.colormode(255)

panel = turtle.Screen().bgcolor('black') # set the background color to black.
turtle.color((80,80,200)) # set the turtle color using RGB values inside of a tuple
turtle.speed(10) # draw at the fastest speed
turtle.up() # pick up the pen

#===============================
#Circle spirograph (EASY!)
    
inc = 10 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of iterations to make a complete circle. 
innerCirc = 2 # radius of inner circle
radius = 50 # radius of circles drawn in pattern

turtle.goto(150,150) # center of the pattern

for iteration in range(numIt):
    # for loop creates a ring of overlapping circles--a spirograph!
    turtle.down()
    turtle.circle(radius)
    turtle.forward(innerCirc)
    turtle.right(inc)    
#=============================== 
# This section allows for clean execution of the code! (Ignore it)
turtle.up()    
 
#===============================
#Polygon spirograph (HARD!)

#set the size, number of sides, and internal angle of your shape that will make your spirograph
size = 50
sides = 4 # chage this to change the shape!
angle = 360/sides

inc = 10 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of iterations to make a complete circle. 
innerCirc = 20 # radius of inner circle

turtle.goto(-100,-50) # center of the pattern

for iteration2 in range(numIt):
    turtle.down()
    for iteration1 in range(sides):
        turtle.forward(size)
        turtle.right(angle)
    turtle.up()
    turtle.forward(innerCirc)
    turtle.right(inc)

    
# ================================
# Clean up!
turtle.done()
