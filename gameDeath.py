#!/usr/bin/python3
import pygame
pygame.mixer.pre_init()
pygame.init()

#images
deadScreen = pygame.image.load("assets/images/background/youDead.png")

#menu function
def gameDeathSurface(surface):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				done = True
		surface.blit(deadScreen,(0,0))

		pygame.display.update()

