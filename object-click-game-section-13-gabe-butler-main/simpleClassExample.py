#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 07:39:37 2021

@author: sazamore
"""
import turtle

turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

# Panel is defined BEFORE the class

panel = turtle.Screen() # global variable
w = 600 # global variable
h = 600 # global variable
panel.setup(width=w, height=h)

# a class is a template for your objects! 
# what do they do?
# what do they look like?
class Example:
    def __init__(self, Placeholder):
        # always pass self as 1st parameter!
        
        # attributes are variables inside classes/objects
        self.attribute1 = 0
        self.attribute2 = Placeholder
        self.drawer = turtle.Turtle()
        
    def someMethod(self):
        # always pass self as 1st parameter!
        self.attribute1 += 1 # classes can change values easily!
        
valueForPlaceholder = 10        

instanceExample = Example(valueForPlaceholder)
    # pass in an value to store to an attribute in the object!
print(instanceExample.attribute2)

# Uncomment to see how multiple objects can have different attribute values!
# aDifferentInstanceExample = Example(50)
# print(aDifferentInstanceExample.attribute2) # different values!
    
'''
REMEMBER:
    Attributes = variables inside a class/object
    Methods = functions inside a class/object
    Classes = templates for your object (like a factory!)
    Object = instance of a class (kind of like an iteration)
    
    Because it's an instance, you "instantiate" objects.
'''