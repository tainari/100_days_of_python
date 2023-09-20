# 100_days_of_python

This folder includes my progress in the 100 Days of Python code offered on Udemy!
Link to course: https://www.udemy.com/course/100-days-of-code/

## Day 1: Band Name Generator 🎸

Simple band name generator. Uses user input and string concatenation.

## Day 2: Tip Calculator 🧾

Simple tip calculator leveraging user input, type changing, and simple math.

## Day 3: Choose Your Own Adventure Game 🗺️

Treasure island game. Leverages user input and if statements.

## Day 4: Rock, Paper Scissors 🪨📄✂️

Rock, paper, scissors; leverages random module and user input.
I might come back later and do a "watch the computer play" option.
I made something like that (but sillier) on p5js: https://editor.p5js.org/tainari/sketches/h2urPZng2

## Day 5: Password Generator 🔑

Generates a password with a given number of letters, numbers, and symbols; uses random module.
Note: I went 'above and beyond' for this project by leveraging chr() and list comprehension.

## Day 6: Reeborg Hurdles 🏃🏻‍♀️

This exercise was completed on Reeborg. The code does not exist here.

## Day 7: Hangman 👻

This was a fun game to code! I went "above and beyond" by using requests.get to import a word list from MIT rather than
just using an array of words.

## Day 8: Caesar Cipher 🔐

Encryption and decryption using a standard Caesar cipher. Uses ord() and chr() to perform shift.

## Day 9: Secret Auction 👩‍⚖️

Skipped this one - it just seemed really boring; I know dictionaries well enough already.

## Day 10: Calculator 🧮

Created a calculator app. Went "above and beyond" by including exponent. In the future, may add square root (& single
number support)
as well as parsing longer chains of inputs (e.g., "2 + 4 * 8").

## Day 11: Blackjack 🂡🂭

Coded up a simplified version of blackjack. Went "above and beyond" by including varying deck size and shuffling the
deck.
Future versions may include splitting the player's hand in the case of multiple Aces.

## Day 12: Guess the Number #️⃣

A simple number guessing game.

## Day 13: Debugging 🐛

This exercise was done on an external platform.

## Day 14: Higher Lower ⬆️⬇️

A game where the user must guess who has a higher instagram following.
I'd like to come back and pull live instagram data, if possible, in the future!

## Day 15: Coffee Machine ☕️

A coffee machine! Takes money, makes change, checks, depletes, and reports resources, and makes coffee. Also turns off!
A more advanced iteration will take into account whether the machine can make change.

## Day 16: OOP Coffee Machine ☕️☕️☕️

Updated coffee machine! Rather than using the course's OOP version, I created my own based on Day 15's.
I also added the more advanced iteration, which checks if the machine can make change.
For example, if the register is empty and a user pays 5 quarters and 3 dimes for a $1.50 espresso, they're told the
machine can't make change.

## Day 17: Quiz Game 🤔

True-or-false quiz game with twelve questions, focused on OOP. Added some answer verification.
(Updated to be more OOP-focused and with external question bank)

## Day 18: Million-Dollar Artwork 🎨

Created Damien-Hirsch-esque dot art. Improved on expected output of project by not hardcoding the colour palette.

## Day 19: Turtle Race! 🐢

A simple game with six racing turtles, including betting by the user on which turtle will win.

## Day 20 & 21: Snake 🐍

Letting go of the long-held jealousy that I had a Motorola when my friends had Nokias by creating this game using the
Turtle package.
Implemented slightly differently than tutorial by using grid-based food placement rather than Turtle distance.
Future updates might ensure that food spawns in locations that are not occupied by snake.
Updated 8/28 with high score saving functionality.

## Day 22: Pong 🏓

The classic game, implemented using Python's Turtle package. Originally coded focusing on heading changes (turning by 90
degrees on impact), but the bouncing behaviour was janky, so switched to the tutorial's method of movement and bouncing.

## Day 23: Frogger (but with a turtle) 🐸🚗

Implemented without use of tutorial. Future updates: making sure that the cars don't overlap.

## Day 24: Mail Merge 📨

Basic file read / write

## Day 25: United States Guessing Game 🗺️

Game to guess all 50 states. I'm stuck at 32 on my own playthrough!

## Day 26: NATO Alphabet 💃

Review of list and dictionary comprehension. Added some functionality for non-alpha characters in user string.

## Day 27: Miles to Kilometers Converter 🔄

TKinter-based miles-to-kilometers converter. Future funcionality may include dropdown of conversion options.

## Day 28: Pomodoro Timer 🍅

TKinter-based pomodoro timer. Slightly updated approach to managing number of reps + resetting.

## Day 29: Password Manager 🗝️

TKinter-based password manager (write only). Generates password and writes it to a file.
Additional features in the future may include: overwriting previous passwords; retrieving passwords via GUI

## Day 30: Exception Handling 🙊

Implemented additional features in password manager, including retrieving passwords & data storage in JSON format.
JSON format also accounts for overwriting previous passwords! Thus, added additional functionality: ensuring that user
wants to overwrite password.
NOTE: The passwords and emails stored in the JSON are all fake. :)

## Day 31: Flashcard 🦉

Built my very own Duolingo. Changed functionality since I don't like the timed version; changed it to having a start
button that turns into a "show answer" button. In addition, show/hide correct/incorrect buttons depending on if question
or answer is being shown.
Note: I cannot for the life of me figure out how to get the thin line around the buttons to go away when they're hidden.
Additional functionality to develop: showing how many correct / total in a session; keeping track of how "well known"
each word is by a user.

## Day 32: Automated birthday emails 🎁

A quick program to send automated emails if it's somebody's birthday. First use of smtplib library, and also first use
of Python Anywhere!

## Day 33: ISS Overhead 💫

A quick program to email the user (me!) if the ISS is within 5 degrees of NYC and it's night (so that it's visible).
First use of APIs. Relies on a while loop + sleep for 60 seconds to check every minute — it would be better to deploy
it on a server and run every minute instead!

## Day 34: Quiz Game, with GUI! 👈🧐

Expansion of Day 17's quiz game using TKinter GUI and proper API connection to get questions.

## Day 35: SMS Rain Notifications ☔️

Created a script that runs at 6:30am every day and sends a text to my personal number if it's going to rain in NYC