#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT?

@author: WHO ARE YOU?

WHAT DOES YOUR GAME DO?
    OBJECTIVE - 
    RULES -
    CHALLENGE - 
    INTERACTIONS - 

"""

import turtle
import time, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)

#set up images for game


# ================ VARIABLE DEFINITION & SETUP =========================
running = True

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================ CLASSES =========================
class RenameMe:
    def __init__(self):
        self.RenameThisAttribute = []
        # onclick functions get called here!
        
    # ======== METHODS DEFINITIONS ==========
    # remember: self comes first!

# ================ OBJECTS =========================
# instantiate objects here


# ================ ANIMATION LOOP =========================
# PRO-MOVES - can you get this while loop into a class? 
# You will have to for PC09.
while running:
    # manipulate objects here    
      
    panel.update() # update the window with everything drawn in a single frame
    
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



