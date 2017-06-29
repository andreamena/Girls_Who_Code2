from turtle import *
import math

# Name your Turtle.
#t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)
drea = Turtle()
### Write your code below:
def drawShape(turtle,sides,color):
    turtle.pencolor
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        drea.forward(50)
        drea.right(angle)
        drawnSides+=1

####################

# RUNNING PROGRAM
another = True


while another==True:
    print("How many sides do want your shape to have?")
    numSides = int(input())
    choseColor = input()
    drawShape(drea,numSides,choseColor)
    
    print("Do you want another shape?")
    answer = input()
    if (answer == "no"):
        another=False
        
    print("What color do you want your shape to be")
    chosenColor = input()

drea = Turtle()
drea.turtlesize(2,2)
drea.pensize(5)
drea.pendown()
    


# Close window on click.
exitonclick()
