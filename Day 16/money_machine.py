from menu import recipes

COINS = [
        ("quarter",0.25),
        ("dime",0.1),
        ("nickel",0.05),
        ("penny",0.01)
    ]

class MoneyMachine:
    def __init__(self):
        self.register = {
            "quarter": 0,
            "dime": 0,
            "nickel": 0,
            "penny": 0
        }
        self.total = 0
    def print_register_report(self):
        print(f"Total in register: ${self.total}")
        for coin, count in self.register.items():
            print(f"{coin}(s): {count}")
    def get_coins(self):
        coins_in = {
            "quarter": 0,
            "dime": 0,
            "nickel": 0,
            "penny": 0
        }
        for coin, coin_value in COINS:
            n_coins = None
            while n_coins is None:
                n_coins = input(f"How many {coin}s? ")
                try:
                    n_coins = int(n_coins)
                except (ValueError, TypeError) as error:
                    print("Please enter a valid number of coins.")
                    n_coins = None
                else:
                    if n_coins < 0:
                        print("Please enter a positive number.")
                        n_coins = None
            coins_in[coin] += n_coins
        return coins_in

    def calculate_total(self,coins_in):
        total_in = 0
        for coin, coin_value in COINS:
            total_in += coins_in[coin] * coin_value
        return total_in

    def check_total(self,total_in,price):
        return total_in >= price

    def make_change(self, change_needed, coins_in):
        track_change_needed = change_needed
        new_coins_in = {k:v for k, v in coins_in.items()}
        new_register = {k:v for k, v in self.register.items()}
        if track_change_needed > 0:
            for coin, coin_value in COINS:
                coin_surplus = track_change_needed // coin_value
                if new_coins_in[coin] >= coin_surplus:
                    new_coins_in[coin] -= coin_surplus
                    track_change_needed -= coin_surplus * coin_value

        if track_change_needed == 0:
            #all done!
            print(f"Here's your change of ${change_needed}!")
            return self.register, new_coins_in, True
        # if change is STILL needed, check register
        else:
            for coin, coin_value in COINS:
                coin_surplus = round(track_change_needed // coin_value, 2)
                if new_register[coin] >= coin_surplus:
                    new_register[coin] -= coin_surplus
                    track_change_needed -= coin_surplus * coin_value
        #final check! If you have enough coins in the register, then all good
        if track_change_needed == 0:
            print(f"Here's your change of ${change_needed}!")
            #return new dictionaries and a success flag
            return new_register, new_coins_in, True
        else:
            #otherwise, you can't make the change
            print("Sorry, the machine can't make change for you. Try again.")
            return self.register, coins_in, False
    def process_user_payment(self,user_selection):
        total_in = 0
        selection_price = recipes[user_selection]["price"]
        print(f"Please remit at least ${selection_price:.2f}")
        coins_in = self.get_coins()
        total_in = self.calculate_total(coins_in)
        sufficient_amount = self.check_total(total_in, selection_price)
        if not sufficient_amount:
            print("Sorry, that's not enough.")
            return False
        print(f"You've paid ${total_in:.2f}")
        change_needed = round(total_in - selection_price, 2)
        self.register, coins_in, change_success = self.make_change(change_needed,coins_in)
        if change_success:
            for coin, coin_value in COINS:
                self.register[coin] += coins_in[coin]
            self.total = self.calculate_total(self.register)