#!/usr/bin/python3
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

#images
jimVN = pygame.image.load("assets/images/jimVN.png")

def gameIntro():
    done = False
    pictureCount = 0
    pictureNumber = 10
    backImage = jimVN
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pictureCount +=1
                    print(pictureCount)
            if pictureCount > pictureNumber:
                #start game
                pass

            if pictureCount == 0:
                backImage = jimVN
        screen.fill(black)
        screen.blit(jimVN,(0,0))
        pygame.display.update()

gameIntro()
