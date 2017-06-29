
from turtle import *
import math 

alex=Turtle()
alex.pensize(10)
alex.turtlesize(4,4)
pendown()

def drawShapes(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    sides = sides+1
    angle = 360/sides
    turtle.speed("slow") 
    while drawnSides < sides:
        turtle.forward(50)
        turtle.right(angle)
        drawnSides+=1
        

print("How many sides do you want your shape to have?")
numsides = int(input())

print ("What color do you want your shape to be?")
colorchosen=input()

drawShapes(alex,numsides,colorchosen)




exitonclick()
