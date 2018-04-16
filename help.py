#!/usr/bin/python3
import pygame
import os
from displayText import *
from buttons import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()


black = ((0,0,0))



#function for menu which you can call
def helps(surface):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					done = True
		surface.fill(black)
		messageText("Help",325,30,40,surface,244,67,54,"ComicSans")
		messageText("",100,30,30,surface,244,67,54,"ComicSans")
		button("Main Menu",320,400,150,50,True,surface)
		pygame.display.update()
