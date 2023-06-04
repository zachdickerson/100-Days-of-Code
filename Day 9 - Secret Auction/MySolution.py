#from replit import clear
import os
#HINT: You can call clear() to clear the output in the console.
from art import logo

our_flow = True

auction_dictionary = []

def auction_leaderboard(bid_total):
    
    max = 0
    for key in auction_dictionary:
      if max < key["bid"]:
        max = key["bid"]
        max_name = key["name"]
    print(f"The winner is {max_name} with a bid of ${max}.")
    

while our_flow == True:
  print(logo)
  name = input("What is your name? ")
  bid = int(input("What is you bid? $"))

  auction_dictionary.append({"name":name, "bid":bid})
  
  other_bids = input("Are there any other bidders? Type 'yes' or 'no.'\n")

  if other_bids == "yes":
    os.system('clear')
  else:
    our_flow = False
    os.system('clear')
    auction_leaderboard(auction_dictionary)
    

  

    