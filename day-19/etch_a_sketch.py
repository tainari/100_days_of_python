from turtle import Turtle, Screen

STEP_SIZE = 5

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(STEP_SIZE)

def move_backward():
    timmy.backward(STEP_SIZE)

def turn_left():
    timmy.left(STEP_SIZE)

def turn_right():
    timmy.right(STEP_SIZE)

def clear():
    timmy.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="space", fun=clear)



screen.exitonclick()