import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
import os, platform

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = list('_'*word_length)
lives = 6
end_of_game = False

clear()
print(logo)

# print(f'Correct answer is {chosen_word}')

while not end_of_game:

    letter = input('Guess a letter: ')
    clear()

    # if the input is corrent
    for i,c in enumerate(chosen_word):
        if letter == c:
            display[i] = letter

    # if the input is incorrect
    if letter not in chosen_word:
        print(f'You guessed {letter}. It\'s not in the word. You lost a life')
        lives -= 1
    else:
        print(f'You guessed {letter}. It\'s in the word.')

    if lives<=0 or '_' not in display:
        end_of_game = True

    print(' '.join(display))
    print(stages[lives])
    print(f'Remaining lives {lives}')

if lives<=0:
    print('You lost')
    print(f'Correct word was {chosen_word}')
else:
    print('You won')


# Problems
# 2 if an incorrect guess is given dont deduct life another time
