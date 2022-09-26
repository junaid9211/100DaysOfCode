import os
import platform

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
    "money": 0
}


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Money: {money}$')


def process_coins(cost):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    if total_money >= cost:
        change = total_money - cost
        print("Here is ${c:1.2f} change".format(c=change))
        return cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def check_resources(coffee_name):
    ingredients = MENU[coffee_name]['ingredients']
    required_water = ingredients['water']
    required_coffee = ingredients['coffee']

    if required_water > resources['water']:
        print('Sorry there is not enough water.')
        return False
    elif required_coffee > resources['coffee']:
        print('Sorry there is not enough coffee.')
        return False
    if coffee_name != 'espresso':
        required_milk = ingredients['milk']
        if required_milk > resources['milk']:
            print('Sorry there is not enough milk.')
            return False
        else:
            return True

    else:
        return True


def deduct_resources(coffee_name):
    global resources
    ingredients = MENU[coffee_name]['ingredients']
    required_water = ingredients['water']
    required_coffee = ingredients['coffee']
    resources['water'] -= required_water
    resources['coffee'] -= required_coffee

    if coffee_name != 'espresso':
        required_milk = ingredients['milk']
        resources['milk'] -= required_milk


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        report()
    elif choice == 'off':
        # end the program
        is_on = False
    elif choice in ['espresso', 'latte', 'cappuccino']:
        coffee = MENU[choice]

        if check_resources(choice):
            money = process_coins(coffee['cost'])

            if money > 0:
                resources['money'] += money
                deduct_resources(choice)
                print(f'Here is your {choice} ☕️. Enjoy!')
    elif choice == 'clear':
        clear()
    else:
        print('Not a valid choice')
