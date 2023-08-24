from turtle import Turtle, Screen
import random

colours = ['red','yellow','orange','green','blue','purple']

screen = Screen()
WIDTH = 500
HEIGHT = 400
screen.setup(width=WIDTH,height=HEIGHT)

user_bet = screen.textinput("Place your bets",f"Which turtle will win?: {', '.join(colours)}").lower().strip()
# WIDTH = screen.window_width()
# HEIGHT = screen.window_height()

start_x = -WIDTH // 2 + 20
start_y = 130
turtles = []
for c in colours:
    t = Turtle(shape='turtle',visible=False)
    t.up()
    t.color(c)
    t.setx(start_x)
    t.sety(start_y)
    start_y -= 40
    turtles.append(t)

for t in turtles:
    t.showturtle()

winner = False
winning_colour = None
while not winner:
    for t in turtles:
        t.forward(random.randint(0,20))
        if t.xcor() >= WIDTH * 0.5 - 30:
            winner = True
            if winning_colour is None:
                winning_colour = t.pencolor()
print(f"Winning turtle is {winning_colour}")
if user_bet == winning_colour:
    print("You win!")
else:
    print("You lose :(")
screen.exitonclick()