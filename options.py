#!/usr/bin/python3
import pygame
import os
from displayText import *
from buttons import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#surface
optionsBack = pygame.image.load("assets/images/background/optionsBG.png")
black = ((0,0,0))

def options(surface):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					done = True
		surface.blit(optionsBack,(0,0))
		button("Main Menu",320,400,150,50,True,surface)
		pygame.display.update()
