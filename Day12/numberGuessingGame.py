import random, os

logo = '''
_________                              ___________                                    ______              
__  ____/___  _____________________    __  /___  /______     ___________  ________ ______  /______________
_  / __ _  / / /  _ \_  ___/_  ___/    _  __/_  __ \  _ \    __  __ \  / / /_  __ `__ \_  __ \  _ \_  ___/
/ /_/ / / /_/ //  __/(__  )_(__  )     / /_ _  / / /  __/    _  / / / /_/ /_  / / / / /  /_/ /  __/  /    
\____/  \__,_/ \___//____/ /____/      \__/ /_/ /_/\___/     /_/ /_/\__,_/ /_/ /_/ /_//_.___/\___//_/                                                                                                         
'''

chances = 10

def checkAnswer(guess, key): 
    if guess == key: 
        print("\nWell done soldier!")
        return True
    elif guess < key: print("\nNah, that's too low!")
    else: print("\nHoly cow, that's too high!")
    return False


def game():
    key = random.randint(1, 100)
    if "hard" == input("\nGame difficulty: 'easy' or 'hard': "): 
        global chances
        chances = 5
    for i in range(chances, 0, -1):
        guess = int(input(f"\nYou have {i} lives left. \n\nGuess the number between 1 and 100: "))
        if checkAnswer(guess, key): break
        if i == 1: 
            print(f"\nRan out of lives😭 It's actually {key}!")
            break
    chances = 10
        

while True:
    os.system("clear")
    print(logo, end="")
    game()
    if "no" == input("\nEnter 'yes' to play again, else 'no': "):
        os.system("clear")
        break