#!/usr/bin/python3
import pygame
import os
import random
from displayText import * #KYLER DO UR CREDITS
from credits import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
#images
gameBG3 = pygame.image.load("assets/images/background/stars3BG.png")
bossSceneImage = pygame.image.load("assets/images/background/boss.png")
jumbi1 = pygame.image.load("assets/images/jumbiBoss.png")
jumbi2 = pygame.image.load("assets/images/jumbiBoss1.png")

def jumbiBoss(x,y,angery,surface):
	if angery == True:
		surface.blit(jumbi2,(x,y))
	else:
		surface.blit(jumbi1,(x,y))

#boss
def bossLevel():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		screen.blit(gameBG3,(0,0))
		pygame.display.update()
bossLevel()

def bossScene():#short cutscene before actual boss fight
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				bossLevel()
				done = True
		screen.blit(bossSceneImage,(0,0))
		pygame.display.update()


    
