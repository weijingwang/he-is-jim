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
jimVN = pygame.image.load("assets/images/jimVN.png")
grill1 = pygame.image.load("assets/images/grill1.png")
grill2 = pygame.image.load("assets/images/grill2.png")
deskBG = pygame.image.load("assets/images/background/deskBG.png")
inHouse = pygame.image.load("assets/images/background/inHouse.png")
outHouse = pygame.image.load("assets/images/background/outHouse.png")
end = pygame.image.load("assets/images/background/end.png")
end_end = pygame.image.load("assets/images/background/end_end.png")
doge = pygame.image.load("assets/images/doge.png")
#Sound Effects

    #if pictureCount >= 18:

def playMusic():
    end_song = pygame.mixer.music.load("assets/music/Last_Hi.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)

def gameEnd(surface):
    done = False
    dogeX = -250#250
    dogeY = -200#200
    playMusic()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        surface.blit(end_end,(0,0))
        surface.blit(doge,(dogeX,dogeY))
        pygame.display.update()
        if dogeX <= 250:
            dogeX+=1
        else:
            dogeX+=0

        if dogeY <= 200:
            dogeY +=1
        else:
            dogeY+=0

def gameOutro(surface):
    sayWhatEnd = ""

    global pictureCount
    pictureCount = 0
    global backImage
    backImage = deskBG

    done = False
    pictureNumber = 10
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
        if pictureCount ==10:
            sayWhat = '"Oh shoot! I almost forgot! yeah... i was too busy playing this game about frogs..."'
        if pictureCount ==11:
            character1 = jimVN
            dogeX = -100
            dogeY = 500
            sayWhat ='"called... I-I-I was trying to get the br-rown frog..", Jim said quickly'
        if pictureCount == 12:
            sayWhat='"do you like apple green onion sandwiches?, Sarah asked Jim"'
        if pictureCount ==13:
            sayWhat = '"I think they are pretty tasty garden"'
        if pictureCount == 14:
            sayWhat = ""
            jimX = 10000
            girlX = 10000
            dogeX = 10000
            backImage = end
            sayWhatEnd = '"Tiens! Lets go to the park! I made some of those sandwiches!"'
        if pictureCount == 15:
            sayWhatEnd = '"Okay", Jim said'
        if pictureCount ==16:
            sayWhatEnd = 'And so, they went to the park to try some sandwiches freshness'
        if pictureCount ==17:
            sayWhatEnd = 'Jim Thought to himself,"Wow, it sure is great to be in this world!"'
        if pictureCount >= 18:
            sayWhatEnd = ""
            gameEnd(surface)

            #START ANIME SONG
            #240 661 0307
        surface.blit(backImage,(0,0))
        surface.blit(character1,(jimX,jimY))
        surface.blit(character2,(girlX,girlY))
        surface.blit(character3,(dogeX,dogeY))
        messageText(sayWhat,50,550,20,surface,255,255,255,"Roboto")
        messageText(sayWhatEnd,50,550,20,surface,0,0,0,"Roboto")
        pygame.display.update()
gameOutro(surface)