from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drink_names = menu.get_items()
is_on = True

while is_on:
    choice = input(f"What would you like? ({drink_names}): ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        is_on = False
    elif choice in ['espresso', 'latte', 'cappuccino']:
        drink = menu.find_drink(choice)

        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            # process coins
            transaction_successful = money_machine.make_payment(drink.cost)
            if transaction_successful:
                coffee_maker.make_coffee(drink)


# Steps
# _TODO 1 prompt user for input
# TODO 2 if it is report then give report
# TODO 3 if it is off then turn off the machine
# _TODO 4 if it is any of the drink then check resources
# _TODO 5 process coins
#  deduct resources give the drink
