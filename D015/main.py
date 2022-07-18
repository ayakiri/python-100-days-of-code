from menu import MENU
import os
import art

resources = {
    "water": {
        "value": 300,
        "unit": "ml",
    },
    "milk": {
        "value": 200,
        "unit": "ml"
    },
    "coffee": {
        "value": 100,
        "unit": "g"
    },
    "money": {
        "value": 0,
        "unit": "$"
    },
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def user_pick_drink():
    print(art.drinks)
    print("Available drinks in our machine: ")
    for drink in MENU:
        print(f'{drink.title()}: ${MENU[drink]["cost"]}')
    choice = input("\nWhat would you like to order? Input the name of the drink: ").lower()
    return choice


def print_report():
    print("Current resources: ")
    for key in resources:
        print(f"{key.title()}: {resources[key]['value']}{resources[key]['unit']}")
    print()


def serve_drink(drink):
    if check_resources(drink):
        if payment(MENU[drink]["cost"]):
            for ingredient in MENU[drink]["ingredients"]:
                resources[ingredient]["value"] = resources[ingredient]["value"] - MENU[drink]["ingredients"][ingredient]
            resources["money"]["value"] += MENU[drink]["cost"]
            print(f"Here is your {drink}, enjoy!")
    print("Order finished\n")


def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]["value"]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def payment(price):
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickles = int(input("Insert nickles: "))
    pennies = int(input("Insert pennies: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total >= price:
        change = round(total - price, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        short = price - total
        print(f"Sorry, you are ${short} short. Money refunded")
        return False


print(art.vending_machine)
power_on = True

while power_on:
    action = user_pick_drink()
    if action == "off":
        power_on = False
    elif action == "report":
        print_report()
    elif action == "clear":
        clear()
    elif action in MENU:
        serve_drink(action)

