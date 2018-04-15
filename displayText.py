import pygame
import os
pygame.init()
def messageText(text,x,y,size,surface,red,green,blue,font):
	# os.getcwd()
	# os.chdir("roboto")
	# fontPath = os.path.dirname(os.path.abspath("Roboto-Regular.ttf"))
	# print (fontPath)

	myFont = pygame.font.Font(font, size)


	label = myFont.render(text, 1, (red, green, blue))
	    
	surface.blit(label, (x, y))
	        
	pygame.display.flip()
 
 #how to use
 #messageText("bob ate a dog",x,y,size,what surface,redlevel,greenlevel,bluelevel)




