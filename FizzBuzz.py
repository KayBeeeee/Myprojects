#FizzBuzz

#This program automatically prints the solutions to a FizzBuzz Game
#The rules are as follows:
#For each number from 1 to 100, print "Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is divisible by both 3 and 5. If the number is not divisible by 3 or 5, print the number itself.

#Loop through numbers 1 to 100
for num in range(1, 101):
    #Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    #Check if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")
    #Check if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    #If the number is not divisible by 3 or 5, print the number itself
    else:
        print(num)

