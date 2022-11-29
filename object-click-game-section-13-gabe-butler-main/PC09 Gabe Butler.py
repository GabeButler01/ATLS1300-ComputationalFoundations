#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 9, 2021

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
firstColor = colors[random.randint(0,len(colors)-1)]
firstShape = shapes[random.randint(0,len(shapes)-1)]
memoryColor = [firstColor] # remember the final choices for later (the first one is the correct option, but will be screambled later)
memoryShape = [firstShape]
positions = [(-150, 0), (150, 0), (-150, -250), (150, -250)]

# ================ VARIABLE DEFINITION & SETUP =========================
running = True

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================ CLASSES =========================
class Options(turtle.Turtle):
    def __init__(self, posx, posy):
        global colors
        global shapes
        
        super().__init__()
        
        self.imageColor = colors[random.randint(0,6)]
        
        # set up images
        self.image = shapes[random.randint(0,3)]
        self.shape(self.image)
        self.shapesize(5,5)
        self.color(self.imageColor)
        
        # set a location for the button 
        self.location = (posx, posy)
        self.up()
        self.goto(self.location)
        

    # ======== METHODS DEFINITIONS ==========
    # remember: self comes first!
    
    def picked(self):
        global memoryColor
        global memoryShape # remember the object's shape and color for later
        memoryColor.append(self.imageColor)
        memoryShape.append(self.image)
        self.color((253, 255, 247)) # make the shape color the same as the background
        
    panel.update()
        
class FinalChoices(turtle.Turtle):
    def __init__(self):
        global memoryColor
        global memoryShape
        global firstColor
        global firstShape
        global positions
        
        super().__init__()

        # as long as the correct answer is instantiated first, this creates 4 options
        self.shape(memoryShape[0])
        self.color(memoryColor[0])
        
        tempcolor = memoryColor[0]
        tempshape = memoryShape[0]
        
        self.shapesize(10,10)
        
        memoryColor.pop(0)
        memoryShape.pop(0)
        
        place = random.randint(0,len(positions)-1)
        self.goto(positions[place])
        positions.pop(place)
        
        if(tempcolor == firstColor and tempshape == firstShape):
            self.onclick(self.winner)
        else:
            self.onclick(self.loser)

    # if you guess the correct option
    def winner(x,y,z):
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
            
    def loser(x,y,z):
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
        
    
def run():
    # ================ OBJECTS =========================
    # instantiate objects here
    global running
    global memoryColor
    global memoryShape
    global colors
    global shapes
    
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

        for i in range(4):
            FinalChoices()

        panel.update()
        
        # ask the question
        text = turtle.Turtle()
        text.up()
        text.goto(0,200)
        text.write("what DID NOT disappear?", font=("Cookie", 40, "bold"), align=("center"))
        text.hideturtle()
            
        running = False

    # ================ CLEANUP =========================
    turtle.mainloop()  # allows for user interactions; handles cleanup
if __name__ == '__main__':
    run()


