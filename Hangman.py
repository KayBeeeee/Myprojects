# This game is called Hangman
# It is a game where the player has to guess a word by guessing one letter at a time
# The player has a limited number of guesses before they lose
# The game ends when the player guesses all the letters in the word or runs out of guesses
import random

hangman = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''' ]



print("Welcome to Hangman!")



word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word) 
end_of_game = False
lifes = 0
display = []
for _ in range(word_length):
 display += "_"
#print(hangman[6 - lives])
print("Word to guess:")
print(f"{' '.join(display)}")

display = ['_'] * len(chosen_word)  # Create a display list with underscores for each letter
guessed_letters = []  # List to track all guessed letters

while '_' in display:  # Continue until the word is fully guessed
    guess = input("Guess a letter: ").lower()  # Prompt the user for a letter

    if guess not in chosen_word:  # If the letter is not in the word
        print(f"Letter '{guess}' is not in the word.")
        lifes += 1
        hangman[lifes]
        print(hangman[lifes])


        continue
    
    guessed_letters.append(guess)  # Add the guess to the list of guessed letters

    # Find the first occurrence of the guessed letter that hasn't been revealed
    found = False
    for i, ch in enumerate(chosen_word):
        if ch == guess and display[i] == '_':  # Reveal one unrevealed occurrence
            display[i] = guess
            found = True
            break  # Stop after revealing one occurrence

    if found:
        print(f"{' '.join(display)}")  # Print the updated display
    else:
        print(f"You have already revealed all occurrences of '{guess}'.")

print(f"Congratulations! You guessed the word: {chosen_word}")



        





















    #     lives -= 1
    #     print(hangman[6 - lives])
    #     print(f"{' '.join(display)}")
    #     if lives == 0:
    #         end_of_game = True
    #         print("You lose.")
    #         print(f"The word was {chosen_word}")
    #         break
    #     continue
    # for position in range(word_length):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #         display[position] = letter
    #         print(hangman[6 - lives])
    #         print(f"{' '.join(display)}")
    #         if "_" not in display:
    #             end_of_game = True
    #             print("You win!")
    #             break
    #         break
    #     elif position == word_length - 1:
    #         lives -= 1
    #         print(hangman[6 - lives])
    #         print(f"{' '.join(display)}")
    #         if lives == 0:
    #             end_of_game = True
    #             print("You lose.")
    #             print(f"The word was {chosen_word}")
    #             break
    #         break
    #     else:
    #         continue
        


            



