import sys
sys.path.append("")

from util.helper import clear
from helper import LOGO, MENU, resources, CURRENCY

def showReport(): 
    '''Shows a report on the resources present in the coffee machine''' 
    print(f"\nWater: {resources['water']}ml | Milk: {resources['milk']}ml | Coffee: {resources['coffee']}gms | Money: ${resources['money']} available in the machine")

def checkAvailability():
    '''Checks the availability of the ingredients if the order can be facilitated or not'''
    ingredient =  MENU[order]['ingredients']
    if ingredient['water'] * quantity > resources['water'] or ingredient['milk'] * quantity > resources['milk'] or ingredient['coffee'] * quantity > resources['coffee']: 
        print(f"\nSorry, not enough resources in the machine for a {order}.")
        showReport()
        return False
    return True

def cashSlot():
    '''Manages the cash flow'''
    paid, price = 0, quantity * MENU[order]['cost']
    print(f"\n{quantity} {order}s costs ${price}0. Please insert coins.")
    for cash in CURRENCY: 
        paid += CURRENCY[cash] * int(input(f"How many {cash}s: "))

    clear()
    print(f"\nPaid amount: {round(paid/60, 2)}")

    if (paid/60) < price: 
        print("Paid amount is not enough. Please reorder😓\n")
        return False
    
    print(f"\nHere's your change: {round((paid/60) - price, 2)}")
    updateResources()
    return True

def updateResources():
    '''Updates the resources after using up some of the ingredients to facilitate the order'''
    resources['money'] += MENU[order]['cost'] * quantity
    resources['water'] -= MENU[order]['ingredients']['water'] * quantity
    resources['milk'] -= MENU[order]['ingredients']['milk'] * quantity
    resources['coffee'] -= MENU[order]['ingredients']['coffee'] * quantity

clear()
print(LOGO)

while True:
    order = input("\nWhat would you like? (Espresso/Latte/Capuccino)☕: ").capitalize()
    if order in MENU: 
        quantity = int(input(f"How many {order}s? "))
        if not checkAvailability(): continue
        if not cashSlot(): continue
        print(f"\nHere's your {quantity} {order}s☕. Have a good day😊")
        showReport()
        break
    elif order == "Report": showReport()
    else: break