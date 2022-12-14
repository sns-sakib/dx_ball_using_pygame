import pygame
from config import Config

cfg = Config()
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.size_scaler = cfg.SCREEN_SCALER
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


    def moveLeft(self, pixels):
        self.rect.x -= pixels*self.size_scaler[0]
	    #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels*self.size_scaler[0]
        #Check that you are not going too far (off the screen)
        if self.rect.x > 700*self.size_scaler[0]:
          self.rect.x = 700*self.size_scaler[0]

    def moveUp(self, pixels):
        self.rect.y += pixels*self.size_scaler[1]
        #Check that you are not going too far (off the screen)
        if self.rect.y > 560*self.size_scaler[1]:
          self.rect.y = 560*self.size_scaler[1]

    def moveDown(self, pixels):
        self.rect.y -= pixels*self.size_scaler[0]
        #Check that you are not going too far (off the screen)
        if self.rect.y < 40*self.size_scaler[1]:
          self.rect.y = 40*self.size_scaler[1]