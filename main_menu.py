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
#music
pygame.mixer.music.load("assets/music/SadBoySong.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#screen
pygame.display.set_caption("Jim's Big Win")
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))

gameIcon = pygame.image.load("assets/images/icon.png")#game icon
pygame.display.set_icon(gameIcon)
#clock = pygame.time.Clock()
menu_back = pygame.image.load("assets/images/background/mainMenuBG.png")


#function for menu which you can call
def main_menu():
	print ("open main menu")
	done = False
	mainCount = 0
	while not done:
		#clock.tick(10)
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
		#messageText("Jim's Big Win",450,500,50,screen,255,255,255,"Roboto")

		#Draw "Press Up and Down to move selection"
		#messageText("Press Up and Down to move selection",30,470,15,screen,255,255,255,"ComicSans")
		# messageText("Press",30,470,15,screen,244,67,54,"ComicSans")
		# messageText("Up",71,470,15,screen,255,87,34,"ComicSans")
		# messageText("and",95,470,15,screen,255,152,0,"ComicSans")
		# messageText("Down",123,470,15,screen,255,193,7,"ComicSans")
		# messageText("to",165,470,15,screen,255,235,59,"ComicSans")
		# messageText("move",183,470,15,screen,76,175,80,"ComicSans")
		# messageText("select",220,470,15,screen,0,150,136,"ComicSans")
		# messageText("tion",255,470,15,screen,0,188,212,"ComicSans")
		#messageText("Press Enter to Select",30,490,15,screen,255,255,255,"ComicSans")
		# messageText("Press",30,490,15,screen,3,169,244,"ComicSans")
		# messageText("En",70,490,15,screen,33,150,243,"ComicSans")
		# messageText("ter",87,490,15,screen,63,81,181,"ComicSans")
		# messageText("to",115,490,15,screen,103,58,183,"ComicSans")
		# messageText("Se",135,490,15,screen,156,39,176,"ComicSans")
		# messageText("lect",155,490,15,screen,233,30,99,"ComicSans")

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
