# calculator program: This program is a simple 
# calculator that performs basic arithmetic operations


def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."



print("Welcome to the Calculator App!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
result = calculator(num1, num2, operation)
print("Result:", result)
#continue with result or start calculator app again: This section allows the user to 
# either continue with the result of the previous calculation or start a new calculation
while True:
    choice = input("Do you want to continue with the result or start a new calculation? (y/n): ")
    if choice == 'y':
        operation = input("Enter the operation (+, -, *, /): ")
        #rest num2: This line prompts the user to enter the second number again
        num2 = float(input("Enter the second number: "))
        result = calculator(result, num2, operation)
        print("Result:", result)
    elif choice == 'n':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        result = calculator(num1, num2, operation)
        print("Result:", result)
    else:
        print("Invalid choice. Please try again or type 'e' to exit.")
        

