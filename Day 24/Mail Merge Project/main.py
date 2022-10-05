# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# get the letter template
with open('Input/Letters/starting_letter.txt') as f:
    template = f.read()

# get the names of all the people
with open('Input/Names/invited_names.txt') as f:
    names = f.readlines()
    # for each name in the invited_names.txt file
for name in names:
    name = name.strip()

    # create the letter
    file_name = f'letter_for_{name}.txt'
    letter_to_send = template.replace('[name]', name)

    # save the letter
    with open(f'Output/ReadyToSend/{file_name}', mode='w') as letter:
        letter.write(letter_to_send)
        print(f'Written letter for {name}')

