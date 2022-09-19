from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run = 'yes'

def encrypt(plain_text, shift):
    cipher_text = ''
    for char in plain_text:
        if char in alphabet:
            index = alphabet.index(char)
            index += shift 
            index = adjust_index(index)
            shifted_char = alphabet[index]
            cipher_text += shifted_char
        else:
            cipher_text += char

    return cipher_text


def decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char in alphabet:
            index = alphabet.index(char)
            index -= shift 
            index = adjust_index(index)
            shifted_char = alphabet[index]
            decrypted_text += shifted_char
        else:
            decrypted_text += char

    return decrypted_text        


def adjust_index(index):
    if index > 25:
        while index > 25:
            index -= 26

    elif index < 0:
        while index < 0:
            index += 26
    return index


    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

print(logo)

while run == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()

    while True:
        shift = input("Type the shift number:\n")
        if not shift.isdigit():
            print(f'Shift can only be an integer value, you provided {shift}')
        else:
            shift = int(shift)
            break

    if direction == 'encode':
        encrypted_text = encrypt(text, shift)
        print(f'Here\'s the encoded result: {encrypted_text}')
    elif direction =='decode':
        decrypted_text = decrypt(text, shift)
        print(f'Here\'s the decoded result: {decrypted_text}')
    else:
        print(f"error, you can only provide two options 'encode' and 'decode', you provided {direction}")
        continue

    run = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
