#Caesar Cipher
#This program implements the Caesar Cipher encryption and decryption algorithms.

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.

    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The number of positions to shift the characters.
        mode (str): The mode of operation, either 'encrypt' or 'decrypt'.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result