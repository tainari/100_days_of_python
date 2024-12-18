import random
from art import guess_the_number_logo as logo

lives = 10
print(logo)

keep_playing = True
while keep_playing:
    target_number = random.randint(1, 100)
    print("\n" * 20)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Do you want to play easy or hard? ")
    if level == "easy":
        lives = 10
    else:
        lives = 5
    guess = -1
    while guess != target_number and lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < target_number:
            lives -= 1
            print("Your guess is too low.\nGuess again.")
        elif guess > target_number:
            lives -= 1
            print("Your guess is too high.\nGuess again.")
        else:
            print(f"That's right! The number is {target_number}.")
    if lives == 0:
        print(f"You lose! The number was {target_number}.")
    keep_playing = input("Do you want to play again? (y/n) ").lower()[0] == 'y'
