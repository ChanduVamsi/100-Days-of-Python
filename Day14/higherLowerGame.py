import sys, random
sys.path.append("")

from hlg_helper import LOGO, VS, data
from util.helper import clear

score = 0

clear()
print(LOGO)
account_B = random.choice(data)

while True:
    account_A = account_B
    print(f"Compare A: {account_A['name']}, {account_A['description']} from {account_A['country']}")

    print(VS)

    account_B = random.choice(data)
    while account_B == account_A: account_B = random.choice(data)
    print(f"Against B: {account_B['name']}, {account_B['description']} from {account_B['country']}")

    choice = input("\nWho has more followers on Instagram? Type 'A' or 'B': ").upper()
    while choice != "A" and choice != "B": 
        print("\nInvalid input! Try again")
        choice = input("\nWho has more followers on Instagram? Type 'A' or 'B': ").upper()

    clear()
    print(LOGO)
    print(f"\n{account_A['name']} has {account_A['follower_count']} million followers\n{account_B['name']} has {account_B['follower_count']} million followers")

    if (account_A['follower_count'] > account_B['follower_count'] and choice == "A") or (account_A['follower_count'] < account_B['follower_count'] and choice == "B"): 
        score += 1
        print(f"\nYou're right! New score: {score}\n")
        continue
    else: 
        print(f"\nYou're wrong! Final score: {score}\n")
        break