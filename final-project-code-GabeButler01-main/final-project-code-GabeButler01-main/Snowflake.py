import turtle as t
import random

# setup the window with a background colour
panel = t.Screen()
panel.bgcolor("black")
panel.setup(width=600, height=600) 


t = t.Turtle()
t.speed(5)
t.pencolor("gold")
#set the variable numbers like branch numbers, sizes, angles, 
#and distance of gaps of the snowflake
sizes = [5, 6, 7, 8, 9, 10]
# pensizes = [2, 4, 6, 8, 10]
angles = [72, 60, 45]
branches = [2, 3, 4, 5]
branchSizes = [15, 30 ,45]
branchGaps = [6, 9, 12, 15, 18]
branchAngles = [30, 45, 60]


# class SnowFlake:
#     def __init__(self, size, x, y):
#         self.size = size
#         self.x = x
#         self.y = y
#         panel.onscreenclick(self.snowflake)
    
#         panel.update()    

#create the random snowflake shape 
def snowflake(size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(10*size)
    t.ht()
    angle = random.choice(angles)
    num = int(360/angle)
    branchNum = random.choice(branches)
    branchSize = random.choice(branchSizes)
    branchGap = random.choice(branchGaps)
    branchAngle = random.choice(branchAngles)
    for i in range(num):
        branch(size, branchNum, branchSize, branchGap, branchAngle)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.left(angle)
        t.forward(10*size)

# create random branch of the snowflake
def branch(size, branchNum, branchSize, branchGap, branchAngle):
    for i in range(branchNum):
        t.backward(branchGap)
        t.right(branchAngle)
        t.forward(branchSize)
        t.backward(branchSize)
        t.left(branchAngle*2)
        t.forward(branchSize)
        t.backward(branchSize)
        t.right(branchAngle)

        
snowflake(random.choice(sizes), 0, 0)

# leave the window open until click to close
panel.exitonclick()