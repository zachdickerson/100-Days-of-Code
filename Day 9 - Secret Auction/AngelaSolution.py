#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

our_flow = True

auction_dictionary = {}

def auction_leaderboard(bid_record):
    max = 0
    for key in auction_dictionary:
      if max < auction_dictionary[key]:
        max = auction_dictionary[key]
        max_name = key
    print(f"The winner is {max_name} with a bid of ${max}.")
    

while our_flow == True:
  print(logo)
  user_name = input("What is your name? ")
  user_bid = int(input("What is you bid? $"))
  auction_dictionary[user_name] = user_bid
  
  other_bids = input("Are there any other bidders? Type 'yes' or 'no.'\n")

  if other_bids == "yes":
    #clear()
    print('should be clear')
  else:
    our_flow = False
    #clear()
    auction_leaderboard(auction_dictionary)