import random

# Number guessing Game:
#Rules:

# 1. The computer will randomly generate a number between 1 and 100.
# 2. Prompt the user to enter a number between 1 and 100.
# 3. If the user's guess is correct, display "Congratulations! You guessed the number correctly."
# 4. If the user's guess is too high, display "Your guess is too high. Try again."
# 5. If the user's guess is too low, display "Your guess is too low. Try again."
# 6. The game should continue until the user guesses the correct number.
#The user will have a limited number of attempts to guess the number.
# Attemps = 7

# Generate a random number between 1 and 100

number = random.randint(1, 100) 
attempts = 7


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 attempts to guess the number.")
print("Let's begin!") 

numberguess =int(input("Please guess a number between 1 and 100: "))

def guess(numberguess):
    global attempts
    if numberguess < number:
        attempts -= 1
        print(f"Your guess is too low. Try again. You have {attempts} attempts left.")
    elif numberguess > number:
        attempts -= 1
        print(f"Your guess is too high. Try again. You have {attempts} attempts left.")
    elif numberguess == number:
        print("Congratulations! You guessed the number correctly.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")

    if attempts > 0 and numberguess != number:
        numberguess = int(input("Please guess a number between 1 and 100: "))
        guess(numberguess)
        if attempts == 0:
            print("Sorry, you have no more attempts left. The number was", number)
            print("Better luck next time!")

            # Run the game
guess(numberguess)









