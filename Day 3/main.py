#treasure island game
#note that none of these have input control 
#this is according to specs

print("Welcome to Treasure Island.")
print("Your goal is to find the treasure.")
choice1 = input("You're at a crossword. Do you want to go left or right?\n").lower()
if choice1 == "right":
    print("Game over.")
    quit()
choice2 = input("You come to a lake. There is an island in the middle of the lake.\
                Type 'wait' to wait or 'swim' to swim.\n").lower()
if choice2 == "swim":
    print("Game over.")
    quit()
choice3 = input("You're XXX. Which door: red, blue, or yellow?\n").lower()
if choice3 == "red" or choice3 == "blue":
    print("Game Over.")
else:
    print("You win!")
