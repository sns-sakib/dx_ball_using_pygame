#Import the pygame library and initialise the game engine
import pygame
from components.bullet import Bullet
from components.paddle import Paddle
from components.ball import Ball
from components.brick import Brick
from components.bullet import Bullet
from utils import *
from components.button import Button
from config import Config



cfg = Config()
    # Define some colors

if __name__ == "__main__":
    pygame.init()
    
    screen_size = cfg.SIZE
     # Open a new window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Breakout Game")

    # call the staring window
    stage1(screen)
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()