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

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()



