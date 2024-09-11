# Caesar Cipher Program for Encryption and Decryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encrypt function using Caesar Cipher
def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

# Decrypt function using Caesar Cipher
def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % len(alphabet)
            plain_text += alphabet[new_position]
        else:
            plain_text += letter
    return plain_text

# Main logic to choose between encoding and decoding
if direction == "encode":
    encoded_text = encrypt(text, shift)
    print(f"The encoded text is {encoded_text}")
    
    # Optionally decode immediately to check if it matches the original
   # decoded_text = decrypt(encoded_text, shift)
  #  print(f"Decoded back: {decoded_text}")
    
  #  if decoded_text == text:
  #      print("The decoded text matches the original input!")
   # else:
     #   print("The decoded text does NOT match the original input.")

elif direction == "decode":
    decoded_text = decrypt(text, shift)
    print(f"The decoded text is {decoded_text}")
else:
    print("Invalid input. Please try again.")
