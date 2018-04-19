import pygame
import random
from displayText import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600
black = ((0,0,0))
screen = pygame.display.set_mode((x,y))
gameBG1 = pygame.image.load("assets/images/background/stars1BG.png")
gameBG2 = pygame.image.load("assets/images/background/stars2BG.png")
gameBG3 = pygame.image.load("assets/images/background/stars3BG.png")
gameBG4 = pygame.image.load("assets/images/background/stars4BG.png")
jimPic = pygame.image.load("assets/images/jim.png")
ARock = pygame.image.load("assets/images/ARock.png")
BRock = pygame.image.load("assets/images/BRock.png")
CRock = pygame.image.load("assets/images/CRock.png")
ORock = pygame.image.load("assets/images/ORock.png")
HRock = pygame.image.load("assets/images/HRock.png")
jumbi1 = pygame.image.load("assets/images/jumbiBoss.png")
jumbi2 = pygame.image.load("assets/images/jumbiBoss1.png")

#music
pygame.mixer.music.load("assets/music/HopeForADog.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#objects
def jim(x,y):
	screen.blit(jimPic,(x,y))#Jim

def spaceRock(x,y,type):
	rockSprite = "what rock?"
	if type == "A":
		rockSprite = ARock
	elif type == "B":
		rockSprite = BRock
	elif type == "C":
		rockSprite = CRock
	elif type == "O":
		rockSprite = ORock
	elif type == "H":
		rockSprite = HRock

	screen.blit(rockSprite,(x,y))


def jumbiBoss(x,y,angery):
	if angery == True:
		screen.blit(jumbi2,(x,y))
	else:
		screen.blit(jumbi1,(x,y))

def kill_count(count):
	font = pygame.font.Font("assets/fonts/Roboto-Regular.ttf", 18)
	killCountText = font.render("Kills: "+str(count), True, (255, 255, 255))
	screen.blit(killCountText,(0,0))#corner text score
	pygame.display.update()

def game():
	done = False
	jimX = 350
	jimY = 470
	spaceRockX = 0
	spaceRockY = 0
	spaceRockSpeed = 8
	killCount = 0
	jumbiX = 0
	jumbiY = -1000
	backgroundCount = 0#fail
	enemyKillCount = 0#THIS IS USED FOR COUNTING ENEMIES KILLED. RANDOM ENEMIES YES? WHEN CERTAIN NUMBER OF ENEMIES KILLED, TRIGGER EVENT
	spaceRockTypeNumber = random.randrange(0,4)
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a and spaceRockLetter == "A":
					print ("a")
					spaceRockX = random.randrange(0,700)
					spaceRockY = -200
					spaceRockSpeed += 1
					spaceRockTypeNumber = random.randrange(0,4)
					killCount +=1
				elif event.key == pygame.K_b and spaceRockLetter == "B":
					print ("b")
					spaceRockX = random.randrange(0,700)
					spaceRockY = -200
					spaceRockSpeed += 1
					spaceRockTypeNumber = random.randrange(0,4)
					killCount +=1
				elif event.key == pygame.K_c and spaceRockLetter == "C":
					print ("c")
					spaceRockX = random.randrange(0,700)
					spaceRockY = -200
					spaceRockSpeed += 1
					spaceRockTypeNumber = random.randrange(0,4)
					killCount +=1
				elif event.key == pygame.K_o and spaceRockLetter == "O":
					print("o")
					spaceRockX = random.randrange(0,700)
					spaceRockY = -200
					spaceRockSpeed += 1
					spaceRockTypeNumber = random.randrange(0,4)
					killCount +=1
				elif event.key == pygame.K_h and spaceRockLetter == "H":
					print("h")
					spaceRockX = random.randrange(0,700)
					spaceRockY = -200
					spaceRockSpeed += 1
					spaceRockTypeNumber = random.randrange(0,4)
					killCount +=1

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

		spaceRockLetter = "A"
		if spaceRockTypeNumber == 0:
			spaceRockLetter = "A"
		elif spaceRockTypeNumber == 1:
			spaceRockLetter = "B"
		elif spaceRockTypeNumber == 2:
			spaceRockLetter = "C"
		elif spaceRockTypeNumber == 3:
			spaceRockLetter = "O"
		elif spaceRockTypeNumber == 4:
			spaceRockLetter = "H"

		screen.blit(gameBG3,(0,0))
		spaceRock(spaceRockX,spaceRockY,spaceRockLetter)
		spaceRockY +=spaceRockSpeed

		jim(jimX,jimY)
		#killCountScore('1')
		########
		kill_count(killCount)
		if spaceRockY>600:
			spaceRockTypeNumber = random.randrange(0,4)
			spaceRockY = 0 - 100
			spaceRockX = random.randrange(0,700)
			spaceRockSpeed += 1
			spaceRockTypeNumber = random.randrange(0,4)
			#score + 1
		jumbiBoss(jumbiX,jumbiY,False)
		print (killCount)
		pygame.display.update()
game()
