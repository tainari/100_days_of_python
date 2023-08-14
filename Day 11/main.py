"""
100 days of Python course
DAY 11
"""

################################ BLACKJACK ################################
##  This project allows the user to play blackjack on the command line.  ##
##  Note that it has somewhat simplified rules:                          ##
##  1) There is only one player and one dealer                           ##
##  2) Player cannot split aces - you play with just one hand.           ##
##  3) User can choose how many decks to play with                       ##
##  4) One ace in hand can be 11 or 1 (if total score > 21 with 11)      ##
##     Multiple aces count as 10 + A, or A, where A is num. aces in hand ##
##  5) Deck is reshuffled only at end of round (once winner declared),   ##
##     and only when the number of remaining cards < 40% of the original ##
##     number of cards in the deck.                                      ##
###########################################################################

import os
from art import logo
from deck import make_deck, shuffle_deck
from game import score_hand, show_status, compare_hand, show_open_status


#show logo
os.system('clear')
print(logo)

#make deck & discard
num_decks = None
while not num_decks:
    try:
        num_decks = int(input("How many decks would you like to play with? "))
    except ValueError:
        print("Must enter a number.")
        num_decks = None

deck = make_deck()
num_cards = len(deck)
discard = []
player_hand = []
dealer_hand = []
dealer_hidden_hand = []

keep_playing = True


#start play loop
while keep_playing:
    # deal hands
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hidden_hand = [dealer_hand[0],"_"]

    #calculate score of each hand
    # assume this version of program will not have splitting hands for the sake of initial sanity :)
    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)

    if dealer_score != 21:
        #show cards - both of player, first of dealer
        show_status(player_hand, player_score, dealer_hidden_hand)

        #ask if player wants another card
        want_another = True
        while player_score <= 21 and want_another:
            hit_me = input("Type y for another card, otherwise type n.\n")
            if hit_me != 'y':
                want_another = False
            else:
                player_hand.append(deck.pop())
                player_score = score_hand(player_hand)
                show_status(player_hand, player_score, dealer_hidden_hand)

        drama = input("Dealer turn... press Enter to continue.")
        show_open_status(player_hand, player_score, dealer_hand, dealer_score)
        
        # if dealer has score < 17, must take another card; show that dealer takes
        while dealer_score < 17:
            drama = input("Dealer must draw... press Enter to continue.")
            dealer_hand.append(deck.pop())
            dealer_score = score_hand(dealer_hand)
            show_open_status(player_hand, player_score, dealer_hand, dealer_score)
    else:
        show_open_status(player_hand, player_score, dealer_hand, dealer_score)
        print("\nDealer hit blackjack!")
    
    # compare hands
    win_status = compare_hand(player_score,dealer_score)

    # report results
    print(f'\nYou {win_status}.')

    # ask for another game
    play_answer = input(
        "\nWould you like to play another game?\nType y for yes and n for no.\n")
    
    if play_answer == 'n':
        keep_playing = False
    else:
        #move used cards to discard and reset hands
        discard.extend(player_hand)
        discard.extend(dealer_hand)
        player_hand = []
        dealer_hand = []
        # shuffle cards if the number of cards remaining in the deck is small
        if len(deck) < num_cards * 0.4:
            deck = shuffle_deck(deck, discard)
    os.system('clear')

