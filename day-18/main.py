import random
from turtle import Turtle, Screen
import colorgram

CANVAS_DIMENSION = 800
PEN_SIZE = 20

#extract colours from image of choice
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


# Set up our toitle
timmy = Turtle()
timmy.pensize(PEN_SIZE)
timmy.shape("turtle")

# Set up our screen
screen = Screen()
screen.colormode(255)
screen.setup(width=CANVAS_DIMENSION, height=CANVAS_DIMENSION)


# turtle.teleport is in the docs but does not work for some reason
timmy.penup()
timmy.setposition(-CANVAS_DIMENSION/2 + 15,-CANVAS_DIMENSION/2 + 20)
timmy.pendown()

while timmy.ycor() < CANVAS_DIMENSION/2:
    while timmy.xcor() < CANVAS_DIMENSION/2:
        ind = random.randint(0, len(rgb_colors) - 1)
        timmy.pencolor((rgb_colors[ind][0], rgb_colors[ind][1], rgb_colors[ind][2]))
        timmy.pendown()
        timmy.forward(0)
        timmy.penup()
        timmy.forward(PEN_SIZE * 2)
    timmy.setposition(-CANVAS_DIMENSION/2 + 15,timmy.ycor() + PEN_SIZE * 2)

screen.exitonclick()