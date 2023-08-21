from menu import recipes

class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def get_user_choice(self):
        user_options = {"espresso", "latte", "cappuccino", "report", "register", "off"}
        user_wants = None
        while not user_wants:
            user_wants = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
            if user_wants not in user_options:
                print("Please enter a valid input.")
                user_wants = None
        return user_wants
    def check_resources(self,user_selection):
        for resource in self.resources.keys():
            if self.resources[resource] < recipes[user_selection][resource]:
                return resource
        return None

    def make_drink(self,user_selection):
        for resource in self.resources.keys():
            self.resources[resource] -= recipes[user_selection][resource]
        print(f"Enjoy your {user_selection} ☕️!")

    def print_report(self):
        for resource in self.resources.keys():
            print(f"{resource.capitalize()}: {self.resources[resource]}")

    def turn_off(self):
        quit()