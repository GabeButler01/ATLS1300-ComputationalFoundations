#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 1, 2021

@author: Gabe Butler

WHAT DOES YOUR GAME DO?
    OBJECTIVE - Click on the shape that DID NOT dissapear (or randomly guess).
    RULES - Observe the shapes/colors (all color-blind friendly), then remember the three that 
    disappeared, 4 options will appear and the user must click the shape that didn't disappear
    CHALLENGE - Memorizing everything quickly.
    INTERACTIONS - Clicking to submit your guess.

"""

import turtle
import time, random
import sys

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
panel.bgcolor((253, 255, 247))

#set up images for game

colors = [(80, 81, 79), (180, 173, 234), (89, 255, 160), (255, 237, 101), (0, 175, 185), (255, 81, 95), (167, 68, 130)] # all potential colorblind friendly colors
shapes = ['circle', 'square', 'triangle', 'turtle'] # all potential shapes
memory = [colors[random.randint(0,3)], shapes[random.randint(0,3)]] # remember the final choices for later (the first one is the correct option, but will be screambled later)

# ================ VARIABLE DEFINITION & SETUP =========================
running = True

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================ CLASSES =========================
class Options:
    def __init__(self, posx, posy):
        global colors
        global shapes
        
        self.color = colors[random.randint(0,6)]
        
        # set up images
        self.image = shapes[random.randint(0,3)]
        self.shape = turtle.Turtle(shape=self.image) # make a square turtle
        self.shape.shapesize(5,5)
        self.shape.color(self.color)
        
        # set a location for the button 
        self.location = (posx, posy)
        self.shape.up()
        self.shape.goto(self.location)
        

    # ======== METHODS DEFINITIONS ==========
    # remember: self comes first!
    
    def picked(self):
        global memory # remember the object's shape and color for later
        memory.append(self.color)
        memory.append(self.image)
        self.shape.color((253, 255, 247)) # make the shape color the same as the background
        
    panel.update()
        
# ================ OBJECTS =========================
# instantiate objects here

option1 = Options(-300,0)
option2 = Options(-100,0)
option3 = Options(100,0)
option4 = Options(300,0)

option5 = Options(-300,150)
option6 = Options(-100,150)
option7 = Options(100,150)
option8 = Options(300,150)

option9 = Options(-300,300)
option10 = Options(-100,300)
option11 = Options(100,300)
option12 = Options(300,300)

option13 = Options(-300,-150)
option14 = Options(-100,-150)
option15 = Options(100,-150)
option16 = Options(300,-150)

option17 = Options(-300,-300)
option18 = Options(-100,-300)
option19 = Options(100,-300)
option20 = Options(300,-300)

# put all objects into a list
optionList = [option1, option2, option3, option4, option5, option6,
              option7, option8, option9, option10, option11, option12, 
              option13, option14, option15, option16, option17, option18, 
              option19, option20]

# black square that will act as a transition
cover = turtle.Turtle()
cover.shape("square")
cover.shapesize(800,800)
cover.color("black")
cover.hideturtle()

# if you guess the correct option
def winner(x,y):
    # text that declares you won
    global running
    winner = turtle.Turtle()
    winner.up()
    winner.goto(0,280)
    winner.color((43, 192, 22))
    winner.write("WINNER", font=("Arial Rounded MT Bold", 70, "bold"), align=("center"))
    winner.hideturtle()
    running = False
    sys.exit() # end script when choice is made
    
# if you guess an incorrect option
        
def loser(x,y):
    # text that declares you lost
    global running
    loser = turtle.Turtle()
    loser.up()
    loser.goto(0,280)
    loser.color((239, 35, 60))
    loser.write("LOSER", font=("Arial Rounded MT Bold", 70, "bold"), align=("center"))
    loser.hideturtle()
    running = False
    sys.exit() # end script when choice is made
    
# ================ ANIMATION LOOP =========================

while running:
    # manipulate objects here    
    panel.update()
    
    time.sleep(15) # give time to look at the original image

    cover.showturtle() # make the screen back
    # pick the three objects that are going to be hidden
    hidden1 = random.randint(0,19) 
    hidden2 = random.randint(0,19)
    hidden3 = random.randint(0,19)
    
    # make sure the hidden objects are not going to be the same
    for i in range(10):  
        if(hidden1 == hidden2 or hidden1 == hidden3):
            hidden1 = random.randint(0,19)
        
        if(hidden2 == hidden3):
            hidden1 = random.randint(0,19)
            
    # hide the objects
    optionList[hidden1].picked()
    optionList[hidden2].picked()
    optionList[hidden3].picked()
    panel.update()
    
    time.sleep(0.5) # let the screen stay black for a little bit
    
    cover.hideturtle()
     
    panel.update() # update the window with everything drawn in a single frame
    
    time.sleep(5) # give the user some time to look at the new image
    
    # instead of clearing the panel, just cover it with a big square that is the same color as the background
    cover2 = turtle.Turtle()
    cover2.shape("square")
    cover2.shapesize(800,800)
    cover2.color((253, 255, 247))
    cover2.showturtle()
    
    # use attributes from memory to create 4 turtles
    correct = turtle.Turtle()
    correct.shape(memory[1])
    correct.color(memory[0])
    correct.shapesize(10,10)
    
    incorrect1 = turtle.Turtle()
    incorrect1.shape(memory[3])
    incorrect1.color(memory[2])
    incorrect1.shapesize(10,10)    
    
    incorrect2 = turtle.Turtle()
    incorrect2.shape(memory[5])
    incorrect2.color(memory[4])
    incorrect2.shapesize(10,10)  
        
    incorrect3 = turtle.Turtle()
    incorrect3.shape(memory[7])
    incorrect3.color(memory[6])
    incorrect3.shapesize(10,10)
    
    # randomize the positions of the 4 choices
    positions = [(-150, 0), (150, 0), (-150, -250), (150, -250)]
    
    correctpos = random.randint(0,3)
    correct.goto(positions[correctpos])
    positions.remove(positions[correctpos])
    
    incorrect1.goto(positions[0])
    incorrect2.goto(positions[1])
    incorrect3.goto(positions[2])
    
    panel.update()
    
    # ask the question
    text = turtle.Turtle()
    text.up()
    text.goto(0,200)
    text.write("what DID NOT disappear?", font=("Cookie", 40, "bold"), align=("center"))
    text.hideturtle()
        
    running = False
    
# different outcome depending on what the user clicks
correct.onclick(winner)
incorrect1.onclick(loser)
incorrect2.onclick(loser)
incorrect3.onclick(loser)

# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



