print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

road = input("You're " + 'at a cross road. Where do you want to go? Type "left" or "right"\n')

if road == "left":
    lake = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if lake == "wait":
        color = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n')
        if color == 'red':
            print("Burned by fire. Game Over.")
        elif color == 'yellow':
            print("You Win!")
        elif color == 'blue':
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print('Attacked by trout. Game Over')
else:
    print("Fall into a hole. Game Over")