import random
import os

os.system("clear")

user = input("Please choose head or tails: ")

options = ["Heads", "Tails"]
computer = random.choice(options)

if computer.lower() == user.lower():
    print(f"\nHurray, you won the toss. It's {computer}!\n")
else:
    print(f"\nBetter luck next time. It's {computer}!\n")