#This is progrom simulates a coffeMachine


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

def coffeeMachine():
    print("Welcome to the Coffee Machine!")
    print("What would you like? (espresso/latte/cappuccino): ")
    coffee = input()
#TODO: check for ingredients at this step  
    
    if coffee == "espresso":
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) # 0.25
        dimes = int(input("How many dimes?: ")) # 0.10
        nickles = int(input("How many nickles?: ")) # 0.05
        pennies = int(input("How many pennies?: ")) # 0.01
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if total >= MENU["espresso"]["cost"]:
            change = total - MENU["espresso"]["cost"]
            print(f"Here is your change: ${change}")
            print("Here is your espresso. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")
    elif coffee == "latte":
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) # 0.25
        dimes = int(input("How many dimes?: ")) # 0.10
        nickles = int(input("How many nickles?: ")) # 0.05
        pennies = int(input("How many pennies?: ")) # 0.01
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if total >= MENU["latte"]["cost"]:
            change = total - MENU["latte"]["cost"]
            print(f"Here is your change: ${change}")
            print("Here is your latte. Enjoy!") 
        else:
            print("Sorry, that's not enough money. Money refunded.")

    elif coffee == "cappuccino":
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) # 0.25
        dimes = int(input("How many dimes?: ")) # 0.10
        nickles = int(input("How many nickles?: ")) # 0.05
        pennies = int(input("How many pennies?: ")) # 0.01
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if total >= MENU["cappuccino"]["cost"]:
            change = total - MENU["cappuccino"]["cost"]
            print(f"Here is your change: ${change}")
            print("Here is your cappuccino. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")

    else: 
        print("Invalid input. Please try again.")
        
coffeeMachine()


def checkIngredients(coffee):
    if coffee == "espresso":
        if MENU["espresso"]["ingredients"]["water"] < 50: 
            print("Not enough water.")
        elif MENU["espresso"]["ingredients"]["coffee"] < 18:
            print("Not enough coffee.")
        else:
            print("Enough ingredients.")
    elif coffee == "latte":
        if MENU["latte"]["ingredients"]["water"] < 200:
            print("Not enough water.")
        elif MENU["latte"]["ingredients"]["milk"] < 150:
            print("Not enough milk.")
        elif MENU["latte"]["ingredients"]["coffee"] < 24:
            print("Not enough coffee.")
        else:
            print("Enough ingredients.")
    elif coffee == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] < 250:
            print("Not enough water.")
        elif MENU["cappuccino"]["ingredients"]["milk"] < 100:
            print("Not enough milk.")
        elif MENU["cappuccino"]["ingredients"]["coffee"] < 24:
            print("Not enough coffee.")
        else:
            print("Enough ingredients.")
    else:
        print("Invalid input.")



        




