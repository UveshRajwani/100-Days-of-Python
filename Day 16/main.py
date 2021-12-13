from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
while True:
    order = input(f"What Do You Want {menu.get_items()} ").lower()
    if menu.find_drink(order) is not None:
        for items in menu.menu:
            if items.name == order:
                if money_machine.make_payment(items.cost) and coffee_maker.is_resource_sufficient(items):
                    coffee_maker.make_coffee(items)

    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        print("Bye")
        break
