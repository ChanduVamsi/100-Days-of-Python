#Save the fellow creed member - Assassin's Creed Unity
import random, os
from termcolor import colored
os.system("clear")

HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank
words = ('mrgod asura theblackspade glitch karma aura zero crazymonk switcher cobra scorpion '
         'tate myron lucifer devil god orange eagle spider crow ghost raven power andrew luke '
         'dht hawk lion reptile snake mole snitch dagger rat wolf gym attitude speed trade '
         'jesse black panda dark tenet python rabbit covid redpill relentless money attention delusion ').split()

pswd = random.choice(words)
key = []
for i in range(len(pswd)): key.append("_")

for life in range(8):
    for i in range(len(pswd)): print(key[i], end="")
    if "_" not in key:
        os.system("clear")
        print(colored(f'\n\nGood work. Creed owes you one!\n', 'green', attrs=['blink']))
        print(colored(f'{HANGMANPICS[life]}\n', 'green', attrs=['blink']))
        break
    else:
        if life == 7:
            os.system("clear")
            print(colored(f'\n\nThe password was {pswd}. Unable to save. Time to avenge!', 'red', attrs=['blink']))
            print(colored(f'{HANGMANPICS[life]}\n', 'red', attrs=['blink']))
            break
        guess = input("\n\nEnter a letter: ").lower()
        for num in range(len(pswd)):
            if pswd[num] == guess:
                key[num] = guess
        print(f"{HANGMANPICS[life]}\n")