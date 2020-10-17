import pygame
from pygame.locals import*
import math
import random

# Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Calibri',25,True, False)
pygame.display.set_caption("MyGame")

# Loop until the user clicks the close button
done = False

# used to manage time .. how fast the screen updates
clock = pygame.time.Clock()

class enemy(pygame.sprite.Sprite):
    # Define the constructor function

    def __init__(self, color, width, height, speed):
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
             self.reset_pos()
             
    def reset_pos(self):
        self.rect.x = random.randrange(0,690)
        self.rect.y = 0

class attacker(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.rect.x = 200
        self.rect.y = 490

    def get_x(self):
        return self.rect.x

    def update(self):
        if self.rect.x < 0 or self.rect.x > 690:
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 690:
                self.rect.x = 690
        else:    
            self.rect.x = self.rect.x + x_speed

class bullet(pygame.sprite.Sprite):

    def __init__(self, color, width, height,x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.y_speed = -3
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self):
        if self.rect.y < 0:
            self.rect.y = -50
        else:
            self.rect.y = self.rect.y + self.y_speed

block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
x_speed = 0
y_speed = 1
score = 0
no_of_blocks = 6
lives = 3
bullet_count = 0
start_game_flag = True
player = attacker(RED,10,10)
all_sprites_list.add(player)

def start_game(speed, blocks):            
    global lives
    lives = lives + 1
    global bullet_count
    bullet_count = 0
    for x in range(blocks):
        my_enemy = enemy(WHITE, 10, 10,speed)
        block_list.add(my_enemy)
        all_sprites_list.add(my_enemy)
        

#Main program Loop

while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                if bullet_count > 49:
                    pass
                else:
                    mybullet = bullet(RED,5,5, player.get_x(), 490)
                    all_sprites_list.add(mybullet)
                    bullet_list.add(mybullet)
                    bullet_count += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0

                
    # Game logic goes in here
    if start_game_flag == True:
        start_game_flag = False
        start_game(y_speed, no_of_blocks)
        y_speed += 1
        no_of_blocks += 1
        
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    bullet_hit_list = pygame.sprite.groupcollide(block_list, bullet_list, True, False)

    for foo in blocks_hit_list:
        lives -= 1
        score -= 30
        foo.reset_pos()

    for me in bullet_hit_list:
        score +=20

    if lives == 0:
        done = True

    if not block_list:
        start_game_flag = True

    all_sprites_list.update()
    

    # Drawing code goes in here
    screen.fill(BLACK)

    text = font.render("Lives: " + str(lives),True,WHITE)
    screen.blit(text,[30,30])
    text = font.render("Score: " + str(score),True,WHITE)
    screen.blit(text,[30,60])
    text = font.render("Bullets: " + str(50 - bullet_count),True,WHITE)
    screen.blit(text,[30,90])
    
    all_sprites_list.draw(screen)

    
    # update the screen
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()


