#!/usr/bin/python3
import pygame
pygame.mixer.pre_init()
pygame.init()

#images
deadScreen = pygame.image.load("assets/images/background/youDead.png")
#music
pygame.mixer.music.load("assets/music/gameOver.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)

#menu function
def gameDeathScreen(surface):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				done = True
		surface.blit(deadScreen,(0,0))

		pygame.display.update()

