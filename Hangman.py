import random

# Hangman stages
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
========='''
]

# Function to play the game
def play_hangman():
    print("Welcome to Hangman!")

    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lifes = 0
    display = ['_'] * word_length  # Create a display list with underscores
    guessed_letters = []  # List to track guessed letters

    print("Word to guess:")
    print(f"{' '.join(display)}")  # Show initial underscores

    while '_' in display and lifes < len(hangman) - 1:  # Loop until word is guessed or lives run out
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        # If the guessed letter is not in the word
        if guess not in chosen_word:
            print(f"Letter '{guess}' is not in the word.")
            lifes += 1
            print(hangman[lifes])  # Show the hangman stage
        else:
            # Reveal all occurrences of the guessed letter in the word
            found = False
            for i, ch in enumerate(chosen_word):
                if ch == guess and display[i] == '_':  # Reveal all unrevealed occurrences
                    display[i] = guess
                    found = True

            if found:
                print(f"{' '.join(display)}")  # Show the updated display
            else:
                print(f"All occurrences of '{guess}' have already been revealed.")

    # Check if the player won or lost
    if '_' not in display:
        print(f"Congratulations! You guessed the word: {chosen_word}, you win!")
    else:
        print("Game Over! You ran out of lives.")
        print(f"The word was: {chosen_word}")

# Main loop to allow retry
while True:
    play_hangman()
    retry = input("Do you want to play again? (yes/no): ").lower()
    if retry != 'yes':
        print("Thanks for playing!")
        break
