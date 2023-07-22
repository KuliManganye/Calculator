import os
from calculator_art import logo

# A simple calculator program

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

def calculator():
    print(logo)

    # prompt the user to input the numbers they want to calculate and allow for the program to take in numbers with decimals
    num1 = float(input("What's the first number?:"))

    for symbol in operations:
        print(symbol)
    calculating = True

    while calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == 'y':
            num1 = answer
        else:
            calculating = False
            os.system("cls")
            calculator()

calculator()