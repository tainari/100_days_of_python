"""
100 days of Python course
DAY 12
"""

############################ NUMBER GUESSING GAME ############################
##  In this game, the user must try to guess a number between 1 and 100.    ##
##  The user can choose to play in easy or hard mode.                       ##
##  Easy mode has 10 guesses.                                               ##
##  Hard mode has 5 guesses.                                                ##
##############################################################################

import random

from gameplay import set_level, guess_number, set_guesses, check_guess



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = set_level()
num_guesses = set_guesses(level)

# EASY_GUESSES = 10
# HARD_GUESSES = 5
# num_guesses = EASY_GUESSES if level == 'easy' else HARD_GUESSES

correct_number = random.randint(1,101)

player_won = False

while num_guesses > 0 and not player_won:
    print(f'You have {num_guesses} left to guess a number.')
    guess = guess_number()
    player_won = check_guess(guess,correct_number)
    num_guesses -= 1

if player_won:
    print("You guessed correctly. You win!")
elif num_guesses == 0:
    print("You ran out of guesses. You lose!")
    print(f'The correct number was: {correct_number}')
