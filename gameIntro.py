#!/usr/bin/python3
import pygame
from displayText import * 
from fadetoWhite import *
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
deskBG = pygame.image.load("assets/images/deskBG.png")
computerBG = pygame.image.load("assets/images/deskBG2.png")
#doge
def gameIntro():
    done = False
    pictureCount = 0
    pictureNumber = 10
    backImage = deskBG
    character1 = jimVN
    jimX = 0
    jimY = 50
    character2 = "doge"
    dogeX = 0
    dogeY = 0
    sayWhat = 'i hate mondays'
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
                backImage = deskBG
                jimX = 0
                jimY = 50
                sayWhat = 'Press Space'
            elif pictureCount == 1:
                sayWhat = 'This is Jim. He screwed up and now plays the game "Frogs in the Night" every day.'
            elif pictureCount == 2:
                sayWhat = 'Jim is lonely and the only "friends" he has are are the internet.'
            elif pictureCount == 3:
                sayWhat = 'Today, there is a special event in "Frogs in the Night"'
            elif pictureCount == 4:
                sayWhat = ' and he plans to spend his entire day ingame.'
            elif pictureCount ==5:
                jimX = 500
                sayWhat = '"Must g-g-get the b-b-rownn frog-g-g", says Jim,'
            elif pictureCount ==6:
                sayWhat = '"need to win the g-game..."'
            elif pictureCount ==7:
                sayWhat = ''
                jimX = 1000
                backImage = computerBG

                #FitN screen

        screen.blit(backImage,(0,0))
        screen.blit(character1,(jimX,jimY))
        #screen.blit(character2,(jimX,jimY))
        messageText(sayWhat,50,550,20,screen,255,255,255,"Roboto")
        pygame.display.update()

gameIntro()
