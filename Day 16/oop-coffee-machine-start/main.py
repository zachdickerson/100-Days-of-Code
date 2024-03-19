from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_choice = Menu()

is_on = True






while is_on:
    
    user_choice = input(f"What would you like? ({menu_choice.get_items()}): ")

    if user_choice == "off":
        is_on = False
    
    elif user_choice == "report":
        money_machine.report()
        coffee_maker.report()
    
    else:
        print(coffee_maker.is_resource_sufficient(menu_choice.find_drink(user_choice)))
        
