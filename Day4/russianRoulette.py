import os
import random

os.system("clear")

roulette = []
for i in range(1, 37):
    roulette.append(i)

user = int(input("Place your bet on any number between 1 and 36: "))
print("\n")
while True:
    arrow = random.choice(roulette)
    if user == arrow:
        print("\nWhat a lucky day, you won!/n")
        break
    else:
        print(f"Unlucky. It's {arrow}. Try again!")