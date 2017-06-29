from turtle import *
import math 


#setup(500,500)
setup(500,500)


# FUNCTION
def drawShape(turtle,side,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
            turtle.forward(50)
            turtle.right(angle)
            drawnSides+=1
            
def forDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    angle = 360/sides

    for s in range(sides):
        turtle.forward(50)
        turtle.right(angle)


# RUNNING CODE
anah = Turtle()#creates turtle
anah.turtlesize(2,2) #makes turtle larger
anah.pensize(5) #makes pen larger
anah.pendown()

another = True

while another == True:

    print("How many sides do you want your shape to have?")
    numSides = int(input())

    print("What color do you want your shape to be?")
    chosenColor = input()

    forDrawShape(anah,numSides,chosenColor)
    print("Do you want to draw another shape?")
    answer = input()

    if(answer == "no"):
        another = False

#whileDrawShape(anah,4,"green")
#anah.penup()
#anah.forward(100)
#anah.pendown()
#forDrawnShape(anah,5,"pink")
#whileDrawShape(diana,5,red)


#closes the turtle window on click
exitonclick()
