import colorgram
from turtle import Turtle, Screen, colormode
from turtle_colours import colours
import random


palette = [[n for n in c.rgb] for c in colorgram.extract('hirst.jpg',10)]

timmy = Turtle()
colormode(255)
timmy.pensize(2)
timmy.speed(10)

dot_size = 20

screen = Screen()
screen.setworldcoordinates(-10, -10, screen.window_width() - 1, screen.window_height() - 1)
#
w = screen.window_width()
h = screen.window_height()

def go_right():
    while timmy.pos()[0] < w - dot_size:
        timmy.dot(dot_size,random.choice(palette))
        timmy.up()
        timmy.forward(1.5*dot_size)
        timmy.down()
def turn_left():
    timmy.up()
    timmy.left(90)
    timmy.forward(1.5*dot_size)
    timmy.left(90)
    timmy.forward(1.5*dot_size)
    timmy.down()

def go_left():
    while timmy.pos()[0] > -1:
        timmy.dot(dot_size,random.choice(palette))
        timmy.up()
        timmy.forward(1.5*dot_size)
        timmy.down()

def turn_right():
    timmy.up()
    timmy.right(90)
    timmy.forward(1.5*dot_size)
    timmy.right(90)
    timmy.forward(1.5*dot_size)
    timmy.down()

while timmy.pos()[1] < h:
    go_right()
    turn_left()
    go_left()
    turn_right()






screen.exitonclick()

##SPIROGRAPH
# num_circles = 10
# angle = 360/num_circles
# for _ in range(num_circles):
#     timmy.color(random.choice(colours))
#     timmy.circle(100)
#     timmy.right(angle)

#random walk
# DIRECTION_OPTIONS = [timmy.left, timmy.right]
# for _ in range(1000):
#     colour = random.choice(colours)
#     angle = random.randint(0,360)
#     direction = random.choice(DIRECTION_OPTIONS)
#     direction(angle)
#     timmy.color(colour)
#     timmy.forward(20)


#buncha shapes
# for n_sides in range(3,11):
#     angle = 360/n_sides
#     for side in range(n_sides):
#         timmy.forward(100)
#         timmy.right(angle)











