from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = input(f"What would you like {menu.get_items()}: ").lower()
    if order == "off": break
    elif order == "report": 
        coffee_maker.report()
        money_machine.report()
    else: 
        item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
            coffee_maker.report()
            money_machine.report()