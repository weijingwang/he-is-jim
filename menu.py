#!/usr/bin/python3
import pygame
import os
from displayText import * #KYLER DO UR CREDITS
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
def main_menu():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		screen.fill(black)
		messageText("Jim",100,100,100,screen,255,255,255)
		pygame.display.update()
main_menu()
