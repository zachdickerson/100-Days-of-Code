# form replit import art   # this is for replit to clear the terminal

import art

keep_going = True
bidders = {}

print(art.logo)
print("Welcome to the secret auction program.")

def highest_bid():
    count = 0
    high_key = ""
    for key in bidders:
        if bidders[key] > count:
            count = bidders[key]
            high_key = key
            
    print(f"The winner is {high_key} with a bid of ${count}.")

while keep_going:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    keep_pushing = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if keep_pushing == 'no':
        keep_going = False
        highest_bid()
    #elif keep_pushing == 'yes': # this is where we would clear if using replit.
    #    clear()

