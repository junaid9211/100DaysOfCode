import os, platform
from getpass import getpass
from art import logo

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

print(logo)
print('Welcome to the secret auction program.\n ')
      
# get names and bids
bidings = {}
# get inputs
run = 'yes'
while run == 'yes':
    
    # taking name as input
    name = input('What is your name?: ')

    # taking bid as input
    while True:
        bid = getpass('What\'s your bid?: $')
        if bid.isdigit():
            bid = int(bid)
            break
        else:
            print(f'Bid can only be an integer value you provided {bid}')

    # adding name and bid to the dictionary
    bidings[name] = bid 

    # asking to continue adding names and bids
    run = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()



# get the name and highest bid
highest = 0
name = ''
for key, value in bidings.items():
    if value>highest:
        highest = value
        name = key 

print(f'The winner is {name} with a bid of ${highest}.\n')


