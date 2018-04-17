#!/usr/bin/python3
import pygame
from displayText import *
from main_menu import * 
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()

x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))

main_menu(screen)