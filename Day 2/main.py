#tip calculator 

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = float(input("What percent of tip would you like to give? 10, 12, or 15? "))
percent = 1 + (tip/100)
people = int(input("How many people should split the bill? "))
per_person = (total * percent) / people
print(f'Each person should pay ${per_person:.2f}')
