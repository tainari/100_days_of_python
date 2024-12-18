from typing import List, Dict

def new_screen():
    print("\n" * 20)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coin_box = 0
#{
#     "penny": 0,
#     "nickel": 0,
#     "dime": 0,
#     "quarter": 0
# }

coin_values = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

def calculate_total_cash(coin_counts: Dict[str, int]):
    total_cash = 0
    for coin in coin_counts.keys():
        total_cash += coin_values[coin] * coin_counts[coin]
    return total_cash

def print_report():
    # cash = calculate_total_cash(coin_box)
    print(f"""
    Water: {resources['water']} mL
    Milk: {resources['milk']} mL
    Coffee: {resources['coffee']} g
    Money: ${coin_box:.2f}
    """)

def check_resources(drink_type):
    insufficient_resources = []
    for resource in resources:
        in_stock = resources[resource]
        needed = MENU[drink_type]["ingredients"].get(resource,0)
        if in_stock < needed:
            insufficient_resources.append(resource)
    return insufficient_resources

def get_coins():
    inserted_coins = {}
    print("Please insert coins:")
    inserted_coins["penny"] = int(input("Number of pennies: "))
    inserted_coins["nickel"] = int(input("Number of nickels: "))
    inserted_coins["dime"] = int(input("Number of dimes: "))
    inserted_coins["quarter"] = int(input("Number of quarters: "))
    return inserted_coins

def make_change(drink_type, coins):
    expected_amount = MENU[drink_type]["cost"]
    provided_amount = calculate_total_cash(coins)
    change = provided_amount - expected_amount
    return change

def deplete_resources(drink_type):
    for resource in resources.keys():
        resources[resource] -= MENU[drink_type]["ingredients"].get(resource,0)

while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type in ["espresso","latte","cappuccino"]:
        insufficient_resources = check_resources(coffee_type)
        if insufficient_resources:
            print(f"Sorry, you don't have enough {(' or ').join(insufficient_resources)}")
            continue
        inserted_coins = get_coins()
        change = make_change(coffee_type, inserted_coins)
        if change < 0:
            print("Sorry, that wasn't enough money.")
            continue
        else:
            coin_box += MENU[coffee_type]["cost"]
            deplete_resources(coffee_type)
            print(f"Here's your ${change:.2f} in change.")
            print(f"Here's your {coffee_type}! ☕️")

    elif coffee_type == "report":
        print_report()
    elif coffee_type == "off":
        print("Smell ya later! 💨")
        quit()
    else:
        print("Sorry, we are unable to recognize the coffee type. Please try again.")