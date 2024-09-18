import json

#This program simulates a coffee machine that can make espresso, latte, and cappuccino.
#It uses a JSON file to store the resources and update them as the program runs.
#The program also allows the user to add resources manually.



# File to store resources
RESOURCE_FILE = "resources.json"

# Initial resources
initial_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

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

def load_resources():
    """Load resources from a file, or initialize default resources."""
    try:
        with open(RESOURCE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return initial_resources  # Return initial resources if no file exists

def save_resources():
    """Save the current resources to a file."""
    with open(RESOURCE_FILE, "w") as file:
        json.dump(resources, file)

def report():
    """Print the current balance of resources."""
    print("\nCurrent Resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}\n")

def add_resources():
    """Function to add resources manually."""
    print("\nAdd Resources:")
    water = int(input("How much water to add?: "))
    milk = int(input("How much milk to add?: "))
    coffee = int(input("How much coffee to add?: "))
    
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee
    
    print("\nResources updated!")
    report()
    save_resources()

def check_ingredients(coffee):
    """Check if there are enough ingredients to make the coffee."""
    ingredients = MENU[coffee]["ingredients"]
    for item, amount in ingredients.items():
        if resources[item] < amount:
            print(f"Not enough {item}.")
            return False
    return True

def update_resources(coffee):
    """Update resources after making the coffee."""
    ingredients = MENU[coffee]["ingredients"]
    for item, amount in ingredients.items():
        resources[item] -= amount
    resources["money"] += MENU[coffee]["cost"]
    save_resources()

def process_payment(coffee):
    """Handle coin insertion and check if the payment is enough."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))  # 0.25
    dimes = int(input("How many dimes?: "))  # 0.10
    nickles = int(input("How many nickles?: "))  # 0.05
    pennies = int(input("How many pennies?: "))  # 0.01
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    cost = MENU[coffee]["cost"]
    if total >= cost:
        change = total - cost
        print(f"Here is your change: ${change:.2f}")
        update_resources(coffee)
        print(f"Here is your {coffee}. Enjoy!")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def coffee_machine():
    """Main function to run the coffee machine."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/report/add/off): ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            report()
        elif choice == "add":
            add_resources()
        elif choice in MENU:
            if check_ingredients(choice):
                if process_payment(choice):
                    again = input("Would you like another coffee? (Y/N): ").lower()
                    if again != 'y':
                        print("Thank you for using the Coffee Machine!")
                        break
            else:
                print("Not enough ingredients to make that coffee.")
        else:
            print("Invalid input. Please select espresso, latte, cappuccino, report, add, or off.")

# Load the resources from the file
resources = load_resources()

# Run the coffee machine
coffee_machine()
