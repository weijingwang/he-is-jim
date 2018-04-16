#!/usr/bin/python3
import pygame
import os
from displayText import * #KYLER DO UR CREDITS
from buttons import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#surface


creditsTxt = "This game was made by:\nWeijing Wang\nKyler Chin\n\n\nSpecial Thanks to:\nHana the Doge\nDogecoin Foundation\nWang Wang the regular dog\nMomo the Jumbi Cat"
creditsBack = pygame.image.load("assets/images/the-pygameMAN.png")

#function for menu which you can call
def showCredits(surface):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					done= True
		surface.blit(creditsBack,(0,0))

		messageText("Credits",325,30,40,surface,244,67,54,"ComicSans")
		messageText("Weijing Wang",270,100,40,surface,255,87,34,"ComicSans")
		messageText("Kyler Chin",300,150,40,surface,255,152,0,"ComicSans")
		messageText("Hana the Doge",320,200,20,surface,255,193,7,"ComicSans")
		messageText("Wang Wang the Regular Dog",250,230,20,surface,255,235,59,"ComicSans")
		messageText("Momo DA EVIL JUMBI",270,260,20,surface,205,220,57,"ComicSans")
		messageText("Jim the homo sapien from planet earth",200,290,20,surface,139,195,74,"ComicSans")
		messageText("Github Source",320,320,20,surface,76,175,80,"ComicSans")
		messageText("PyWeek 25",330,350,20,surface,0,150,136,"ComicSans")

		kylerButton("Main Menu",320,400,150,50,True,surface,"Roboto",40)

		pygame.display.update()
