# Secret Auction

import os


class SecretAuction:
    def __init__(self):
        self.bids = {}  # Dictionary for bidder names and bids
        self.highest_bid = 0  # Highest bid amount
        self.winner = ""  # Name of the winner
        self.more_bidders = True  # Flag for more bidders

        self.clear_console()  # Clear console initially
        print("Welcome to the Secret Auction!")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def bidDetails(self):
        while self.more_bidders:
            name = input("What is your name?: ")
            bid = int(input("What is your bid?: $"))
            self.bids[name] = bid

            # Update highest bid if current bid is higher
            if bid > self.highest_bid:
                self.highest_bid = bid
                self.winner = name  # Update winner if highest

            more = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
            if more == "yes":
                self.clear_console()  # Clear for the next bidder
            elif more == "no":
                self.more_bidders = False
                self.clear_console()  # Clear before displaying winner
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
                continue  # Ask for input again

    def findWinner(self):
        if self.bids:  # Check if there were any bids
            print(f"The winner is {self.winner.capitalize()} with a bid of ${self.highest_bid}.")
        else:
            print("No bids received.")

# Creating an instance of the SecretAuction class and start the auction
auction = SecretAuction()
auction.bidDetails()
auction.findWinner()