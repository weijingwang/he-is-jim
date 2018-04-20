#!/usr/bin/python3
import pygame
import os
import random
from displayText import * #KYLER DO UR CREDITS
from credits import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
#images
gameBG3 = pygame.image.load("assets/images/background/stars3BG.png")

#boss
def bossLevel():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		screen.blit(gameBG3,(0,0))
		#messageText("Jim",100,100,100,screen,255,255,255)
		print("EBFKSBDS")
		pygame.display.update()
bossLevel()


def boss():
	pass
    
