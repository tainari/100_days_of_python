from turtle import Turtle, Screen

squirtle = Turtle()
screen = Screen()

def forward():
    squirtle.forward(10)

def back():
    squirtle.back(10)

def turn_left():
    squirtle.setheading(squirtle.heading()+10)
def turn_right():
    squirtle.setheading(squirtle.heading()-10)

def clear_screen():
    squirtle.reset()
    # squirtle.clear()

screen.listen()
screen.onkey(forward,key='w')
screen.onkey(back,key='s')
screen.onkey(turn_left,key='a')
screen.onkey(turn_right,key='d')
screen.onkey(clear_screen,key='c')

# def right():
#     squirtle.setheading(0)
#     squirtle.forward(10)
# def down():
#     squirtle.setheading(270)
#     squirtle.forward(10)
#
# def left():
#     squirtle.setheading(180)
#     squirtle.forward(10)
# def up():
#     squirtle.setheading(90)
#     squirtle.forward(10)
#
# def clockwise():
#     squirtle.circle(100)
#
# def counterclockwise():
#     squirtle.circle(100,-360)
#
# screen.listen()
# screen.onkey(fun=right,key='d')
# screen.onkey(fun=down,key='s')
# screen.onkey(fun=left,key='a')
# screen.onkey(fun=up,key='w')
# screen.onkey(fun=counterclockwise,key='q')
# screen.onkey(fun=clockwise,key='e')
#

screen.exitonclick()