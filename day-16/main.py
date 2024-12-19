from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# latte = MenuItem(name="latte",water=200,milk=150,coffee=24,cost=2.5)
# espresso = MenuItem(name="espresso",water=50,milk=0,coffee=18,cost=1.5)
# cappuccino = MenuItem(name="cappuccino",water=250,milk=100,coffee=24,cost=3.0)

#
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

more_coffee = True
while more_coffee:
    user_selection = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_selection == "off":
        more_coffee = False
    elif user_selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(user_selection)
        if coffee and coffee_maker.is_resource_sufficient(coffee) and  money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)