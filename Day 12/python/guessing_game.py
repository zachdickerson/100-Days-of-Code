import random
import art

random_number = random.randint(1,100)
print(random_number)

diff_easy = 10
diff_hard = 5

winner = False

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'hard':
    #print(f"You have {diff_hard} attempts remaining to guess the number.")
    lives = diff_hard
else:
    #print(f"You have {diff_easy} attempts remaining to guess the number.")
    lives = diff_easy

while not winner:

    print(f"You have {lives} attempts remaining to guess the number.")

    guess = int(input('Make a guess: '))

    if lives > 1:
        if guess == random_number:
            winner = True
            print(f"You got it, the answer was {random_number}")

        elif guess > random_number:
            print("Too High\nGuess Again")
            lives -= 1
        else:
            print("Too Low\nGuess Again")
            lives -= 1
    else:
        winner = True

if lives == 0:
    print("You've run out of guesses, you lose.")
    print(f"The random number was {random_number}")
