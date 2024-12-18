import random
from hangman_words import word_list
from art import hangman_logo as logo, hangman_stages as stages

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

print(logo)

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed the letter '{guess}'. Guess again.")
    else:
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            print(f"You guessed the letter '{guess}', which is not in the word. You lose a life.")
            lives -= 1

            if lives == 0:
                game_over = True

                print(f"***********************YOU LOSE**********************\nThe correct word was: {chosen_word}")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(stages[lives])
