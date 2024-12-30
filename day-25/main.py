import csv
from turtle import Turtle, Screen, textinput

state_data = {}
with open("50_states.csv") as f:
    rd = csv.reader(f)
    next(rd)
    for r in rd:
        state_data[r[0].lower()] = {"x": float(r[1]), "y": float(r[2])}

current_score = 0

# Set up screen with map
screen = Screen()
screen.setup(width=725, height=500)
screen.bgpic("blank_states_img.gif")
screen.title("Name the States")

# Set up turtle
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.color("black")

# Function to write state name
def write_state_name(state):
    turtle.goto(state_data[state]["x"], state_data[state]["y"])
    turtle.write(state,move=False,align="center",font=("Courier", 12, "normal"))


while current_score < 50:
    guess = textinput(title=f"{current_score}/50 States Correct", prompt="What's another state name?").lower()
    if guess in state_data:
        current_score = current_score + 1
        write_state_name(guess)
        del state_data[guess]
    elif guess == "quit":
        break

for state in state_data:
    screen.title(f"Name the States - Final Score {current_score}")
    turtle.color('red')
    write_state_name(state)



screen.exitonclick()