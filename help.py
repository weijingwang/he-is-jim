#!/usr/bin/python3
import pygame
import os
from displayText import *
from buttons import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
helpBG = pygame.image.load("assets/images/background/helpBG.png")
def helps(surface):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					done = True
		surface.blit(helpBG,(0,0))
		# messageText("Help",325,30,40,surface,255,255,255,"ComicSans")
		# messageText("Press the Letter on keyboard on the rock the rock to kill it",100,90,20,surface,255,255,255,"ComicSans")
		# messageText("sometimes, there will be multiple letters. ",100,120,20,surface,255,255,255,"ComicSans")
		# messageText("That means you have to press them all at once.",100,150,20,surface,255,255,255,"ComicSans")
		# messageText("There may be a boss somewhere in the game.",100,180,20,surface,255,255,255,"ComicSans")
		# messageText("It may not die even after entering lots of keys!",100,210,20,surface,255,255,255,"ComicSans")
		button("Main Menu",320,400,150,50,True,surface)
		pygame.display.update()

