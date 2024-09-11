# This is a BlackJack game
# rules:


# Objective:
# - The goal is to beat the dealer's hand without going over 21.
# - Try to get as close to 21 as possible without exceeding it.

# Card Values:
# - Number Cards (2-10): Face value.
# - Face Cards (Jacks, Queens, Kings): Worth 10 points each.
# - Aces: Worth either 1 or 11 points, depending on which is more favorable for the hand.

# Gameplay:
# 1. Initial Deal:
#    - Each player is dealt two cards.
#    - The dealer is dealt two cards (one face up, one face down).

# 2. Player's Turn:
#    - Players can choose from the following actions:
#      - Hit: Take an additional card.
#      - Stand: Keep their current hand.
#      - Double Down: Double their bet and receive only one more card.
#      - Split: If the two initial cards are of the same rank, split them into two separate hands.
#      - Surrender: Forfeit half their bet and end their turn (if allowed).

# 3. Dealer's Turn:
#    - After all players have acted, the dealer reveals their face-down card.
#    - The dealer must hit until their hand totals 17 or higher.
#    - In some games, the dealer must hit on a soft 17 (a hand containing an Ace valued as 11).

# 4. Winning and Losing:
#    - If a player's hand is closer to 21 than the dealer's hand without exceeding 21, the player wins.
#    - If a player's hand exceeds 21, they lose regardless of the dealer's hand.
#    - If the dealer's hand exceeds 21, all remaining players win.
#    - If both the player and dealer have the same total (21 or less), it's a push, and the player gets their bet back.


import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



