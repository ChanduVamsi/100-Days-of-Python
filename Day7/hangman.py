#Save the fellow creed member - Assassin's Creed Unity
import random, os
from hangman_art import HANGMANPICS, logo
from termcolor import colored
os.system("clear")

#Word bank
words = ('mrgod asura theblackspade glitch karma aura zero crazymonk switcher cobra scorpion '
         'tate myron lucifer devil god orange eagle spider crow ghost raven power andrew luke '
         'dht hawk lion reptile snake mole snitch dagger rat wolf gym attitude speed trade '
         'jesse black panda dark tenet python rabbit covid redpill relentless money attention delusion ').split()

pswd = random.choice(words)
key = []
for i in range(len(pswd)): key.append("_")
print(logo)

for life in range(9):
    # for i in range(len(pswd)): print(key[i], end="")
    if "_" not in key:
        os.system("clear")
        print(colored(f'\nGood work. The key is {pswd}. Creed owes you one!', 'light_green', attrs=['blink']))
        print(colored(f'{HANGMANPICS[life-1]}\n', 'light_green', attrs=['blink']))
        break
    else:
        if life == 8:
            os.system("clear")
            print(colored(f"\nUnable to save. The key is {pswd}. It's time to avenge!", 'red', attrs=['blink']))
            print(colored(f'{HANGMANPICS[life-1]}\n', 'red', attrs=['blink']))
            break
        for i in range(len(pswd)): print(key[i], end="")
        guess = input("\n\nEnter a letter: ").lower()
        for num in range(len(pswd)):
            if pswd[num] == guess:
                key[num] = guess
        print(f"{HANGMANPICS[life]}\n")