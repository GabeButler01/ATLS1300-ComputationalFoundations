# -*- coding: utf-8 -*-
"""
Created on Nov 21, 2021

@author: Gabe Butler (Hairong Li, and Erica Hung)

Generate different trees and stars (random combinations).

There are 3 styles of tree (mosaic, triangle, and circles)
There are 3 styles of star (regular, bubbles, and stick)

Color scheme for all scripts is black, white, and gold 
to create a clean color scheme that is color-blind friendly
"""

import turtle
import random

# ================ CLASSES =========================

class Star(turtle.Turtle):
    
    def __init__(self, posx, posy): 
       
        super().__init__()
        
        self.color("gold")
        
        starStyle = random.randint(1,3)
        
        
        
        if starStyle == 1:
            self.regular(posx, posy)
            
        if starStyle == 2:
            self.bubbles(posx, posy)
        
        if starStyle == 3:
            self.stick(posx, posy)
            
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
        
    def bubbles(self, x, y):
        centerX = x - 6
        centerY = y - 20
        self.up()
        self.goto(centerX, centerY)
        self.down()
        
        self.color("gold")
        self.begin_fill()
        
        # big center circle
        self.circle(15)
        self.end_fill()
        
        # second layer of circles
        
        # top circle
        self.begin_fill()        
        self.goto(centerX, centerY+27)
        self.circle(10)
        self.end_fill()
        
        # right top corner
        self.begin_fill()        
        self.goto(centerX+20, centerY+16)
        self.circle(10)
        self.end_fill()
        
        # left top corner
        self.begin_fill()        
        self.goto(centerX-20, centerY+16)
        self.circle(10)
        self.end_fill()
        
        # right bottom corner
        self.begin_fill()  
        self.up()
        self.goto(centerX+15, centerY-8)
        self.down()
        self.circle(10)
        self.end_fill()
        
        # left bottom corner
        self.begin_fill()        
        self.up()
        self.goto(centerX-15, centerY-8)
        self.down()
        self.circle(10)
        self.end_fill()
        
        self.hideturtle()
        
    def stick (self, x, y):
        xPos = x-6
        yPos = y -10
        self.up()
        self.goto(xPos, yPos)
        self.down()
        
        self.color("gold")
        
        self.pensize(10)
        
        self.left(90)
        
        for i in range(5):
            self.forward(15)
            self.up()
            self.goto(xPos, yPos)
            self.down()
            self.right(72)
        
# draw the trees (all same size, just different styles)
class Tree(turtle.Turtle):
    
    def __init__(self, panel, posx, posy):
        
        super().__init__()
        
        self.up()
        self.goto(posx, posy)
        self.down()
        
        self.panel = panel
        
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
        self.panel.update()
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
        self.panel.update()
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
        self.panel.update()
        self.hideturtle()

class Stump(turtle.Turtle): # draw stumps
    
    def __init__(self, panel, posx, posy):
        
        super().__init__()
        
        self.panel = panel
        
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
            Tree(self.panel, self.xcor(), self.ycor())
            
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
        self.panel.update()
        
class Manager:
    def __init__(self):
        self.panel = turtle.Screen()
        self.w = 800
        self.h = 800
        
        self.setup()
        
    def setup(self):
        turtle.colormode(255) # accept 0-255 RGB values
        turtle.tracer(0) # turn off turtle's animation
        
        self.panel.setup(width=self.w, height=self.h)
        self.panel.bgcolor("white")
        
        self.run()
        
    def run(self):
       Stump(self.panel,-310,30) 
        
if __name__=='__main__':
    Manager()
        
