import art
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_computer_card():
    computer_cards = []

    computer = 0

    while computer <= 21:
        x = cards[random.randint(0,12)]
        if x == 11:
            if computer + x > 21:
                x = 1
        computer += x
        computer_cards.append(x)
    
    if sum(computer_cards) > 21:
        #print(computer_cards)
        computer_cards.pop()

    return computer_cards


def get_human_cards():
    human_cards = []
    human = 0
    
    for i in range(0,2):
        x = cards[random.randint(0,12)]
        if x == 11:
            if human + x > 21:
                x = 1
        human_cards.append(x)
    return human_cards


def blackjack():

    computer_cards = get_computer_card()
    computer_sum = sum(computer_cards)

    human_cards = get_human_cards()
    human = sum(human_cards)

    print(art.logo)
    print(f"Your cards: {human_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    # print(computer_cards)

    hitting = True
    while hitting:
        another_hit = input("Type 'y' to get another card, type 'n' to pass: ")

        if another_hit == 'y':
            z = cards[random.randint(0,12)]
            if z == 11:
                if human + z > 21:
                    z = 1
            
            human_cards.append(z)
            print(f'Your cards {human_cards} and the total is {sum(human_cards)}')
            if sum(human_cards) > 21:
                print(f"Your final hand: {human_cards}")
                print(f"Computers final hand: {computer_cards}")
                print('Computer Wins!')
                hitting = False
            elif sum(human_cards) == 21 and computer_sum == 21:
                print(f"Your final hand: {human_cards}")
                print(f"Computers final hand: {computer_cards}")
                print("It's a draw!")
                hitting = False
        else:
            hitting = False
            if sum(human_cards) == computer_sum:
                print(f"Your final hand: {human_cards}")
                print(f"Computers final hand: {computer_cards}")
                print("It's a draw!")
            elif sum(human_cards) > computer_sum:
                print(f"Your final hand: {human_cards}")
                print(f"Computers final hand: {computer_cards}")
                print("You win!")
            else:
                print(f"Your final hand: {human_cards}")
                print(f"Computers final hand: {computer_cards}")
                print('Computer wins!')

    game2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game2 == 'y':
        blackjack()
    else:
        print("Thank you for playing!")

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()


# I completed the problem with only 1 hint! Which is expert ;)