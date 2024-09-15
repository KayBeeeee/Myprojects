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


input("What would you like? (espresso/latte/cappuccino): ")
print("Please insert coins.")
quarters = int(input("How many quarters?: ")) # 0.25
dimes = int(input("How many dimes?: ")) # 0.10  
nickles = int(input("How many nickles?: ")) # 0.05
pennies = int(input("How many pennies?: ")) # 0.01
total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


