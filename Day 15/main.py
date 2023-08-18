from machine import *

#starting amounts
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0.

#coins: penny, nickel, dime, quarter

#program:
# print report - what resources it has left
# check if resources sufficient
# ask for quantity of each coin; check if it's enough money - refund, no drink if not.
# make drink and use up resources
# "Here is your _____ . Enjoy!"

while True:
    user_choice = user_input()
    if user_choice in ("espresso","latte","cappuccino"):
        insufficient_resource = check_if_low_resources(user_choice, resources)
        if not insufficient_resource:
            payment = accept_user_coins()
            sufficient_payment = check_sufficient_payment(payment,user_choice)
            if sufficient_payment:
                money_in = process_payment(payment,user_choice)
                money += money_in
                resources = make_drink(user_choice,resources)
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print(f"Sorry, there isn't enough {insufficient_resource}")
    elif user_choice == "report":
        for resource, value in resources.items():
            print(f"{resource.capitalize()}: {value}")
        print(f'Money: ${money:.2f}')
    else:
        turn_off()