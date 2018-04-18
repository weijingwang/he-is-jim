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

pictureCount = 0

def introImage(img):
    backImage = pygame.image.load(img)
    return backImage

def gameIntro():
    while not done:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			quit()
    		if event.type == pygame.KEYDOWN:
    			pass

            if pressed[pygame.K_SPACE]:
                pictureCount+=1

            if pictureCount == 1:
                introImage(img)
            elif pictureCount ==2:
                introImage(img)
            elif pictureCount ==3:
                introImage(img)
            elif pictureCount ==4:
                introImage(img)
            elif pictureCount ==5:
                introImage(img)
            elif pictureCount ==6:
                introImage(img)
            elif pictureCount ==7:
                introImage(img)
            elif pictureCount ==8:
                introImage(img)
            elif pictureCount ==9:
                introImage(img)
            elif pictureCount ==10:
                    introImage(img)

        screen.blit(backImage,(0,0))
		pygame.display.update()
