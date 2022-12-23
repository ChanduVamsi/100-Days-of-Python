#Rock Paper Scissor game with the computer using randomization and lists
import os
import random

os.system("clear")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

options = [rock, paper, scissor]

user = int(input("Type 0 for rock, 1 for paper and 2 for scissor: "))
if user > 2:
    print("\nPlease enter a valid choice x_x\n")
else:
    comp = random.randint(0, 2)

    print(f"You chose:\n{options[user]}\n")
    print(f"Computer chose:\n{options[comp]}")

    if comp - user == 1 or comp - user == -2:
        print("You lost TT\n")
    elif comp - user == 0:
        print("It's a draw :)\n")
    else:
        print("Congrats! You won XD\n")