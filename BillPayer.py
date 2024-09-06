import random


# This is a simple program that randomly selects a person from a list of friends to be the bill payer.

randomiser = random.randint(0,4)

friends = ['John', 'Peter', 'Paul', 'Mary', 'Jane'] 

print(friends[randomiser] + " is the bill payer") # This is the bill payer 


