import sys
import pygame
from pygame.locals import *

pygame.init()
size = width, height = 800,500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("testing")
myfont = pygame.font.SysFont("monospace", 16)#first load font
WHITE = (255,255,255)
BLACK = (0,0,0)
jumbi2 = pygame.image.load("assets/images/jumbiBoss1.png")
def game():
    score = 0
    x = 30
    y = 30

    while True:
        for event in pygame.event.get():
            # I remove the timer just for my testing
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                score  +=1
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        screen.fill(WHITE)
        screen.blit(jumbi2,(0,0))

        disclaimertext = myfont.render("Some disclaimer...", 1, (0,0,0))#render text
        screen.blit(disclaimertext, (5, 480)) #blit text
        pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 60, 60))
        #scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
        scoretext = myfont.render("Score"+str(score), True, (BLACK))
        screen.blit(scoretext, (5, 10))
        #score += 1
        pygame.display.flip()

game()