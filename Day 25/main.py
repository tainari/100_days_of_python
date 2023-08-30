import pandas
import turtle

screen = turtle.Screen()
screen.setup(width=725,height=491)
screen.bgpic("./blank_states_img.gif")
screen.title("State guesses.")

writer = turtle.Turtle()
writer.hideturtle()
writer.up()

state_locations = pandas.read_csv("50_states.csv")

states = state_locations["state"].to_dict()
states = {v:k for k,v in states.items()}
print(states)

correct_answers = set()
while len(correct_answers) < len(states):
    guess = turtle.textinput(f"{len(correct_answers)} / 50 states correct.","Guess a state: ").title()
    if guess == "Reload":
        try:
            past_states = pandas.read_csv("last_session.csv")
            print(past_states)
        except FileNotFoundError:
            pass
        else:
            for s in past_states.state:
                correct_answers.add(s.strip())
                guess_x = state_locations[state_locations.state == s].x
                guess_y = state_locations[state_locations.state == s].y
                writer.goto(int(guess_x), int(guess_y))
                writer.write(s, font="Courier", align="center")
    elif guess == "End":
        with open("last_session.csv","w") as f:
            f.write("state\n")
            for s in correct_answers:
                f.write(s + "\n")
        quit()
    elif guess in states:
        correct_answers.add(guess)
        guess_x = state_locations[state_locations.state == guess].x
        guess_y = state_locations[state_locations.state == guess].y
        writer.goto(int(guess_x),int(guess_y))
        writer.write(guess,font="Courier",align="center")

screen.mainloop()