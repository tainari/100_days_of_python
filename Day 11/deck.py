import random

suits = ["H","S","C","D"]
values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def make_deck(num_decks = 1):
    '''
    Make a deck. Default is to deal out one deck but can do more.
    '''
    deck = []
    for s in suits:
        for v in values:
            deck.extend([f'{v}{s}' for _ in range(num_decks)])
    deck = shuffle_deck(deck)
    return deck

def shuffle_deck(deck,discard=[],hand1=[], hand2=[]):
    '''
    Shuffle the deck (add discard back in). in current iteration of game,
    do not shuffle in the middle of play since only
    two players and no ace splitting, but the option
    is there if needed.'''
    deck = deck + discard
    cards_in_hand = hand1+hand2
    for card in cards_in_hand:
        cards_in_hand.pop(cards_in_hand.index(card))
    random.shuffle(deck)
    return deck


