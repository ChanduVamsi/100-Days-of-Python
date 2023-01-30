import sys, random
sys.path.append("")

from util.helper import clear

logo = '''\n
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/                 
'''

cards = {
    "A" : 11, 
    1 : 1, 
    2 : 2, 
    3 : 3, 
    4 : 4, 
    5 : 5, 
    6 : 6, 
    7 : 7, 
    8 : 8, 
    9 : 9, 
    10 : 10, 
    "J" : 10, 
    "Q" : 10, 
    "K" : 10
}

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

def cardDeck(flag, user_cards, user_sum, comp_cards, comp_sum):
    '''Shows the current status of the players decks'''
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