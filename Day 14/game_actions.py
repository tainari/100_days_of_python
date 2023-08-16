import os
from art import logo, vs

def print_current_vs(A,B,current_score,top_score):
    os.system('clear')
    print(logo)
    if current_score > 0:
        print(f"You're right! Current score: {current_score}")
        print(f'Top score: {top_score}')
        print()
    print(f'Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}')
    print(vs)
    print(f'Against B: {B["name"]}, a {B["description"]}, from {B["country"]}')


def end_current_game(current_score,top_score):
    os.system('clear')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {current_score}")
    if current_score > top_score:
        print(f"You beat your previous top score of {top_score}!")
    else:
        print(f'You did not beat your current top score of {top_score}.')
    keep_playing = None
    while not keep_playing:
        keep_playing = input("Do you want to play again? Type y for yes or n for no. ").lower().strip()
        if keep_playing not in ('y','n'):
            print("Not a valid input.")
            keep_playing = None
        return keep_playing == 'y'

def get_user_choice():
    user_choice = None
    while not user_choice:
        user_choice = input("Who has more followers? Type A or B.: ").upper().strip()
        if user_choice not in ("A","B"):
            print("Invalid entry. Please try again.")
    return user_choice


def check_user_choice(user_choice, A, B):
    if user_choice == "A":
        if A["follower_count"] > B["follower_count"]:
            return True
        else:
            return False
    else:
        if B["follower_count"] > A["follower_count"]:
            return True
        else:
            return False
