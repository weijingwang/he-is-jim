import pygame
import random
from displayText import *
from gameDeath import *
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()
#screen
x = 800
y = 600

screen = pygame.display.set_mode((x,y))

black = ((0,0,0))
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
bossSceneImage = pygame.image.load("assets/images/background/boss.png")

spaceRockTypeNumber = random.randrange(0,6)
musicOption = True

#music
# pygame.mixer.music.load("assets/music/HopeForADog.mp3")
# pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1)

#sound

#objects
def jim(x,y,surface):
	surface.blit(jimPic,(x,y))#Jim

def spaceRock(x,y,rocktype,surface):
	global rockSprite
	surface.blit(rocktype,(x,y))


#load font
font = pygame.font.Font("assets/fonts/ComicSansMSRegular.ttf", 18)
def kill_count(count,surface):
	spaceRockTypeNumber = random.randrange(0,6)
	killCountText = font.render("Kills: "+str(count), True, (255, 255, 255))
	surface.blit(killCountText,(0,0))#corner text score

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
	if spaceRockSpeed <= 13:
		spaceRockSpeed += 0.8
	elif spaceRockSpeed > 10 and spaceRockSpeed <= 50:
		spaceRockSpeed += 0.5
	elif spaceRockSpeed > 50 and spaceRockSpeed <= 100:
		spaceRockSpeed += 0.37
	elif spaceRockSpeed > 100 and spaceRockSpeed <= 150:
		spaceRockSpeed += 0.35
	elif spaceRockSpeed > 150 and spaceRockSpeed <= 200:
		spaceRockSpeed += 0.12
	#randomly selects next spacerock
	spaceRockTypeNumber = random.randrange(0,6)
	#random.choice(spaceRockLetterChoices)
	findRockLetter()
	#print(spaceRockTypeNumber)
	#adds 1 to killCount score in corner of screen, see kill_count()
	killCount +=1
	spaceRockTypeNumber = random.randrange(0,6)

def game(surface):
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
	spaceRockSpeed = 9
	killCount = 0
	jumbiX = 0
	jumbiY = -1000
	backgroundCount = 0#fail
	enemyKillCount = 0#THIS IS USED FOR COUNTING ENEMIES KILLED. RANDOM ENEMIES YES? WHEN CERTAIN NUMBER OF ENEMIES KILLED, TRIGGER EVENT
	spaceRockTypeNumber = random.randrange(0,6)

	while not done:
		pygame.mixer.stop()#stop death sound
		pygame.mixer.music.unpause()#background music always unpaused but when death

		findRockLetter()
		if (spaceRockY > 600):
			print("Rock below")
			killCount -= 1 #score penalty if no kill
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

		#requirements to pass level 1
		if killCount == 35:
			pass#LOAD BOSS LEVEL

		if jimY < spaceRockY+100:
			print("y cross over")
			if jimX>spaceRockX and jimX < spaceRockX+100:
				print("ALSO X CROSS???!!!")
				print("you ded")
				pygame.mixer.music.pause()#stop music
				gameDeathSurface(surface)#death screen
				gameOverMusic.play()
				print("play sound")
				killSpaceRock()# and space rock positions
				killCount = 0 #reset score
				spaceRockSpeed = 9#speed reset	


		findRockLetter()
		#print("spaceTypeLetter: " + spaceRockLetter)

		surface.blit(gameBG3,(0,0))
		spaceRock(spaceRockX,spaceRockY,rockSprite,surface)
		spaceRockY += spaceRockSpeed

		jim(jimX,jimY,surface)
		#killCountScore('1')
		########
		kill_count(killCount,surface)

			#score + 1
		#print (killCount)
		pygame.display.update()
#game()
#spaceRockTypeNumber = random.randrange(0,6)

def jumbiBoss(x,y,angery,surface):
	if angery == True:
		screen.blit(jumbi2,(x,y))
	else:
		screen.blit(jumbi1,(x,y))

def bossScene():#short cutscene before actual boss fight
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				bossLevel()
				done = True
		screen.blit(bossSceneImage,(0,0))#background
		pygame.display.update()

#boss
def bossLevel():
	global jumbiX
	global jumbiY
	global jimX
	global jimY
	jimX = 350
	jimY = 470
	jumbiX = 200
	jumbiY = -300#slowly moves into view and when on bottom, you lose
	spaceRockX = 0
	spaceRockY = 0
	spaceRockSpeed = 9
	killCount = 0
	enemyKillCount = 0
	done = False

	while not done:
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

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT] and jimX>=0:
			jimX-=7

		if pressed[pygame.K_RIGHT] and jimX<=740:
			jimX+=7

		screen.blit(gameBG3,(0,0))#background
		jumbiBoss(jumbiX,jumbiY,False,screen)
		jim(jimX,jimY,screen)
		pygame.display.update()
#bossLevel()

