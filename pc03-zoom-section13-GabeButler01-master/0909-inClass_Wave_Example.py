"""
Created on Thu Sep 10 12:58:10 2020

@author: Dr. Z
9/10 in class example code for drawing with data structures

"""
#============================
# 1. IMPORT LIBRARIES

from turtle import *  #import everything inside the turtle library
import math # import math, but keep it under the math library name.

#=============================
# 2. DEFINE VARIABLES
height = 100
offset = 100
ANGLES = range(0,360)

#=============================
# 3. DO STUFF!

# To access the math library use the name of the libarary followed by a dot then the function
# For us to use the sine wave we'll do:
    # math.sin()
# This function takes RADIANS, not DEGREES.
    
for angle in ANGLES:
    RAD = math.radians(angle)  # convert from degrees (0-360) to radians (0-2*pi)
    Y = height * math.sin(RAD) + offset # use the sine function to create a wave
    X = angle # move forward so it makes a wave, not a line
    goto(X,Y)
    
# Want to animate after the code runs?
# Comment out the next line (place a # at the beginning of the line)
done() # allows you to close your window by hitting the x. 
