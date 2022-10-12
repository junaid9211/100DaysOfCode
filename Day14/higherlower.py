import os, platform
import art
from game_data import data
import random
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

def check_answer(options, choice):

    if choice in ['a', 'b']:
        answer = options[choice]
    else:
        return False

    if options['a']['follower_count']>options['b']['follower_count']:
        correct_option = options['a']
    elif options['a']['follower_count']<options['b']['follower_count']:
        correct_option = options['b']
    else:
        return True # both are correct options

    return correct_option == answer


random.shuffle(data)
score = 0
clear()

for i in range(len(data)-1):
    options = {'a':data[i], 'b':data[i+1]}
    print(art.logo)

    if score>0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {options['a']['name']}, a {options['a']['description']}, from {options['a']['country']}.")
    print(art.vs)
    print(f"Against B: {options['b']['name']}, a {options['b']['description']}, from {options['b']['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    clear()
    if check_answer(options, choice):
        score += 1
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break



