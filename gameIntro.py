#!/usr/bin/python3
import pygame
from displayText import *
from fadetoWhite import *
from game import * #later
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()


#images
jimVN = pygame.image.load("assets/images/jimVN.png")
jimVNBuff = pygame.image.load("assets/images/jimVNCool.png")
dogeRight = pygame.image.load("assets/images/dogeMan.png")
dogeLeft = pygame.image.load("assets/images/dogeMan1.png")
deskBG = pygame.image.load("assets/images/background/deskBG.png")
computerBG = pygame.image.load("assets/images/background/deskBG2.png")
farewell = pygame.image.load("assets/images/background/farewell.png")
#Sound Effects
Scene0 = pygame.mixer.Sound("assets/music/introVoice/0.ogg")
Scene1 = pygame.mixer.Sound("assets/music/introVoice/1.ogg")
Scene2 = pygame.mixer.Sound("assets/music/introVoice/2.ogg")
Scene3 = pygame.mixer.Sound("assets/music/introVoice/3.ogg")
Scene4 = pygame.mixer.Sound("assets/music/introVoice/4.ogg")
Scene5 = pygame.mixer.Sound("assets/music/introVoice/5.ogg")
Scene6 = pygame.mixer.Sound("assets/music/introVoice/6.ogg")
Scene7 = pygame.mixer.Sound("assets/music/introVoice/7.ogg")
Scene9 = pygame.mixer.Sound("assets/music/introVoice/9.ogg")
Scene10 = pygame.mixer.Sound("assets/music/introVoice/10.ogg")
Scene15 = pygame.mixer.Sound("assets/music/introVoice/15.ogg")
Scene16 = pygame.mixer.Sound("assets/music/introVoice/16.ogg")
Scene17 = pygame.mixer.Sound("assets/music/introVoice/17.ogg")
Scene18 = pygame.mixer.Sound("assets/music/introVoice/18.ogg")
Scene45 = pygame.mixer.Sound("assets/music/introVoice/45.ogg")
Scene46 = pygame.mixer.Sound("assets/music/introVoice/46.ogg")


def playVoice(whichVoice):
    pygame.mixer.stop()
    whichVoice.play()

def gameIntro(surface):
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
                playVoice(Scene0)
                backImage = deskBG
                jimX = 0
                jimY = 50
                sayWhat = 'Press Space and make sure to not move the mouse or press any other buttons'
            elif pictureCount == 1:
                playVoice(Scene1)
                sayWhat = 'This is Jim. After High School, he somehow decided to be a hardcore gamer boy'

            elif pictureCount == 2:
                playVoice(Scene2)
                sayWhat = 'and now plays the game "Frogs in the Night" every day.'
            elif pictureCount == 3:
                sayWhat = 'Jim is lonely and the only "friends" he has are on the internet.'
                playVoice(Scene3)
            elif pictureCount == 4:
                sayWhat = 'Today, there is a special event in "Frogs in the Night"'
                playVoice(Scene4)
            elif pictureCount == 5:
                sayWhat = ' and he plans to spend his entire day ingame.'
                playVoice(Scene5)
            elif pictureCount ==6:
                jimX = 500
                sayWhat = '"Must g-g-get the b-b-rownn frog-g-g", says Jim,'
                playVoice(Scene6)
            elif pictureCount ==7:
                sayWhat = '"need to win the g-game..."'
                playVoice(Scene7)
            elif pictureCount ==8:
                sayWhat = '...'
                jimX = 1000
                backImage = computerBG
            elif pictureCount == 9:
                sayWhat = '"oh no... I have the case of the lose!"'
                playVoice(Scene9)
            elif pictureCount == 10:
                sayWhat = '"will NOT lose but can?"'
                playVoice(Scene10)
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
                playVoice(Scene15)
                sayWhat = 'WOOOWWWZZZ'
            elif pictureCount == 16:
                playVoice(Scene16)
                sayWhat = '"WHAHAHAHATATATATAT GET OFF MY KEYBOARD", Jim shouted'
            elif pictureCount == 17:
                playVoice(Scene17)
                sayWhat = '"I AM GOING TO LOSE THE GAME WHAT THE HECK"'
            elif pictureCount ==18:
                playVoice(Scene18)
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
                #FitN surface
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
                sayWhat = '"I give you co-leader okok? BUT when flying to other world,"'
            elif pictureCount == 42:
                sayWhat = '"There are evil space rocks that might kill you."'
                character2 == dogeRight
            elif pictureCount == 43:
                sayWhat = '"so what you wanna do is press keys on keyboard and kill space rocks yes?"'
            elif pictureCount == 44:
                sayWhat = '"All right I got it I am in", replied Jim with exitement'
            elif pictureCount == 45:
                jimX = 10000
                dogeX = 10000
                backImage = farewell
                sayWhat = 'And so Jim flew away to see if he could reach the second world and get co-leader'
                playVoice(Scene45)
            elif pictureCount == 46:
                sayWhat = 'Go Jim! Good Luck Jim! Let us see if you are cool enough to join the kool klub!'
                playVoice(Scene46)
            elif pictureCount == 47:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/music/HopeForADog.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
                game(surface) # don't add yet since still developing
        surface.blit(backImage,(0,0))
        surface.blit(character1,(jimX,jimY))
        surface.blit(character2,(dogeX,dogeY))
        messageText(sayWhat,50,550,20,surface,255,255,255,"Roboto")
        pygame.display.update()
