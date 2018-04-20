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
#Sound Effects
Scene1 = pygame.mixer.Sound("assets/music/introVoice/0.ogg")

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
                sayWhat = 'Press Space'
            elif pictureCount == 1:
                pygame.mixer.stop()
                sayWhat = 'This is Jim. After High School, he somehow decided to be a hardcore gamer boy'
                Scene1.play()
            elif pictureCount == 2:
                pygame.mixer.stop()
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
                sayWhat = '"WHAHAHAHATATATATAT GET OFF MY KEYBOARD", Jim shouted'
            elif pictureCount == 17:
                sayWhat = '"I AM GOING TO LOSE THE GAME WHAT THE HECK"'
            elif pictureCount ==18:
                character2 = dogeLeft
                sayWhat = '"No...", said the magic doge'
            elif pictureCount ==19:
                sayWhat = '"watch this my man"'
            elif pictureCount ==20:
                dogeY = 10
            elif pictureCount == 21:
                dogeY = 70
            elif pictureCount == 22:
                sayWhat = 'the magic doge is secret coder'
            elif pictureCount == 23:
                sayWhat = 'and he typed: "wafuinwoq39df'
            elif pictureCount == 24:
                sayWhat = '"Boohoo hoo, no i will never win", said Jim as he raised his head'
            elif pictureCount ==25:
                sayWhat = '"NANI IS HAPPEN!?", Jim Shouted as he looked at his monitor'
                jimX = 500
                character2 = dogeRight
                dogeX = 70
            elif pictureCount == 26:
                sayWhat ='"You..YY.YOU maake mmee wi-wi-w-win game!", Jim mumbled in amazement'
            elif pictureCount ==27:
                backImage =deskBG
                dogeX = -110
                sayWhat = "Jim is stunned and decides to become Doge's first worshipper"
            elif pictureCount ==28:
                sayWhat = '"here is one of my favorite cookies, here try one", Jim says to the doge'
            elif pictureCount ==29:
                sayWhat = '"No thanks, maybe next time", the magic Doge replied.'
            elif pictureCount == 30:
                sayWhat = '"no problemo", said the Jim'
            elif pictureCount == 31:
                sayWhat = '"By the way thanks for becoming my first follower",doge say'
            elif pictureCount ==32:
                sayWhat = '"much thank much wowzies"'
            elif pictureCount ==33:
                sayWhat = '"Oh, I know! wanna see something cool?"'
            elif pictureCount == 34:
                sayWhat = '"sure what is???", Jim say again with curiousity'
                #FitN screen
            elif pictureCount ==35:
                sayWhat = '...'
            elif pictureCount == 36:
                sayWhat='doge does magic ritual DEFINITELY NOT EVIL'
            elif pictureCount ==37:
                character1 = jimVNBuff
                sayWhat = 'WHA NANI HAPPEN!!??'
            elif pictureCount == 38:
                sayWhat = '"okok so you can fly cool yes?", doge explains'
            elif pictureCount == 39:
                sayWhat = '"But what is even cooler is if you fly to----"'
            elif pictureCount == 40:
                sayWhat = '"THE OTHER WORLD, so there are TWO WORLDS,"'
                character2 = dogeLeft
            elif pictureCount == 41:
                character2 == dogeRight
                sayWhat = '"I give you co-leader okok? BUT when flying to other world,"'
            elif pictureCount == 42:
                sayWhat = '"There are evil space rocks that might kill you."'
            elif pictureCount == 43:
                sayWhat = '"so what you wanna do is press keys on keyboard and kill space rocks yes?"'
            elif pictureCount == 44:
                sayWhat = '"All right I got it I am in", replied Jim with exitement'

        screen.blit(backImage,(0,0))
        screen.blit(character1,(jimX,jimY))
        screen.blit(character2,(dogeX,dogeY))
        messageText(sayWhat,50,550,20,screen,255,255,255,"Roboto")
        pygame.display.update()

gameIntro()
