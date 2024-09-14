import random

# Number guessing Game:
# Rules:
# 1. The computer will randomly generate a number between 1 and 100.
# 2. Prompt the user to enter a number between 1 and 100.
# 3. If the user's guess is correct, display "Congratulations! You guessed the number correctly."
# 4. If the user's guess is too high, display "Your guess is too high. Try again."
# 5. If the user's guess is too low, display "Your guess is too low. Try again."
# 6. The game should continue until the user guesses the correct number.
# The user will have a limited number of attempts to guess the number.
# Attempts = 7

# Generate a random number between 1 and 100
number = random.randint(1, 100) 
attempts = 7

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 attempts to guess the number.")
print("Let's begin!") 

while True:
    try:
        # Prompt the user to guess a number
        numberguess = int(input("Please guess a number between 1 and 100 (or enter 0 to stop): "))
        
        if numberguess == 0:
            print("You entered 0. Exiting the program.")
            break  # Exit the loop and stop the program when 0 is entered
        
        # If the guess is outside the valid range, warn the user
        if numberguess < 1 or numberguess > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        # If the guess is correct
        if numberguess == number:
            print("Congratulations! You guessed the number correctly.")
            break
        
        # If the guess is too low
        elif numberguess < number:
            attempts -= 1
            print(f"Your guess is too low. Try again. You have {attempts} attempts left.")
        
        # If the guess is too high
        elif numberguess > number:
            attempts -= 1
            print(f"Your guess is too high. Try again. You have {attempts} attempts left.")
        
        # If the user runs out of attempts
        if attempts == 0:
            print(f"Sorry, you have no more attempts left. The number was {number}. Better luck next time!")
            break

    except ValueError:
        print("That was not a valid number. Please try again.")  # Ask for input again if input is invalid
  