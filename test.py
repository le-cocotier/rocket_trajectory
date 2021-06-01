import pygame
import time
from math import *
from pygame.locals import *


class Spacecraft:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.force = 1 * (10 ** 5)
        self.alpha = 60
        self.dt = 0.1
        self.t = 0
        self.m = 90
        self.g = 9.8
        self.p = self.m * self.g
        self.vx = cos(radians(self.alpha)) * self.force / self.p
        self.vy = sin(radians(self.alpha)) * self.force / self.p
        self.is_fly = False

    def new_coo(self):
        self.t += self.dt
        preview.calcul_vitesse()
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt
        pygame.draw.rect(screen, (255, 255, 255),(self.x, self.y, 2, 2))
        pygame.display.flip()
        if self.y >= 0:
            self.is_fly = True
        else:
            self.is_fly = False

    def calcul_vitesse(self):
        self.vy += self.t ** 2 * self.g * -1/2

    def acceleration(self, value):
        self.vx += cos(radians(self.alpha)) * value
        self.vy += sin(radians(self.alpha)) * value
        print(cos(radians(self.alpha)) * value, sin(radians(self.alpha)) * value)

    def refresh(self):
        screen.fill((0, 0, 0))
        self.new_coo()


pygame.init()

running = True
pygame.key.set_repeat(250, 100)


screen = pygame.display.set_mode((1200, 600), RESIZABLE)
preview = Spacecraft()
preview.refresh()

while running:
    if preview.is_fly:
        preview.new_coo()
    for event in pygame.event.get():
             
            if event.type==QUIT: #la croix en haut à gauche
                running=False
                 
            elif event.type==KEYDOWN:   #appui sur une touche
 
                if event.key==K_ESCAPE:
                    running=False

                elif event.key == K_SPACE:
                    preview.acceleration(100)
                    print('hello')
                     
                elif event.key==K_UP:
                    preview.alpha += 1
                     
                elif event.key==K_DOWN:
                    preview.alpha -= 1
    time.sleep(0.1)


pygame.quit()