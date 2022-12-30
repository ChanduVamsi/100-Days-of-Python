import os
os.system("clear")

#Loops
fruits = ["banana", "cherry", "peach", "mango"]
n = 1
print("\nBelow are the available smoothies at our franchise today:")
for fruit in fruits:
    print(f"{n}. {fruit} smoothie")
    n += 1

daily_profits = [21, 108, 69, 420, 99, 1212, 45, 8888]
print(f"\nAverage daily profit is ${int(sum(daily_profits)/len(daily_profits))} per branch.\n")