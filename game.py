#!/usr/bin/python3
import pygame
from displayText import * #KYLER DO UR CREDITS
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
gameBG = pygame.image.load("assets/images/starsBG.png")
jim = pygame.image.load("assets/images/jim.png")
#menu function
def game():
	done = False
	jimX = 350
	jimY = 470

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				pass

		#controls for jim
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT]: jimX-=7
		if pressed[pygame.K_RIGHT]: jimX+=7

		screen.blit(gameBG,(0,0))
		screen.blit(jim,(jimX,jimY))
		pygame.display.update()
game()
