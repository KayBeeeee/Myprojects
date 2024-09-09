# This game is called Hangman
# It is a game where the player has to guess a word by guessing one letter at a time
# The player has a limited number of guesses before they lose
# The game ends when the player guesses all the letters in the word or runs out of guesses
import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []
for _ in range(word_length):
    display += "_"
    print(hangman[6 - lives])
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
        lives -= 1
        print(hangman[6 - lives])
        print(f"{' '.join(display)}")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")
            break
        continue
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(hangman[6 - lives])
            print(f"{' '.join(display)}")
            if "_" not in display:
                end_of_game = True
                print("You win!")
                break
            break
        elif position == word_length - 1:
            lives -= 1
            print(hangman[6 - lives])
            print(f"{' '.join(display)}")
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}")
                break
            break
        else:
            continue
        


            



