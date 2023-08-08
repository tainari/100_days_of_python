##password generator
import random

#how many letters would you like
num_letters = None
while not num_letters:
    try:
        num_letters = int(input("How many letters would you like in your password?\n"))
    except ValueError:
        print("Please enter a valid integer.")

# how many symbols would you like
num_symbols = None
while not num_symbols:
    try:
        num_symbols = int(
            input("How many symbols would you like in your password?\n"))
    except ValueError:
        print("Please enter a valid integer.")

#how many numbers would you like
num_nums = None
while not num_nums:
    try:
        num_nums = int(
            input("How many numbers would you like in your password?\n"))
    except ValueError:
        print("Please enter a valid integer.")

password = [chr(random.randint(97,123)) if n % 2 else chr(random.randint(65,91)) for n in range(num_letters)]
symbols="!@#$%^&*()-_=+"
password.extend([symbols[random.randint(0,14)] for n in range(num_symbols)])
password.extend([str(random.randint(0,10)) for n in range(num_nums)])
random.shuffle(password)

print(f'Your password is {"".join(password)}')