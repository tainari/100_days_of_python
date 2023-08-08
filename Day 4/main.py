#rock-paper-scissors
import random
# art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
images = {"rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

user_outcomes = {
    "rock": {
        "scissors": "win",
        "paper": "lose",
        "rock": "draw"
    },
    "paper": {
        "rock": "win",
        "scissors": "lose",
        "paper": "draw"
    },
    "scissors": {
        "paper": "win",
        "rock": "lose",
        "scissors": "draw"
    }
}

options = ['rock', 'paper', 'scissors']
user_input = None
while not user_input:
    user_input = input("Please select rock, paper, or scissors.\n").lower().strip()
    if user_input not in user_outcomes:
        user_input = None
        print("Invalid input. Please try again.")

computer_input = options[random.randint(0,4)]

print(f"You chose {user_input}")
print(f"{images[user_input]}")
print()
print()

print(f"Computer chose {computer_input}")
print(f"{images[computer_input]}")
print()
print()

print(f'You {user_outcomes[user_input][computer_input]}')
