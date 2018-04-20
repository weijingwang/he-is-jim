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
jimVNBuff = pygame.image.load("assets/images/jimVNCool.png")
dogeRight = pygame.image.load("assets/images/dogeMan.png")
dogeLeft = pygame.image.load("assets/images/dogeMan1.png")
deskBG = pygame.image.load("assets/images/background/deskBG.png")
computerBG = pygame.image.load("assets/images/background/deskBG2.png")
#doge
def gameIntro():
    done = False
    pictureCount = 0
    pictureNumber = 10
    backImage = deskBG
    character1 = jimVN
    jimX = 0
    jimY = 50
    character2 = dogeRight
    dogeX = 100000
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
                sayWhat = 'This is Jim. After High School, he somehow decided to be a hardcore gamer boy'
            elif pictureCount == 2:
                sayWhat = 'and now plays the game "Frogs in the Night" every day.'
            elif pictureCount == 3:
                sayWhat = 'Jim is lonely and the only "friends" he has are on the internet.'
            elif pictureCount == 4:
                sayWhat = 'Today, there is a special event in "Frogs in the Night"'
            elif pictureCount == 5:
                sayWhat = ' and he plans to spend his entire day ingame.'
            elif pictureCount ==6:
                jimX = 500
                sayWhat = '"Must g-g-get the b-b-rownn frog-g-g", says Jim,'
            elif pictureCount ==7:
                sayWhat = '"need to win the g-game..."'
            elif pictureCount ==8:
                sayWhat = '...'
                jimX = 1000
                backImage = computerBG
            elif pictureCount == 9:
                sayWhat = '"oh no... I have the case of the lose!"'
            elif pictureCount == 10:
                sayWhat = '"will NOT lose but can?"'
            elif pictureCount == 11:
                sayWhat = '...'
            elif pictureCount == 12:
                sayWhat = '. ..'
            elif pictureCount == 13:
                sayWhat = '.. .'
            elif pictureCount == 14:
                sayWhat = '...'
            elif pictureCount == 15:
                dogeX = 100
                dogeY = 100
                sayWhat = 'WOOOWWWZZZ'
            elif pictureCount == 16:
                sayWhat = '"WHAHAHAHATATATATAT GET OF MY KEYBOARD", Jim shouted'
            elif pictureCount == 17:
                sayWhat = '"I AM GOING TO LOSE THE GAME WHAT THE HECK"'
            elif pictureCount ==18:
                character2 = dogeLeft
                sayWhat = '"No...", said the magic doge'
            elif pictureCount ==19:
                sayWhat = '"watch this my man"'

                #FitN screen

        screen.blit(backImage,(0,0))
        screen.blit(character1,(jimX,jimY))
        screen.blit(character2,(dogeX,dogeY))
        messageText(sayWhat,50,550,20,screen,255,255,255,"Roboto")
        pygame.display.update()

gameIntro()
