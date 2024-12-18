import random
from art import hl_logo as logo, vs
from hl_game_data import data

score = 0
not_wrong = True

def get_entry(data):
    ind = random.randint(0, len(data) - 1)
    return data.pop(ind)

def new_screen():
    print("\n" * 20)
    print(logo)

entry_a = get_entry(data)
entry_b = None

new_screen()

while not_wrong:
    entry_b = get_entry(data)
    print(f"Compare A: {entry_a['name']}, a(n) {entry_a['description']} from {entry_a['country']}")
    print(vs)
    print(f"Against B: {entry_b['name']}, a(n) {entry_b['description']} from {entry_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    correct_answer = "A" if entry_a['follower_count'] > entry_b['follower_count'] else "B"
    if guess == correct_answer:
        score += 1
        entry_a, entry_b = entry_b, None
        new_screen()
        print(f"You're right! Current score: {score}")
    else:
        not_wrong = False

new_screen()
print(f"Sorry, that's wrong. Final score: {score}")