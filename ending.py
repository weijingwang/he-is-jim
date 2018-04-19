import os
import pygame
from displayText import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))

front_sprites = pygame.sprite.Group()
dogecoin_sprites = pygame.sprite.Group()
middle_sprites = pygame.sprite.Group()
background_sprites = pygame.sprite.Group()

background_sprites.draw(screen)
middle_sprites.draw(screen)
dogecoin_sprites.draw(screen)
front_sprites.draw(screen)
