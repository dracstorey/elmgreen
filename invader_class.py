import pygame
from pygame.locals import*
import math
import random

# Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invader")

# Loop until the user clicks the close button
done = False

# used to manage time .. how fast the screen updates
clock = pygame.time.Clock()

class enemy(pygame.sprite.Sprite):
    # Define the constructor function

    def __init__(self, color, width, height, speed):
        ## Initialise sprite class (super class)
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = speed
        self.rect.x = random.randrange(0,600)
        self.rect.y = 0

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.y > 500:
            self.rect.x = random.randrange(0,690)
            self.rect.y = 0


# Create enemy and all sprite group
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
blocks = 6

## Create invaders
for x in range(blocks):
    my_enemy = enemy(WHITE, 10, 10,5)
    block_list.add(my_enemy)
    all_sprites_list.add(my_enemy)
        

#Main program Loop

while not done:
    # Main event loo

                
    # Game logic goes in here

    all_sprites_list.update()

    # Drawing code goes in here
    screen.fill(BLACK)
    
    all_sprites_list.draw(screen)

    
    # update the screen
    pygame.display.flip()
    # Tick the clock round
    clock.tick(60)
    
pygame.quit()


