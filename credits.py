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

creditsTxt = "This game was made by:\nWeijing Wang\nKyler Chin\n\n\nSpecial Thanks to:\nHana the Doge\nDogecoin Foundation\nWang Wang the regular dog\nMomo the Jumbi Cat"

#function for menu which you can call
def showCredits():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		screen.fill(black)
		messageText("Credits",325,30,40,screen,244,67,54,"ComicSans")
		messageText("Weijing Wang who draw, code, music",270,100,20,screen,255,87,34,"ComicSans")
		messageText("Kyler Chin who kool coder",300,150,30,screen,255,152,0,"ComicSans")
		messageText("Hana the Doge",300,200,20,screen,255,193,7,"ComicSans")
		messageText("Wang Wang the Regular Dog",300,250,20,screen,255,235,59,"ComicSans")
		messageText("Momo DA EVIL JUMBI",300,300,20,screen,205,220,57,"ComicSans")
		messageText("Jim the homo sapien from planet earth",300,350,20,screen,139,195,74,"ComicSans")
		messageText("Github Source",300,350,20,screen,76,175,80,"ComicSans")
		messageText("PyWeek 25",300,350,20,screen,0,150,136,"ComicSans")
		pygame.display.update()
showCredits()
