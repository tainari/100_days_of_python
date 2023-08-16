"""
100 days of Python course
DAY 14
"""

############################### HIGHER OR LOWER ##############################
##  In this game, the user must guess which option, A or B, has more        ##
##  Instagram followers. If they guess right, they keep playing; if not,    ##
##  the game is over.                                                       ##
##  The game tracks current score and also user high score for that         ##
##  particular session.                                                     ##
##############################################################################

from random import choice
import os

# from art import logo, vs
from game_data import data
from game_actions import print_current_vs, get_user_choice, check_user_choice, end_current_game

# numbers to track scores
top_score = 0
current_score = 0

#choices for each option
A = None
B = None

playing = True

while playing:
    if B:
        A, B = B, choice(data)
    else:
        A = choice(data)
        B = choice(data)
    while A == B:
        B = choice(data)
    print_current_vs(A,B,current_score,top_score)
    user_choice = get_user_choice()
    not_wrong = check_user_choice(user_choice, A, B)
    if not_wrong:
        current_score += 1
    else:
        playing = end_current_game(current_score,top_score)
        if current_score > top_score:
            top_score = current_score
        current_score = 0

os.system('clear')