import pygame
from config import Config

cfg = Config
BLACK = (0,0,0)



class Bullet(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        # self.image = pygame.Surface([width, height])
        bullet_image_path = cfg.BULLET_IMAGE_PATH
        self.rect = pygame.Rect(width, height, 16, 16)
        self.image = pygame.image.load(bullet_image_path)
      
        # Fetch the rectangle object that has the dimensions of the image.
        # self.rect = self.image.get_rect()
    def update(self):
        # Makes the enemy move in the x direction.
        # self.rect.move(0, self.dy)
        # self.rect.y += self.dy
        pass