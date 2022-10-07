import pandas as pd 

# read the data
data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for index, row in data.iterrows()}

# create nato phonetic letters for the input word
user_input = input('Enter a word: ').upper()
output = [nato_alphabet[letter] for letter in user_input]
print(output)