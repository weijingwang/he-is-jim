#!/usr/bin/python3
import pygame
from displayText import *
from fadetoWhite import *
from game import * #later
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()

surface = pygame.display.set_mode((800,600))
#images
jimVNA = pygame.image.load("assets/images/jimVNA.png")
grill1 = pygame.image.load("assets/images/grill1.png")
grill2 = pygame.image.load("assets/images/grill2.png")
deskBG = pygame.image.load("assets/images/background/deskBG.png")
inHouse = pygame.image.load("assets/images/background/inHouse.png")
outHouse = pygame.image.load("assets/images/background/outHouse.png")
end = pygame.image.load("assets/images/background/end.png")
doge = pygame.image.load("assets/images/doge.png")
#Sound Effects


def gameOutro(surface):
    done = False
    pictureCount = 0
    pictureNumber = 10
    backImage = deskBG
    character1 = jimVNA
    jimX = 0
    jimY = 50
    character2 = grill1
    girlX = 10000
    girlY = 0
    character3 = doge
    dogeX = 100000
    dogeY = 0
    sayWhat = None
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
                sayWhat = '"I am in other world???",Jim said'
                dogeX = 500
            if pictureCount == 1:
                sayWhat = '"and i dont have fly power anymore? I still won game though..."'
            if pictureCount == 2:
                sayWhat = '"I think I am going to go outside..."'
            if pictureCount == 3:
                dogeX = 10000
                backImage = inHouse
                sayWhat = 'Jim heads to the door and as he opens the door,'
            if pictureCount == 4:
                sayWhat = ' a bright light starts to fill the room'
            if pictureCount ==5:
                sayWhat = 'Jim exits the house'
            if pictureCount ==6:
                backImage = outHouse
                sayWhat = '!!!'
                jimX = -100
                girlX = 600
                girlY = 100
            if pictureCount ==7:
                sayWhat = '"Oh hi Jim", Sarah said'
            if pictureCount == 8:
                sayWhat = '"I was just waiting for you to have A NICE LONG CHAT"'
            if pictureCount ==9:
                character2 = grill2
                sayWhat = '"IN ORDER TO TALK ABOUT OUR FEELINGS FOR ONE AND A HALF HOUR!"'




        surface.blit(backImage,(0,0))
        surface.blit(character1,(jimX,jimY))
        surface.blit(character2,(girlX,girlY))
        surface.blit(character3,(dogeX,dogeY))
        messageText(sayWhat,50,550,20,surface,255,255,255,"Roboto")
        pygame.display.update()
gameOutro(surface)