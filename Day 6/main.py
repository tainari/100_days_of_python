from hangman_dict import get_word
from graphics import print_logo, print_gallows
import os

# generate secret word
secret_word = get_word().upper()
correct_letters = set(secret_word)
num_correct = 0

# generate answer array
answer = ["_"] * len(secret_word)

# generate lives and keep track of wrong guesses
already_guessed = set()
lives_used = 0
user_won = False

#print logo
os.system('clear')
print_logo()
input("Welcome to hangman! Press enter to begin.")

#start game loop
while lives_used < 7 and not user_won:
    os.system('clear')
    print_gallows(lives_used)
    print()
    print(" ".join(answer))
    print()
    # user makes a guess
    bad_guess = True
    while bad_guess:
        guess = input("Guess a letter: ").upper()
        if guess not in already_guessed:
            already_guessed.add(guess)
            bad_guess = False
        else:
            print("You guessed that already. Guess again!")
    #check if guess in word
    if guess in correct_letters:
        #if yes add to word and add # correct letters
        for n, ch in enumerate(secret_word):
            if ch == guess:
                answer[n] = ch
                num_correct += 1
        #then check if complete
        if num_correct == len(secret_word):
            user_won = True
    else:
        #take away number of lives
        lives_used += 1
        #check if dead happens at top of loop

    #clear screen and print current status

if user_won:
    print("You win!")
else:
    print("You lose :(")