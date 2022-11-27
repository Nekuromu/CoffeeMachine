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


def report(money):
    for resource in resources:
        final_string = ""
        c_resource = resource.capitalize()
        resource_type = ""

        if resource == "water" or resource == "milk":
            resource_type += "ml"
        elif resource == "coffee":
            resource_type = "g"

        final_string += f"{c_resource}: {resources[resource]}{resource_type}"
        print(final_string)
    print("Money: $" + "{:.2f}".format(money))


def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins(_pennies, _nickles, _dimes, _quarters):
    total_cash = [_pennies, _nickles, _dimes, _quarters]

    for cycle in range(4):
        if cycle == 0:
            total_cash[cycle] = _pennies * 0.01
        elif cycle == 1:
            total_cash[cycle] = _nickles * 0.05
        elif cycle == 2:
            total_cash[cycle] = _dimes * 0.10
        elif cycle == 3:
            total_cash[cycle] = _quarters * 0.25
    return "{:.2f}".format(sum(total_cash))


def transaction(drink, money):
    money = float(money)
    drink_cost = MENU[drink]["cost"]

    if drink_cost > money:
        return 0
    else:
        money_back = money - drink_cost
        return money_back


def make_coffee(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    off = False

    while not off:
        money = 0
        user_prompt = ""
        has_resources = False

        while user_prompt != "espresso" and user_prompt != "latte" and user_prompt != "cappuccino" or not has_resources:
            user_prompt = input("What would you like? (espresso/latte/cappuccino): ")
            if user_prompt == "report":
                report(money)
            elif user_prompt == "off":
                return print("Goodbye!")
            else:
                has_resources = check_resources(user_prompt)

        pennies = int(input("How many pennies are you putting in?: "))
        nickles = int(input("How many nickles are you putting in?: "))
        dimes = int(input("How many dimes are you putting in?: "))
        quarters = int(input("How many quarters are you putting in?: "))
        money = process_coins(pennies, nickles, dimes, quarters)

        if user_prompt != "espresso" and user_prompt != "latte" and user_prompt != "cappuccino":
            print("ERROR: Input is incorrect.")
            break

        money = transaction(user_prompt, money)
        if money == 0:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            print(f"Here is ${money} dollars in change.")
            make_coffee(user_prompt)

    if not off:
        coffee_machine()


coffee_machine()
