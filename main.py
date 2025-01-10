"""
Name: Raadhikka Gupta
Student Number: 400557687
Purpose: To create a visual representation of nails connected by 
string using Python's turtle graphics, allowing user input for nail 
positions and calculating the total cost of materials based on the 
number of nails and string length.
"""

# Import Statements.
import turtle
import math

# Constants Variables.
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Assignment 1"
BOARD_PRICE = 5
NAIL_COST_PER_PIECE = 0.12
STRING_COST_PER_METER = 0.07
PIXEL_PER_METER = 32

# Setting up the screen.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)
screen.bgcolor("#feeff5")

t = turtle.Turtle()

size = 30  # Size of each octagon side.
spacing = size * 2  # Spacing between octagons to avoid overlap.

# To make sure that the background is drawn instantly.
screen.tracer(0)

# To loop to cover the screen with octagons.
for y in range(SCREEN_HEIGHT // 2 + spacing, -SCREEN_HEIGHT // 2, -int(spacing)):
    for x in range(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 + spacing, int(spacing)):
        # To go the x, y coordinates
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor("#f0d6de")
        
        # Drawing one octagon.
        for i in range(8):
            t.forward(size)
            t.right(45)  
            
# To update and reset with the background, with original speed settings, and turtle back at origin.
screen.update()
t.penup()
t.goto(0, 0)
screen.tracer(1)

# To take the user's beginning input, number of nails and x,y coordinates.
numOfNails = screen.numinput("Number of nails", "How many nails would you like to pin?: ")
FirstXCoor = screen.numinput("X-Value of 1 nail", "What is the x-value of the 1 nail?: ")
FirstYCoor = screen.numinput("Y-Value of 1 nail", "What is the y-value of the 1 nail?: ")

# To go to the starting point, as entered by the user.
t.goto(FirstXCoor, FirstYCoor)
t.pendown()
t.dot(15, "#cd577b")
t.pensize(3)

# To record the previous x and y values, to determine the length of the string later.
prevXPos = FirstXCoor
prevYPos = FirstYCoor 
stringLength = 0

# Processing the drawing, and then Output it on the screen.
for i in range(2, int(numOfNails)+1):
    # User Input of the next x and y value
    xCoor = screen.numinput(f"X-Value of {i} nail", f"What is the x-value of the {i} nail?: ")
    yCoor = screen.numinput(f"Y-Value of {i} nail", f"What is the y-value of the {i} nail?: ")
    
    # To draw the string and the nail.
    t.penup()
    t.goto(xCoor, yCoor)
    t.pendown()
    t.dot(15, "#cd577b")
    t.pencolor("#490b25")
    t.goto(prevXPos, prevYPos)
    
    # To calculate the length of the string used.
    stringLength += math.sqrt((xCoor - prevXPos)**2 + (yCoor - prevYPos)**2) / PIXEL_PER_METER
    prevXPos = xCoor
    prevYPos = yCoor
    
# To complete the drawing by going back to the first point.
t.penup()
t.goto(prevXPos, prevYPos)
t.pendown()
t.goto(FirstXCoor, FirstYCoor)

# To add the length of the last bit of the string added.
stringLength += math.sqrt((FirstXCoor - prevXPos)**2 + (FirstYCoor - prevYPos)**2) / PIXEL_PER_METER
t.hideturtle()

# Outputing the total cost by calculating the cost and writing it onto the screen.
totalCost = BOARD_PRICE + (int(numOfNails) * NAIL_COST_PER_PIECE) + (stringLength * STRING_COST_PER_METER)
t.penup()
t.goto(230, -200)
t.pencolor("#390018")
t.write(f"Total cost: ${totalCost:.2f}", font=("Courier", 16, "bold"))

# To exit the screen.
screen.exitonclick() 
turtle.done()
