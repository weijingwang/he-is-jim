from pygame import *

def fadetoWhite(surface):
    DONE = False
    alphaSurface = Surface((1024,768)) # The custom-surface of the size of the surface.
    alphaSurface.fill((255,255,255)) # Fill it with whole white before the main-loop.
    alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop. 
    alph = 0 # The increment-variable.
    while not DONE:
        surface.fill((0,0,0)) # At each main-loop fill the whole surface with black.
        alph +=10 # Increment alpha by a really small value (To make it slower, try 0.01)
        alphaSurface.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
        surface.blit(alphaSurface,(0,0)) # Blit it to the surface-surface (Make them separate)

        for ev in event.get():
            if ev.type == QUIT:
                DONE = True
        display.flip() # Flip the whole surface at each frame.
    quit()