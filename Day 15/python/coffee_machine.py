# Makes 3 Hot Flavors 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#print(MENU["espresso"]["ingredients"])
#print(MENU["espresso"]["cost"])


def coin_counter(drink,quaters, dimes, nickles, pennies):
    quaters = quaters * 0.25
    dimes = dimes * 0.1
    nickles = nickles * 0.05
    pennies = pennies * 0.01

    money_total = quaters + dimes + nickles + pennies

    drink_price = MENU[drink]["cost"]

    change = round(money_total - drink_price, 2)

    if drink_price > change:
        return "Sorry that's not enough money. Money refunded."

    return f"Here is ${change} in change."


def resource_check(drink):

    if drink == "espresso":
        drink_water = MENU["espresso"]["ingredients"]["water"]
        drink_milk = 0
        drink_coffee = MENU["espresso"]["ingredients"]["coffee"]
    else:
        drink_water = MENU[drink]["ingredients"]["water"]
        drink_milk = MENU[drink]["ingredients"]["milk"]
        drink_coffee = MENU[drink]["ingredients"]["coffee"]

    resource_water = resources["water"]
    resource_milk = resources["milk"]
    resource_coffee = resources["coffee"]

    new_water = resource_water - drink_water
    new_milk = resource_milk - drink_milk
    new_coffee = resource_coffee - drink_coffee

    if new_water <= 0:
        return "Sorry there is not enough water."
    elif new_milk <=0:
        return "Sorry there is not enough milk."
    elif new_coffee <=0:
        return "Sorry there is not enough coffee."
    else:
        resources["water"] = new_water
        resources["milk"] = new_milk
        resources["coffee"] = new_coffee

    return resources

print(resources)
print(resource_check("espresso"))
print(resource_check("latte"))
print(resource_check("espresso"))
print(resource_check("espresso"))
print(resource_check("espresso"))
print(resource_check("espresso"))







def making_coffee():
    drink = input(" What would you like? (espresso/latte/cappuccino): ")
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))


    print(coin_counter(drink=drink,quaters=quarters,dimes=dimes,nickles=nickles,pennies=pennies))

    print(resources)



