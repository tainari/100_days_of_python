from random import choices

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(cards, n):
    return choices(cards, k=n)

def print_player_hand(hand):
    hand_str = (", ").join([str(card) for card in hand])
    print(f"Player hand: {hand_str} (total: {sum(hand)})")

def print_dealer_hidden_hand(hand):
    print(f"Dealer's hand: {hand[0]}, __")

def print_dealer_open_hand(hand):
    hand_str = (", ").join([str(card) for card in hand])
    print(f"Dealer's hand: {hand_str} (total: {sum(hand)})")


# deal cards for player
player_hand = deal_cards(cards=cards, n=2)
# deal cards for dealer
dealer_hand = deal_cards(cards=cards, n=2)
# show hands
print_player_hand(player_hand)
print_dealer_hidden_hand(dealer_hand)
keep_playing = sum(player_hand) < 21 and sum(dealer_hand) < 21
while keep_playing:
    hit_me = input("Deal another card? (y/n): ").lower()[0] == "y"
    if hit_me:
        player_hand.extend(deal_cards(cards=cards, n=1))
        print_player_hand(player_hand)
        print_dealer_hidden_hand(dealer_hand)
        keep_playing = sum(player_hand) >= 21
    else:
        keep_playing = False

print("Final hands:")
print_player_hand(player_hand)
print_dealer_open_hand(dealer_hand)
if sum(player_hand) > 21:
    print("Dealer wins.")
elif sum(dealer_hand) > 21:
    print("Player wins!")
elif sum(player_hand) > sum(dealer_hand):
    print("Player wins!")
else:
    print("Dealer wins.")