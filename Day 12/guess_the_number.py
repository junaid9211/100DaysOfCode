from art import logo
import random
import os, platform

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

def set_difficulty(difficulty):
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    return attempts


clear()
print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1,100)
# print(f"Pssst, the correct answer is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = set_difficulty(difficulty)



correct_guessed = False
while attempts>0 and not correct_guessed:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    attempts -= 1

    if guess<answer:
        print('Too Low')
    elif guess>answer:
        print('Too high')
    else:
        correct_guessed = True
        break

    if attempts>0 and not correct_guessed:
        print('Guess again.')
        

if correct_guessed:
    print(f'You got it! The answer was {answer}')
else:
    print(f'You have run out of guesses, you lose, The answer was {answer}')
