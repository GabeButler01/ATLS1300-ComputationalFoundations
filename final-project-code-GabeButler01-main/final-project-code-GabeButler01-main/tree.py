# -*- coding: utf-8 -*-
"""
Created on Nov 21, 2021

@author: Gabe Butler (Hairong Li, and Erica Hung)

Generate different trees and stars (random combinations).

There are 3 styles of tree (mosaic, triangle, and circles)
There are 3 styles of star (regular, bubbles, and teardrop)

Color scheme for all scripts is black, white, and gold 
to create a clean color scheme that is color-blind friendly
"""


'''
TO DO LIST:
    - make other star styles (bubbles and teardrop)
    - create management class
'''

import turtle
import math
import random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
panel.bgcolor("white")

# ================ CLASSES =========================

class Star(turtle.Turtle):
    
    def __init__(self, posx, posy): 
       
        super().__init__()
        
        self.color("gold")
        
        self.regular(posx, posy)
        
    def regular(self,x,y):
        self.up()
        self.goto(x, y)
        self.down()
        
        self.color("gold")
        self.begin_fill()

        self.right(10)
        
        for i in range(5):
            self.forward(15)
            self.right(120)
            self.forward(15)
            self.left(48)

        self.end_fill()
        
    '''Other star styles go here'''

# draw the trees (all same size, just different styles)
class Tree(turtle.Turtle):
    
    def __init__(self, posx, posy):
        
        super().__init__()
        
        self.up()
        self.goto(posx, posy)
        self.down()
        
        style = random.randint(1,3)
        
        # randomly pick a tree style
        if style == 1:
            self.mosaic((posx - 25), (posy + 20))
            Star((posx+16), (posy+320))
            
        if style == 2:
            self.triangle((posx + 10), (posy + 20))
            Star((posx+13), (posy+320))

        if style == 3:
            self.circles((posx + 10), (posy + 20))
            Star((posx+16), (posy+320))
        
    # mosaic -- draw line, move up, draw slightly shorter line...
    def mosaic(self,x,y):
        count = 70
        self.up()
        self.goto(x, y)
        self.down()
        for i in range(35):
            self.pensize(2)
            self.forward(count)
            self.left(90)
            self.forward(4)
            self.left(90)
            count -= 1
            self.forward(count)
            self.right(90)
            self.forward(4)
            self.right(90)
            count -= 1
        panel.update()
        self.hideturtle()
    
    # triangle --  draw a filled in triangle     
    def triangle(self,x,y):
        self.up()
        self.goto(x, y)
        self.down()
        self.begin_fill()
        self.forward(35)
        self.left(98)
        self.forward(282)
        self.left(165)
        self.forward(282)
        self.left(97)
        self.forward(45)
        self.end_fill()
        panel.update()
        self.hideturtle()
        
    # circles -- draw a stack of circles that slowly decrease in size    
    def circles(self,x,y):
        radius = 36
        self.up()
        self.goto(x, y)
        self.down()
        for i in range(14):
            self.color("black", "white")
            self.begin_fill()
            self.circle(radius)
            self.end_fill()
            radius -= 2
            self.up()
            self.left(90)
            self.forward(20)
            self.right(90)
            self.down()
        panel.update()
        self.hideturtle()

class Stump(turtle.Turtle): # draw stumps
    
    def __init__(self, posx, posy):
        
        super().__init__()
        
        self.up()
        self.goto(posx, posy)
        self.down()
        self.stump(posx, posy)
        
    def stump(self, posx, posy):
        count = 1
        for i in range(8): # create 8 stumps
            for j in range(2): # draw the stump
                self.begin_fill()
                self.forward(20)
                self.left(90)
                self.forward(20)
                self.left(90)
                self.end_fill()
            count += 1 # track where the stump is
            Tree(self.xcor(), self.ycor())
            
            if count < 5: # if the stump is on the top row, the next stump goes next to it
                self.up()
                self.forward(200)
                self.down()
            if count == 5: # if the stump is at the end of the first row, move down
                self.up()
                self.right(90)
                self.forward(350)
                self.left(90)
                self.down() 
            if count > 5: # if the stump is in the second row, the next stump is to the left
                self.up()
                self.backward(200)
                self.down()
        panel.update()
        
stump = Stump(-310,30)
