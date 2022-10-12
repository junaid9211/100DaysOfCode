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

signs = [rock, paper, scissors]
player_score = 0
computer_score = 0
continue_playing = 'y'

while continue_playing.lower()[0] == 'y':
    player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
    computer_choice = random.randint(0,2)

    print(signs[player_choice])
    print('Computer chose')
    print(signs[computer_choice])

    # condition for a draw
    if player_choice==computer_choice:
        print('Draw')

    # all winning conditions
    elif player_choice==0 and computer_choice==2:
        # player wins:  rock -> scissors
        print('You win')
        player_score += 1
        
    elif player_choice==2 and computer_choice==1:
        # player wins: scissors -> paper
        print('You win')
        player_score += 1
        
    elif player_choice==1 and computer_choice==0:
        # player wins: paper -> rock
        print('You win')
        player_score += 1
        

    # all lossing conditions
    elif player_choice==2 and computer_choice==0:
        # player losses:  rock -> scissors
        print('You lose')
        computer_score += 1
        
    elif player_choice==1 and computer_choice==2:
        # player losses: scissors -> paper
        print('You lose')
        computer_score += 1
        
    elif player_choice==0 and computer_choice==1:
        # player losses: paper -> rock
        print('You lose')
        computer_score += 1

    print('\nSCORE BOARD')
    print(f'Your Score:     {player_score}')
    print(f'Computer Score: {computer_score}\n')
        
    continue_playing = input('\nWant to continue playing? [y/n] ')

