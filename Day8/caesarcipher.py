import os, sys

from time import sleep
from termcolor import colored
from caesarcipher_helper import logo, alphabets

def caesar(message, key, direction):
    result = ""
    for i in range(0, len(message)):
        if direction == "encode":
            pivot = alphabets.index(message[i]) + key
            while pivot > 25: pivot -= 26
        else:
            pivot = alphabets.index(message[i]) - key
            while pivot < 0: pivot += 26
        result += alphabets[pivot]
    return result

os.system("clear")
for char in logo:
    sleep(0.02)
    sys.stdout.write(colored(char, 'light_green', attrs=['blink']))
    sys.stdout.flush()
flag = "yes"

while flag == "yes":
    direction = input("\nType 'encode' to encode, 'decode' to decode: ").lower()

    if direction != "encode" and direction != "decode":
        print("\nThis is an invalid input. Try again.")
        continue
    else:
        message = input("\nEnter the message: ")
        key = int(input("\nEnter shift amount: "))
        print(colored(f"\n{direction.capitalize()}d message is {caesar(message, key, direction)}", 'light_green', attrs=['blink']))

    flag = input("\nType 'yes' if you want to go again, else type 'no': ").lower()

os.system("clear")
print(colored("\nGAME OVER\n", 'red', attrs=['blink']))