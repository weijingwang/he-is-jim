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
gameBG1 = pygame.image.load("assets/images/stars1BG.png")
gameBG2 = pygame.image.load("assets/images/stars2BG.png")
gameBG3 = pygame.image.load("assets/images/stars3BG.png")
gameBG4 = pygame.image.load("assets/images/stars4BG.png")
jim = pygame.image.load("assets/images/jim.png")
#menu function
def game():
	done = False
	jimX = 350
	jimY = 470
	backgroundCount = 0
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				pass
		# if backgroundCount == 0:
		# 	backImage = gameBG1
		# 	print(backgroundCount)
		# elif backgroundCount == 1:
		# 	backImage = gameBG2
		# 	print(backgroundCount)
		# elif backgroundCount == 2:
		# 	backImage = gameBG3
		# 	print(backgroundCount)
		# elif backgroundCount == 3:
		# 	backImage = gameBG4
		# 	print(backgroundCount)
		# elif backgroundCount == -1:
		# 	backgroundCount =3
		# 	print(backgroundCount)
		# elif backgroundCount == 4:
		# 	backgroundCount=0
		# 	print(backgroundCount)


		#controls for jim
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT]: 
			jimX-=7
			backgroundCount-=1
		if pressed[pygame.K_RIGHT]: 
			jimX+=7
			backgroundCount+=1

		screen.blit(gameBG3,(0,0))
		screen.blit(jim,(jimX,jimY))
		pygame.display.update()
game()
