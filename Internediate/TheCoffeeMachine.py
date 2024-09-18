#This is progrom simulates a coffeMachine
#check if the ingredients are enough
#calculate the change
#check if the payment is enough
#update the resources
#check if the user wants another coffee
#If the user wants another coffee, repeat the process
#If the user doesn't want another coffee, print a message saying "Thank you for using the Coffee Machine!"
#If the user doesn't want another coffee, print a message saying "Thank you for using the Coffee Machine!"


resources = {
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

#update ingredients after each coffee
def updateingredients(coffee): 

    global resources

    while True:

 
        if coffee == "espresso":
            resources["water"] -= MENU["espresso"]["ingredients"]["water"] 
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            resources["money"] += MENU["espresso"]["cost"]
            

        
        elif coffee == "latte":
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["money"] += MENU["latte"]["cost"]
        elif coffee == "cappuccino":
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["money"] += MENU["cappuccino"]["cost"]
        else:
            print("Invalid input.")

        break
        return    
        
        
    #we need to update our original resources valueS after performing the calcs above:


    newresources = {
            
                "water": resources["water"],
                "milk": resources["milk"],
                "coffee": resources["coffee"],
                "money": resources["money"]
        }


   # print(newresources)

        
    for key, value in newresources.items():
        if key in resources:
            resources[key] = value
    print(resources)



        
                


        






def coffeeMachine():
    print("Welcome to the Coffee Machine!")
    print("What would you like? (espresso/latte/cappuccino): ")
    coffee = input()
    checkIngredients(coffee)
   
   
    
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
            updateingredients(coffee)

            
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
            updateingredients(coffee)
            
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
            updateingredients(coffee)
           
        else:
            print("Sorry, that's not enough money. Money refunded.")

    else: 
        print("Invalid input. Please try again.")
       
        
coffeeMachine()









    




        




