import sys, random
sys.path.append("")

from util.helper import clear, colored_text
from blackjack_helper import logo, cards

def showCards(all_cards):
    '''Prints all the cards in the player's deck'''
    for card in all_cards: print(f" {card}", end="")

def getSum(all_cards):
    '''Returns the sum of the cards for the concerned player'''
    sum = 0
    for card in all_cards: sum += cards[card]
    if sum > 21 and "A" in all_cards: sum -= 10
    return sum

def hit():
    '''Adds a new card to the player's deck'''
    return random.choice(list(cards.keys()))

def currentCards(flag, user_cards, user_sum, comp_cards, comp_sum):
    '''Reports the current status of the player decks'''
    clear()
    print(logo, end ="")
    print("\nUSER:", end="")
    showCards(user_cards)
    print(f" -> {user_sum}")
    if flag: 
        print("\nCOMP:", end="")
        showCards(comp_cards)
        print(f" -> {comp_sum}\n")
    else: 
        print(f"\nCOMP: {comp_cards[0]}", end="")
        for i in range(1, len(comp_cards)): print(" _", end = "")
        print(" -> ?")

def blackjack(bank, bid):
    '''Checks and reports if the player won the game.
    Updates the bank amount according to the bet and 
    checks if the player want to continue the game'''
    user_cards, user_sum, comp_cards, comp_sum = [], 0, [], 0

    for i in range(2):
        user_cards.append(hit())
        comp_cards.append(hit())

    while True:
        user_sum = getSum(user_cards)
        comp_sum = getSum(comp_cards)
        currentCards(False, user_cards, user_sum, comp_cards, comp_sum)
        
        if user_sum >= 21 or comp_sum >= 21 or input(f"\nEnter {colored_text('hit', 'red')} to draw another card, else enter {colored_text('stand')}: ") != "hit": 
            currentCards(True, user_cards, user_sum, comp_cards, comp_sum)

            if user_sum == comp_sum or (user_sum > 21 and comp_sum > 21): print(colored_text(f"IT'S A DRAW!\n\nBANK: ${bank}\n", 'cyan'))
            elif (user_sum > comp_sum and user_sum <= 21) or comp_sum > 21 : 
                bank += bid
                print(colored_text(f"YOU WON!  +${bid}\n\nBANK: ${bank}\n"))
            else: 
                bank -= bid
                print(colored_text(f"YOU LOST! -${bid}\n\nBANK: ${bank}\n", 'red'))
            return bank, input(f"Enter {colored_text('True')} if you want to start a new game, else {colored_text('False', 'red')}: ")

        user_cards.append(hit())
        if comp_sum < random.choice([15, 16, 17, 18]): comp_cards.append(hit())

game = "True"
bank = 1000
while game == "True":
    print(colored_text(logo))
    print(colored_text(f"BANK: ${bank}"))
    bid = int(input(colored_text("\nENTER BID AMOUNT: $")))
    if bank <= 0: 
        print(colored_text("\nInsufficient balance in the bank!", "red"))
        break
    elif bid > bank or bid <= 0: 
        print(colored_text("\nInvalid input. Try again!", "red"))
        continue
    bank, game = blackjack(bank, bid)