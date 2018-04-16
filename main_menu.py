#!/usr/bin/python3
import pygame
import os
from displayText import *
from buttons import *
#main menu links
from credits import *
from options import *
from help import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
#font
menu_back = pygame.image.load("assets/images/main-menu-bkgd.png")


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

			#enter

				if event.key == pygame.K_RETURN:
					if mainCount == 0:#start
						#import the game
						pass
					elif mainCount == 1:#Options
						#import the Options
						options(screen)
					elif mainCount == 2:#help
						#import the help
						helps(screen)
					elif mainCount == 3:
						#credits
						showCredits(screen)
					elif mainCount ==4:
						quit()

#Start
#Options
#Help
#Credits
#Quit

		screen.blit(menu_back,(0,0))
		#messageText("Jim's Big Win",450,500,50,screen,255,255,255,"/Users/weijingwang/Documents/GitHub/he-is-jim\ local/assets/fonts/ComicSansMSRegular.ttf")#/assets/fonts/ComicSansMSRegular.ttf
		messageText("Jim's Big Win",450,500,50,screen,255,255,255,"Roboto")

		#Draw "Press Up and Down to move selection"
		messageText("Press Up and Down to move selection",30,470,15,screen,255,255,255,"ComicSans")
		messageText("Press",30,470,15,screen,244,67,54,"ComicSans")
		messageText("Up",71,470,15,screen,255,87,34,"ComicSans")
		messageText("and",95,470,15,screen,255,152,0,"ComicSans")
		messageText("Down",123,470,15,screen,255,193,7,"ComicSans")
		messageText("Press Enter to select",30,490,15,screen,255,255,255,"ComicSans")

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
