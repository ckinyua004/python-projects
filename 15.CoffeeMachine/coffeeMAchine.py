# Program Requirements
# 1. Print report.
# 2. Check resources sufficient.
# 3. Process coins.
# 4. Check transction succesful.
# 5.Make coffee

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        }, 
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

profit = 0

def print_report():
    print("Current resources: \n")
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}ml")
    print(f"Profit: ${profit:.2f}")

def check_resources(coffee_type):
    ingredients = MENU[coffee_type]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
    

user_coffee_input = input("What would you like: (espresso, latte, cappuccino)? \nor X to exit \n").lower()
while user_coffee_input != "x":
    user_coffee_input = user_coffee_input.strip()
    if user_coffee_input == "espresso" or "latte" or "cappuccino":
        check_resources(coffee_type=user_coffee_input)
        print(f"Selected coffee: {user_coffee_input.capitalize()}")
        if check_resources(user_coffee_input):
            print(f"Please insert coins for {user_coffee_input}: {MENU[user_coffee_input]["cost"]}$.")
            quarters = int(input("How many quarters? ")) * QUARTER
            dimes = int(input("How many dimes? ")) * DIME
            nickles = int(input("How many nickles? ")) * NICKLE
            pennies = int(input("How many pennies? ")) * PENNY
            
            total_money = quarters + dimes + nickles + pennies
            coffee_cost = MENU[user_coffee_input]["cost"]
            
            if total_money < coffee_cost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = total_money - coffee_cost
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                profit += coffee_cost
                for item in MENU[user_coffee_input]["ingredients"]:
                    resources[item] -= MENU[user_coffee_input]["ingredients"][item]
                print(f"Here is your {user_coffee_input}. Enjoy!")
        else:
            print("Sorry, we cannot make that coffee due to insufficient resources.")
    elif user_coffee_input == "report":
        print_report()
    else:
        print("Invalid input. Please choose from espresso, latte, or cappuccino.")