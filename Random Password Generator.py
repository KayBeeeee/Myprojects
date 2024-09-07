# Random Password Generator
# This program generates a random password of a specified length using a combination of letters, numbers, and special characters.
# The program will randomise the order of the characters in the password.

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the Random Password Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []



# Manipulating the received input feedback:

newLetters = nr_letters+1
newSymbols = nr_symbols+1
newNumbers = nr_numbers+1

randomLetters = range(newLetters)
randomSymbols = range(newSymbols)
randomNumbers = range(newNumbers)




for num in randomLetters:
    generatedLetter = random.choice(letters)
    password += generatedLetter
    letters.remove(generatedLetter) # Remove the used letter from the list to prevent repetition
    if num == nr_letters:
        break
    else:
        continue

for num in randomSymbols:
    generatedSymbol = random.choice(symbols)
    password += generatedSymbol
    symbols.remove(generatedSymbol) # Remove the used symbol from the list to prevent repetition
    if num == nr_symbols:
        break
    else:
        continue


for num in randomNumbers:
    generatedNumber = random.choice(numbers)
    password += generatedNumber
    numbers.remove(generatedNumber) # Remove the used number from the list to prevent repetition
    if num == nr_numbers:
        break
    else:
        continue

random.shuffle(password) #Shuffles the password characters to ensure randomness

print(f"Thank you for using the Password Generator, your randomly generated password is: {password}")








    





