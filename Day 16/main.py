from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

nespresso = CoffeeMaker()
nespresso_register = MoneyMachine()

while True:
    user_choice = nespresso.get_user_choice()
    if user_choice in ("espresso","latte","cappuccino"):
        insufficient_resource = nespresso.check_resources(user_choice)
        if not insufficient_resource:
            good_payment = nespresso_register.process_user_payment(user_choice)
            if good_payment:
                nespresso.make_drink(user_choice)
        else:
            print(f"Sorry, there isn't enough {insufficient_resource}")
    elif user_choice == "report":
        nespresso.print_report()
    elif user_choice == "register":
        nespresso_register.print_register_report()
    else:
        nespresso.turn_off()