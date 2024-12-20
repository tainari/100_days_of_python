import random
from turtle import Turtle, Screen
WIDTH = 500
HEIGHT = 400
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coords = [-75, -45, -15, 15, 45, 75]

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
user_bet = ""
valid_input = False
while not valid_input:
    user_bet = screen.textinput(title="Make your bets!",prompt="Which turtle will win?\nOptions: red, orange, yellow, green, blue, purple").lower()
    if user_bet in colors:
        valid_input = True

def create_turtles():
    turtles = []
    start_x = -WIDTH / 2 + 15
    for ind in range(6):
        turtle = Turtle(shape='turtle')
        turtle.color(colors[ind])
        turtle.penup()
        turtle.goto(x=start_x, y=y_coords[ind])
        turtles.append(turtle)
    return turtles
"""
Turtle race!
I like turtles.
"""
turtles = create_turtles()

at_finish = False
while not at_finish:
    winning_turtle = None
    for ind in range(len(turtles)):
        turtle = turtles[ind]
        rand_dist = random.randint(1, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= WIDTH / 2:
            at_finish = True
            winning_turtle = colors[y_coords.index(turtle.ycor())]
            break


if winning_turtle == user_bet:
    print("Hey, you won!")
else:
    print(f"Sorry - the {winning_turtle} turtle won. :(")

screen.exitonclick()