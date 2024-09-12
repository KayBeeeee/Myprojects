# This game is called Higherlower
#How it works:
#The program will generate a random number between 1 and 100
#The user will guess if the next number is higher or lower
#If the user is correct, the score will increase by 1
#If the user is incorrect, the game will end and the final score will be displayed
import random


number = random.randint(1, 100)
score = 0

def higherlower():
    global number
    global score
    print(f"The current number is {number}.")    
    guess = input("Is the next number higher or lower? (h/l) ")
    next_number = random.randint(1, 100)
    if guess == "h" and next_number > number:
        print("Correct!")
        score += 1
    elif guess == "l" and next_number < number:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The number was {number}. Your final score is {score}.")
        return
    number = next_number
    higherlower()

higherlower()