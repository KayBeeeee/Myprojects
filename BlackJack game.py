# This is a BlackJack game
# rules:
#These are the rules for the game

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random




cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards) 


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # BlackJack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) # Ace = 11
        cards.append(1) # Ace = 1
    return sum(cards) # Return the sum of the cards


def compare(user_score, computer_score):
    """Compare the user's score with the computer's score and return the result."""
    if user_score == computer_score:
        return "Draw" # Draw
    elif computer_score == 0:
        return "Lose, opponent has BlackJack" # Lose, opponent has BlackJack    
    elif user_score == 0:
        return "Win with a BlackJack" # Win with a BlackJack 
    elif user_score > 21:
        return "You went over. You lose" # You went over. You lose 
    elif computer_score > 21:
        return "Opponent went over. You win" # Opponent went over. You win 
    elif user_score > computer_score:
        return "You win" # You win 
    else:
        return "You lose" # You lose 


def play_game():
    """Play the BlackJack game."""
    user_cards = [] # User's cards
    computer_cards = [] # Computer's cards 
    is_game_over = False # Game over flag

    for _ in range(2): # Deal two cards to the user and computer
        user_cards.append(deal_card())
        computer_cards.append(deal_card()) # Deal two cards to the user and computer

    while not is_game_over:
        user_score = calculate_score(user_cards) # Calculate the user's score 
        computer_score = calculate_score(computer_cards) # Calculate the computer's score
        print(f"Your cards: {user_cards}, current score: {user_score}") # Print the user's cards and score
        print(f"Computer's first card: {computer_cards[0]}") # Print the computer's first card and score

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True # Game over if the user has BlackJack, the computer has BlackJack, or the user goes over
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ") # Ask the user if they want another card or pass
            if user_should_deal == "y":
                user_cards.append(deal_card()) # Deal another card to the user if they want
            else:
                is_game_over = True # Game over if the user passes if they want another card

    while computer_score != 0 and computer_score < 17: # Deal cards to the computer until its score is 17 or more
        computer_cards.append(deal_card()) # Deal another card to the computer
        computer_score = calculate_score(computer_cards) # Calculate the computer's score after dealing a card

    print(f"Your final hand: {user_cards}, final score: {user_score}") # Print the user's final hand and score 
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}") # Print the computer's final hand and score 
    print(compare(user_score, computer_score)) # Print the result of the game (Win, Lose, Draw, etc.)

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y": # Ask the user if they want to play again
    play_game() # Play the game
    print("\n") # Print a blank line for better readability
    print("Thank you for playing BlackJack!") # Print a thank you message
    











