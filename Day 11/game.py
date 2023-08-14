import os
from art import logo 

aces = {"AH", "AS", "AC", "AD"}

score_dict = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

def score_hand(hand):
    '''
    Score a hand, adjusting for Ace's variable value.
    Note that splitting the deck is not included at this time. 
    '''
    total = sum([score_dict[card[:-1]] for card in hand])
    a_in_hand = aces.intersection(hand)
    if total > 21 and a_in_hand:
        num_aces = len(a_in_hand)
        # If one ace, change value from 11 to 1 (i.e., subtract 10)
        if num_aces == 1:
            total -= 10
        else:
            soft_val = 10 + num_aces
            if total - (11 * num_aces) + soft_val > 21:
                #subtract points from aces, add back the number of aces
                #this = 11 * num_aces + num_aces = 10 * num_aces
                total -= (10 * num_aces)
            else:
                total -= (11 * num_aces)
                total += soft_val

            
        # if len(a_in_hand) == 2:
        #     if total - 21 > 10:
        #         # Aces both become 1, score from them goes from 22 to 2
        #         total -= 20
        #     else:
        #         # Other option: points change from 22 to 12 (subtract 10)
        #         total -= 10
    return total

def compare_hand(player_score,dealer_score):
    '''Compare the scores of the player & dealer to asses win, lose, draw
    '''
    status = None
    if dealer_score == 21:
        status = "lose"
    elif player_score == 21:
        status = "win"
    elif player_score > 21:
        if dealer_score > 21:
            status = "draw"
        else:
            status = "lose"
    else:
        if dealer_score > 21 or player_score > dealer_score:
            status = "win"
        elif dealer_score == player_score:
            status = "draw"
        else:
            status = "lose"
    return status

def show_status(player_hand, player_score, dealer_hidden_hand):
    '''
    Print player hand and score, and dealer's hidden hand (one card visible)
    '''
    os.system('clear')
    print(logo)
    print(f'Player hand: {" ".join(player_hand)}')
    print(f'Player score: {player_score}')
    print(f'Dealer hand: {" ".join(dealer_hidden_hand)}')


def show_open_status(player_hand, player_score, dealer_hand, dealer_score):
    '''
    Print player hand and score, and dealer's full hand
    '''
    os.system('clear')
    print(logo)
    print(f'Player hand: {" ".join(player_hand)}')
    print(f'Player score: {player_score}')
    print(f'Dealer hand: {" ".join(dealer_hand)}')
    print(f'Dealer score: {dealer_score}')
    
