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
"""Default state of Coffe Machine"""
profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def sum_money(coffe_price):
    """Returns the profit """
    print("Please insert coins. 🪙")
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickles = int(input("How many nickles?")) * 0.05
    pennies = int(input("How many pennies ?")) * 0.01
    sum = quarters + dimes + nickles + pennies
    if sum < coffe_price:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        rest = round(sum - coffe_price, 2)
        print(f"Here is {rest} dollars in change.")
        return coffe_price


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_on = True

while is_on:
    # User choice
    choose = input("What would you like? (espresso/latte/cappuccino):")
    if choose == "report":
        # Show the current machine resources
        for i in resources:
            unit = "ml"
            if i == "coffee":
                unit = "g"
            print(f"{i}: {resources[i]}{unit}")
        print(f"Money: ${profit}")
    elif choose == "off":
        # Turn off machine
        is_on = False
    else:
        drink = MENU[choose]
        is_possible = is_resource_sufficient(drink["ingredients"])
        old_profit = profit
        if is_possible:
            profit += sum_money(drink["cost"])
            if profit != old_profit:
                make_coffee(choose, drink["ingredients"])
