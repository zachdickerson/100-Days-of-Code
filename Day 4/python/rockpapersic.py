import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

actions = [rock, paper, scissors]

computer = random.randint(0,2)

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if human >=3 or computer < 0:
    print('You typed an invalid number, you lose!')
else:
    print(actions[human])
    print(f"Computer chose:\n{actions[computer]}")

    if human == computer:
        print("Draw! Try Again.")
    elif human == 0 and computer == 1:
        print('You Lose!')
    elif human == 0 and computer == 2:
        print('You Win!')
    elif human == 1 and computer == 0:
        print('You Win!')
    elif human == 1 and computer == 2:
        print('You Lose!')
    elif human == 2 and computer == 0:
        print('You Lose!')
    elif human == 2 and computer == 1:
        print('You Win!')
    else:
        print("Invalid Input")


