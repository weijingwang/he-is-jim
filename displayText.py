import pygame
import os
from credits import *
pygame.init()
def messageText(text,x,y,size,surface,red,green,blue,chooseFont,weight):
	# os.getcwd()
	# os.chdir("roboto")
	# fontPath = os.path.dirname(os.path.abspath("Roboto-Regular.ttf"))
	# print (fontPath)

 if (chooseFont == "ComicSans"):
	 myFont = pygame.font.Font("assets/fonts/ComicSansMSRegular.ttf", size)
if (chooseFont == "Roboto"):
	myFont = pygame.font.Font("assets/fonts/Roboto-Regular.ttf", size)


	label = myFont.render(text, 1, (red, green, blue))

	surface.blit(label, (x, y))

	pygame.display.flip()

 #how to use
 #messageText("Text to display",x,y,size,what surface,redlevel,greenlevel,bluelevel)
