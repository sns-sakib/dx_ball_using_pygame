import pygame
BLACK = (0,0,0)

class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.dy = 1
        self.color = color
        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    def update(self):
        # Makes the enemy move in the x direction.
        # self.rect.move(0, self.dy)
        self.rect.y += self.dy
        # pass
    def change_color(self, color):

        size = self.image.get_size()
        self.image = pygame.Surface(size)
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.dy = 1
        self.color = color
        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])