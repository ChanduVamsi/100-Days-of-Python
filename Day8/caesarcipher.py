import os, sys

from time import sleep
from termcolor import colored
from caesarcipher_helper import logo, alphabets

def encode(message, key):
    result = ""
    for i in range(0, len(message)):
        pivot = alphabets.index(message[i]) + key
        while pivot > 25:
            pivot -= 26
        result += alphabets[pivot]
    return result

def decode(message, key):
    result = ""
    for i in range(0, len(message)):
        pivot = alphabets.index(message[i]) - key
        while pivot < 0:
            pivot += 26
        result += alphabets[pivot]
    return result

os.system("clear")
for char in logo:
    sleep(0.02)
    sys.stdout.write(colored(char, 'light_green', attrs=['blink']))
    sys.stdout.flush()
flag = "yes"

while flag == "yes":
    option = input("\nType 'encode' to encode, 'decode' to decode: ").lower()
    if option == "encode":
        plain_text = input("\nType your message: ")
        key = int(input("\nType your shift number: "))
        print(colored(f"\nEncoded message is {encode(plain_text, key)}", 'light_green', attrs=['blink']))

    elif option == "decode":
        cipher_text = input("\nType the cipher text: ")
        key = int(input("\nType your key: "))
        print(colored(f"\nDecoded message is {decode(cipher_text, key)}", 'light_green', attrs=['blink']))
    
    else: 
        print("\nThis is an invalid input. Try again.")
        continue

    flag = input("\nType 'yes' if you want to go again, else type 'no': ").lower()

os.system("clear")
print(colored("\nGAME OVER\n", 'red', attrs=['blink']))