import sys
sys.path.append("") 

from util.helper import clear, type_writer, colored_text
from caesarcipher_helper import logo, alphabets

def caesar(message, key, direction):
    result = ""
    for i in range(0, len(message)):
        if message[i] in alphabets:
            if direction == "encode":
                pivot = alphabets.index(message[i]) + key
                while pivot > 25: pivot -= 26
            else:
                pivot = alphabets.index(message[i]) - key
                while pivot < 0: pivot += 26
            result += alphabets[pivot]
        else: result += message[i]
    return result

clear()
type_writer(colored_text(logo, 'light_green'), 0.02)
flag = "yes"

while flag == "yes":
    direction = input("\nType 'encode' to encode, 'decode' to decode: ").lower()

    if direction != "encode" and direction != "decode":
        print("\nThis is an invalid input. Try again.")
        continue
    else:
        message = input("\nEnter the message: ")
        key = int(input("\nEnter shift amount: "))
        print(colored_text(f"\n{direction.capitalize()}d message is {caesar(message, key, direction)}"))

    flag = input("\nType 'yes' if you want to go again, else type 'no': ").lower()

clear()
print(colored_text("\nGOODBYE\n", "red"))