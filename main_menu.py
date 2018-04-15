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
menu_back = pygame.image.load("assets/images/main-menu-back.png")


#function for menu which you can call
def main_menu():
	print ("main menu")
	done = False
	mainCount = 0
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:

					mainCount = mainCount-1
					print (mainCount)

				if mainCount == -1:
					mainCount = 4
					print (mainCount)
				if event.key == pygame.K_DOWN:

					mainCount = mainCount +1

					print (mainCount)

				if mainCount == 5:
					mainCount = 0
					print (mainCount)
#Start
#Options
#Help
#Credits
#Quit

		screen.blit(menu_back,(0,0))
		#messageText("Jim's Big Win",450,500,50,screen,255,255,255,"/Users/weijingwang/Documents/GitHub/he-is-jim\ local/assets/fonts/ComicSansMSRegular.ttf")#/assets/fonts/ComicSansMSRegular.ttf
		messageText("Jim's Big Win",450,500,50,screen,255,255,255,"Roboto")

		button("Start",0,50,200,50,False,screen)
		button("Options",0,100,200,50,False,screen)
		button("Help",0,150,200,50,False,screen)
		button("Credits",0,200,200,50,False,screen)
		button("Quit",0,250,200,50,False,screen)

		if mainCount == 0:
			button("Start",0,50,200,50,True,screen)
		elif mainCount == 1:
			button("Options",0,100,200,50,True,screen)
		elif mainCount ==2:
			button("Help",0,150,200,50,True,screen)
		elif mainCount ==3:
			button("Credits",0,200,200,50,True,screen)
		elif mainCount == 4:
			button("Quit",0,250,200,50,True,screen)
		else:
			print (mainCount)
		pygame.display.update()

main_menu()
