#Caesar Cipher
#This program implements the Caesar Cipher encryption and decryption algorithms
#It takes a string and a key as input, and returns the encrypted or decrypted string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#This function encrypts the given text using the Caesar Cipher algorithm
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")