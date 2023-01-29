import sys
sys.path.append("")

from util.helper import clear
from calculator_art import logo, operations

def calc(first_num, operation, second_num): 
    """Calculates based on the inputs given by user
    and returns the mathematical result for the equation"""
    if operation == "+": return first_num + second_num
    elif operation == "-": return first_num - second_num
    elif operation == "*": return first_num * second_num
    elif operation == "/": return first_num / second_num
    elif operation == "**": return first_num ** second_num
    elif operation == "//": return first_num // second_num
    elif operation == "%": return first_num % second_num

# "n" for new calculator, "c" to continue with the result and "q" to quit the application
flag = "n"

while flag == "n" or flag == "c":
    if flag == "n": 
        clear()
        print(logo)
        first_num = float(input("Enter the first number: "))
    else: first_num = result
    operation = input(f"\nOperations: {operations.keys()}\n\nEnter an operation from the above list: ")
    second_num = float(input("\nEnter the next number: "))
    result = calc(first_num, operation, second_num)
    print(f"\n{first_num} {operation} {second_num} = {result}")
    flag = input("\n'n' for new calculator, 'c' to continue with the result and 'q' to quit the application: ")
clear()