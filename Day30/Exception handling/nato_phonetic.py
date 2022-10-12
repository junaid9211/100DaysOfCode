import pandas as pd 

# read the data
data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for index, row in data.iterrows()}

correct_input = False
# create nato phonetic letters for the input word
while not correct_input:
    user_input = input('Enter a word: ').upper()
    try:
        output = [nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
    else:
        correct_input = True
        print(output)