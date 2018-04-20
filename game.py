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
ARock = pygame.image.load("assets/images/rocks/ARock.png")
BRock = pygame.image.load("assets/images/rocks/BRock.png")
CRock = pygame.image.load("assets/images/rocks/CRock.png")
ORock = pygame.image.load("assets/images/rocks/ORock.png")
HRock = pygame.image.load("assets/images/rocks/HRock.png")
DRock = pygame.image.load("assets/images/rocks/DRock.png")
jumbi1 = pygame.image.load("assets/images/jumbiBoss.png")
jumbi2 = pygame.image.load("assets/images/jumbiBoss1.png")
spaceRockTypeNumber = random.randrange(0,6)

#music
pygame.mixer.music.load("assets/music/HopeForADog.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#objects
def jim(x,y):
	screen.blit(jimPic,(x,y))#Jim

def spaceRock(x,y,rocktype):
	global rockSprite
	screen.blit(rocktype,(x,y))

def jumbiBoss(x,y,angery):
	if angery == True:
		screen.blit(jumbi2,(x,y))
	else:
		screen.blit(jumbi1,(x,y))

def kill_count(count):
	spaceRockTypeNumber = random.randrange(0,6)
	font = pygame.font.Font("assets/fonts/ComicSansMSRegular.ttf", 18)
	killCountText = font.render("Kills: "+str(count), True, (255, 255, 255))
	screen.blit(killCountText,(0,0))#corner text score
	pygame.display.update()

def findRockLetter():
	global spaceRockTypeNumber
	global rockSprite
	global spaceRockLetter
	global spaceRockTy
	spaceRockLetter = None
	if (spaceRockY > 600):
		print("Rock below")
		spaceRockTypeNumber = random.randrange(0,6)
		print(spaceRockTypeNumber)
	print(spaceRockTypeNumber)
	if spaceRockTypeNumber == 0:
		spaceRockLetter = "A"
		rockSprite = ARock
	elif spaceRockTypeNumber == 1:
		spaceRockLetter = "B"
		rockSprite = BRock
	elif spaceRockTypeNumber == 2:
		spaceRockLetter = "C"
		rockSprite = CRock
	elif spaceRockTypeNumber == 3:
		spaceRockLetter = "O"
		rockSprite = ORock
	elif spaceRockTypeNumber == 4:
		spaceRockLetter = "H"
		rockSprite = HRock
	elif spaceRockTypeNumber == 5:
		spaceRockLetter = "D"
		rockSprite = DRock
	#print (spaceRockLetter)
	#print(rockSprite)

#killSpaceRock() is executed when a player correctly pushes a key
def killSpaceRock():
	global spaceRockX
	global spaceRockY
	global spaceRockSpeed
	global spaceRockTypeNumber
	global killCount

	#random choose next rock location
	spaceRockX = random.randrange(0,700)
	spaceRockY = -200
	#increase spaceRockSpeed over time per button pressed, algorithm acceleration slower over time
	if spaceRockSpeed <= 10:
		spaceRockSpeed += 0.5
	elif spaceRockSpeed > 10 and spaceRockSpeed <= 50:
		spaceRockSpeed += 0.1
	elif spaceRockSpeed > 50 and spaceRockSpeed <= 100:
		spaceRockSpeed += 0.07
	elif spaceRockSpeed > 100 and spaceRockSpeed <= 150:
		spaceRockSpeed += 0.05
	elif spaceRockSpeed > 150 and spaceRockSpeed <= 200:
		spaceRockSpeed += 0.02
	#randomly selects next spacerock
	spaceRockTypeNumber = random.randrange(0,6)
	#random.choice(spaceRockLetterChoices)
	findRockLetter()
	#print(spaceRockTypeNumber)
	#adds 1 to killCount score in corner of screen, see kill_count()
	killCount +=1
	spaceRockTypeNumber = random.randrange(0,6)

def game():
	global jimX
	global jimY
	global spaceRockX
	global spaceRockY
	global spaceRockSpeed
	global killCount
	global jumbiX
	global jumbiY
	global backgroundCount
	global enemyKillCount
	global spaceRockNumber
	global rockSprite

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
	spaceRockTypeNumber = random.randrange(0,6)

	while not done:
		findRockLetter()
		if (spaceRockY > 600):
			print("Rock below")
			spaceRockY = 0 - 100
			spaceRockX = random.randrange(0,700)
			spaceRockSpeed += 1
			spaceRockTypeNumber = random.randrange(0,6)
			print(spaceRockTypeNumber)
			findRockLetter()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a and spaceRockLetter == "A":
					print ("a pressed")
					killSpaceRock()
				elif event.key == pygame.K_b and spaceRockLetter == "B":
					print ("b pressed")
					killSpaceRock()
				elif event.key == pygame.K_c and spaceRockLetter == "C":
					print ("c pressed")
					killSpaceRock()
				elif event.key == pygame.K_o and spaceRockLetter == "O":
					print("o pressed")
					killSpaceRock()
				elif event.key == pygame.K_h and spaceRockLetter == "H":
					print("h pressed")
					killSpaceRock()
				elif event.key == pygame.K_d and spaceRockLetter == "D":
					print("D pressed")
					killSpaceRock()

		#controls for jim
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT] and jimX>=0:
			jimX-=7
			backgroundCount-=1
		if pressed[pygame.K_RIGHT] and jimX<=740:
			jimX+=7
			backgroundCount+=1

		findRockLetter()
		#print("spaceTypeLetter: " + spaceRockLetter)

		screen.blit(gameBG3,(0,0))
		spaceRock(spaceRockX,spaceRockY,rockSprite)
		spaceRockY += spaceRockSpeed

		jim(jimX,jimY)
		#killCountScore('1')
		########
		kill_count(killCount)

			#score + 1
		jumbiBoss(jumbiX,jumbiY,False)
		#print (killCount)
		pygame.display.update()
game()
#spaceRockTypeNumber = random.randrange(0,6)
