
import pygame
from displayText import * #KYLER DO UR CREDITS
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
gameBG1 = pygame.image.load("assets/images/stars1BG.png")
gameBG2 = pygame.image.load("assets/images/stars2BG.png")
gameBG3 = pygame.image.load("assets/images/stars3BG.png")
gameBG4 = pygame.image.load("assets/images/stars4BG.png")
jimPic = pygame.image.load("assets/images/jim.png")
ARock = pygame.image.load("assets/images/ARock.png")
BRock = pygame.image.load("assets/images/BRock.png")
CRock = pygame.image.load("assets/images/CRock.png")
ORock = pygame.image.load("assets/images/ORock.png")
HRock = pygame.image.load("assets/images/HRock.png")
jumbi1 = pygame.image.load("assets/images/jumbiBoss.png")
jumbi2 = pygame.image.load("assets/images/jumbiBoss1.png")



#objects
def jim(x,y):
	screen.blit(jimPic,(x,y))#Jim

def RockA(x,y):
	screen.blit(ARock,(x,y))

def RockB(x,y):
	screen.blit(BRock,(x,y))

def RockC(x,y):
	screen.blit(CRock,(x,y))

def RockO(x,y):
	screen.blit(ORock,(x,y))

def RockH(x,y):
	screen.blit(HRock,(x,y))

def jumbiBoss(x,y,angery):
	if angery == True:
		screen.blit(jumbi2,(x,y))
	else:
		screen.blit(jumbi1,(x,y))



def game():
	done = False
	jimX = 350
	jimY = 470
	backgroundCount = 0#fail
	enemyKillCount = 0#THIS IS USED FOR COUNTING ENEMIES KILLED. RANDOM ENEMIES YES? WHEN CERTAIN NUMBER OF ENEMIES KILLED, TRIGGER EVENT

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				pass
		# if backgroundCount == 0:
		# 	backImage = gameBG1
		# 	print(backgroundCount)
		# elif backgroundCount == 1:
		# 	backImage = gameBG2
		# 	print(backgroundCount)
		# elif backgroundCount == 2:
		# 	backImage = gameBG3
		# 	print(backgroundCount)
		# elif backgroundCount == 3:
		# 	backImage = gameBG4
		# 	print(backgroundCount)
		# elif backgroundCount == -1:
		# 	backgroundCount =3
		# 	print(backgroundCount)
		# elif backgroundCount == 4:
		# 	backgroundCount=0
		# 	print(backgroundCount)


		#controls for jim
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT] and jimX>=0:
			jimX-=7
			backgroundCount-=1
		if pressed[pygame.K_RIGHT] and jimX<=740:
			jimX+=7
			backgroundCount+=1

		screen.blit(gameBG3,(0,0))
		jim(jimX,jimY)
		RockA(0,0)
		RockB(100,100)
		RockC(200,200)
		RockO(300,300)
		RockH(400,400)
		jumbiBoss(500,400,True)
		jumbiBoss(500,200,False)
		pygame.display.update()
game()
