#Rock Paper Scissors Game
# This is a simple rock paper scissors game that allows the user to play against the computer.
# The computer's choice is randomly generated.
# The game is played until the user decides to quit.
# The user's score is displayed at the end of each game.
# The user can choose to play again or quit.

import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_game(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print("Computer chose:", computer_choice)
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            print("Your score:", self.user_score)
            print("Computer's score:", self.computer_score)
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
