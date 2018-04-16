#!/usr/bin/python3
import pygame
pygame.init()

dogeGreen = ((0,150,136))
darkdogeGreen = ((0,100,100))
green = ((0,255,0))
darkgreen = ((0,100,0))
white = ((255,255,255))
black = ((0,0,0))
gold = ((212,175,55))
buttonFont = pygame.font.Font("assets/fonts/Roboto-Regular.ttf", 25)
def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def button(text,x,y,width,height,active,surface):
	if active == True:
		active = white
	else:
		active = gold

	textSurf, textRect = text_objects(text, buttonFont,active)
	textRect.center = ((x+(width/2)),(y+(height/2)))
	#pygame.draw.rect(surface, active, pygame.Rect(x,y,width,height))
	surface.blit(textSurf,textRect)

def kylerButton(text,x,y,width,height,active,surface,fontFamily,fontSize):
	if active == True:
		active = white
	else:
		active = gold

	if (fontFamily == "ComicSans"):
		fontFamilyButton = "assets/fonts/ComicSansMSRegular.ttf"

	elif (fontFamily == "Roboto"):
		fontFamilyButton = "assets/fonts/Roboto-Regular.ttf"
	buttonFont = pygame.font.Font(fontFamilyButton, fontSize)
	textSurf, textRect = text_objects(text, buttonFont,active)
	textRect.center = ((x+(width/2)),(y+(height/2)))
	#pygame.draw.rect(surface, active, pygame.Rect(x,y,width,height))
	surface.blit(textSurf,textRect)

def dogeButton(text,x,y,width,height,active,surface):
	if active == True:
		active = dogeGreen
	else:
		active = darkdogeGreen

	textSurf, textRect = text_objects(text, buttonFont,active)
	textRect.center = ((x+(width/2)),(y+(height/2)))
	#pygame.draw.rect(surface, active, pygame.Rect(x,y,width,height))
	surface.blit(textSurf,textRect)


