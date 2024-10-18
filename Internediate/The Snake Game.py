#The Snake Game
#Rules: 
#1. The snake moves forward, unless it eats a food item, in which case the food item disappears and the snake grows longer.
#2. The snake cannot go off the screen.
#3. The snake cannot go over itself.

# This used to be one of favourites on the Nokia 3310, hahah!

import pygame
import random
import time
import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from collections import deque
from pygame.locals import *



class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.reset_game() # Initialize the game state

    def reset_game(self):
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_position = [random.randrange(1, (self.screen_width // 10)) * 10,
                             random.randrange(1, (self.screen_height // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0 # Initialize the score

    def draw_score(self):
        score_text = self.font.render("Score: " + str(self.score), True, (0, 0, 0))
        self.screen.blit(score_text, [1, 1]) # Draw the score on the screen

    def game_over(self):
        game_over_text = self.font.render("Game Over! Press R to Restart", True, (0, 0, 0))
        self.screen.blit(game_over_text, [self.screen_width // 3, self.screen_height // 2])
        pygame.display.flip()
        time.sleep(2) # Pause for 2 seconds before restarting
        self.reset_game() # Reset the game state after game over

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.change_to = 'RIGHT'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.change_to = 'LEFT'
                    elif event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.change_to = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.change_to = 'DOWN'
                    elif event.key == pygame.K_r:
                        self.reset_game() # Reset the game state when 'R' is pressed

            # Move the snake
            if self.change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT' # Update the direction
            elif self.change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT' # Update the direction
            elif self.change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP' # Update the direction 
            elif self.change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN' # Update the direction # Update the direction

            # Move the snake
            if self.direction == 'RIGHT':
                self.snake_position[0] += 10 # Move right
            elif self.direction == 'LEFT':
                self.snake_position[0] -= 10 # Move left 
            elif self.direction == 'UP':
                self.snake_position[1] -= 10 # Move up # Move up
            elif self.direction == 'DOWN':
                self.snake_position[1] += 10 # Move down # Move down

            # Grow the snake when eating food
            self.snake_body.insert(0, list(self.snake_position))  



    def main(self):
        self.run() # Start the game loop
        pygame.quit() # Quit the game
        quit() # Exit the program
        sys.exit() # Exit the program
        






        


            

    






