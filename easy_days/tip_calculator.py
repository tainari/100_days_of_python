"""
This script is a simple tip calculator. Yay!
"""

print("Welcome to the tip calculator!")

# First get the input
invalid = True
while invalid:
    total_bill = input("What was the total bill? ")
    try:
        total_bill = float(total_bill)
    except ValueError:
        print("Please input a number.\n")
    else:
        invalid = False

invalid = True
while invalid:
    tip = input("How much tip would you like to give? 10, 12, or 15%? ")
    try:
        tip = float(tip.rstrip("%"))/100
    except ValueError:
        print("Please input a number.\n")
    else:
        invalid = False

if tip < 0.10:
    print("Minimum tip percent is 10. Rounding up.")
    tip = 0.10
elif tip > 0.15:
    print("Maximum tip percent is 15. Rounding down.")
    tip = 0.15

invalid = True
while invalid:
    num_people = input("How many people will split the bill? ")
    try:
        num_people = int(num_people)
    except ValueError:
        print("Please input a number.\n")
    else:
        invalid = False

total_per_person = (total_bill * (1+tip)) / num_people
total_per_person = "%.2f" % total_per_person
print(f"Each person should pay ${total_per_person}")