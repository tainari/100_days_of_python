def set_level():
    '''
    Collects user input to select hard or easy game mode.
    '''
    level = None
    while not level:
        level = input("Choose a difficulty. Type easy or hard: ").lower().strip()
        if level not in ('hard','easy'):
            print("Please choose a valid option.")
            level = None
    return level

def set_guesses(level):
    guess_counts = {
        'easy': 10,
        'hard': 5
    }
    return guess_counts[level]

def guess_number():
    '''
    Returns user's inputted guess, checking that it's an int.
    '''
    guess = None
    while not guess:
        try:
            guess = int(input("Take a guess: "))
        except TypeError:
            print("Guess must be an integer. Your input was invalid. Try again.")
    return guess

def check_guess(user_guess, correct_number):
    if user_guess > correct_number:
        print("Too high.")
        return False
    elif user_guess < correct_number:
        print("Too low.")
        return False
    else:
        return True