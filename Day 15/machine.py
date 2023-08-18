from recipes import recipes

COINS = [
        ("quarter",0.25),
        ("dime",0.1),
        ("nickel",0.05),
        ("penny",0.01)
    ]

user_options = {"espresso","latte","cappuccino","report","off"}

def user_input():
    user_wants = None
    while not user_wants:
        user_wants = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        if user_wants not in user_options:
            print("Please enter a valid input.")
            user_wants = None
    return user_wants
def accept_user_coins():
    total = 0
    for coin, coin_value in COINS:
        n_coins = None
        while not n_coins:
            try:
                n_coins = int(input(f"How many {coin}s? "))
            except ValueError:
                print("Please enter a valid number of coins.")
        total += n_coins * coin_value
    print(f"You've paid ${total:.2f}")
    return total

def check_sufficient_payment(total_in,coffee_type):
    return total_in >= recipes[coffee_type]["price"]


def process_payment(total_in,coffee_type):
    price = recipes[coffee_type]["price"]
    change = total_in - price
    if change > 0:
        print(f'Your change is ${change:.2f}')
    return price

def check_if_low_resources(drink, resources):
    check = ["water","milk","coffee"]
    for resource in check:
        if resources[resource] < recipes[drink][resource]:
            return resource
    return False

def make_drink(drink,resources):
    for r in resources.keys():
        resources[r] -= recipes[drink][r]
    print(f"Enjoy your {drink} ☕️!")
    return resources

def print_report():
    pass

def turn_off():
    quit()