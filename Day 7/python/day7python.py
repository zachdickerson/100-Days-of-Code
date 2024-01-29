import random
import hangman_art
import hangman_words

#HangMan
#Randomly Chose a word in the list
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

#print(chosen_word)
word_len = len(chosen_word)

display = []
for i in range(word_len): 
    display +='_'

lives = 6
end_of_game = False
while not end_of_game:

    guess = input("Please guess a letter: ").lower()

    if guess not in display:

        for i in range(word_len):
            if chosen_word[i] == guess:
                display[i] = guess

        if guess not in display:
            print(f"You've guessed '{guess}', this letter is not in the word :(")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print('You lose!')

        if '_' not in display:
            end_of_game = True
            print('You Win!')

        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])

    else:
        print(f"You've guessed '{guess}', try again.")

