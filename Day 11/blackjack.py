############### Blackjack Project #####################
import random
from art import logo
import os, platform

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card_index = random.randint(0, len(cards)-1)
    card = cards[card_index]
    cards.pop(card_index)   
    return card 

def reset_cards():
    global cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
             11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
             11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
             11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(user_cards, computer_cards):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'Your final cards: {user_cards}, final score: {user_score}')
    print(f"Computer's final cards: {computer_cards}, final score {computer_score}")
    if user_score == computer_score:
        print("Draw 🙃")
    elif user_score == 0:
        print('You win with a blackjack 😎')
    elif computer_score == 0:
        print('Lose, opponent has a blackjack 😱')
    elif user_score>21:
        print('You went over, You lose 😤')
    elif computer_score>21:
        print('Computer went over You win 😁')
    elif user_score>computer_score:
        print('You win 😁')
    else:
        print('You lose 😤')


def calculate_score(lst):
    if lst==[11,10] or lst==[10,11]:
        return 0

    if sum(lst)>21 and 11 in lst:
        index_of_11 = lst.index(11)
        lst[index_of_11]=1

    return sum(lst)



def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f'Your cards: {user_cards}, current score: {calculate_score(user_cards)}')
    print(f"Computer's first card: {computer_cards[0]}")

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_blackjack = False 
    computer_blackjack = False

    if calculate_score(user_cards)==0:
        user_blackjack = True

    if calculate_score(computer_cards)==0:
        computer_blackjack = True 

    user_went_over = False
    while not user_went_over and not user_blackjack:
        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f'Your cards: {user_cards}, current score: {user_score}')
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score>21:
                user_went_over = True
        else:
            break
            
        #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
        # what if computer blackjacked?
    while calculate_score(computer_cards)<17 and not user_went_over and not computer_blackjack:
        computer_cards.append(deal_card())

    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

    compare(user_cards, computer_cards)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
    reset_cards()

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


