import pygame
from pygame.locals import *
import math

class Planet:
    def __init__(self):
        self.masse = 5.972 * (10 ** 24)
        self.rayon = 6
        self.x = 200
        self.y = 200
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), self.rayon)
        pygame.display.flip()
        

pygame.init()
running = True
screen = pygame.display.set_mode((1800, 900), RESIZABLE)
Terre = Planet()

while running:
    for event in pygame.event.get():
             
            if event.type==KEYDOWN:   #appui sur une touche
 
                if event.key==K_ESCAPE:
                    running=False

pygame.quit()