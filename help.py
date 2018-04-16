#!/usr/bin/python3
import pygame
import os
from displayText import * 
from buttons import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
#font

#function for menu which you can call
def showCredits():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		screen.fill(black)
		messageText("Help",325,30,40,screen,244,67,54,"ComicSans")

		pygame.display.update()
showCredits()
