import pygame
import time
from math import *
from pygame.locals import *


class Preview:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rectx = 0
        self.recty = 0
        self.force = 1 * (10 ** 5)
        self.alpha = 60
        self.dt = 0.1
        self.t = 0
        self.m = 90
        self.g = 9.8
        self.p = self.m * self.g
        self.vx = cos(radians(self.alpha)) * self.force / self.p
        self.vy = sin(radians(self.alpha)) * self.force / self.p

    def new_coo(self):
        if self.y >= 0:
            self.t += self.dt
            self.calcul_vitesse()
            self.x += round(self.vx * self.dt, 2)
            self.y += round(self.vy * self.dt, 2)
            if self.y < self.recty:
                pygame.draw.arc(screen, (255, 255, 255), (0, 0, self.rectx * 2, self.recty), 0, 3.14)
            else:
                self.rectx, self.recty = self.x, self.y
                self.new_coo()
        else:
            self.y = 0
            self.vx, self.vy = 0, 0
        pygame.display.flip()

    def calcul_vitesse(self):
        if self.y > 0:
            self.vy += self.g * -1/2

    def refresh(self):
        screen.fill((0, 0, 0))
        self.new_coo()


class Rocket:
    def __init__(self):
        self.x0, self.y0 = 0, 0
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0
        self.rocket_rect = pygame.Rect(0, 0, 16, 24)

    def draw(self):
        self.x0, self.y0 = preview.x + sin(radians(preview.alpha)) * 8 - cos(radians(preview.alpha)) * 8, preview.y + cos(radians(preview.alpha)) * 8 - (sin(radians(preview.alpha)) * 8)
        print(preview.x, preview.y)
        print(self.x0, self.y0)
        self.x1, self.y1 = preview.x - (sin(radians(preview.alpha)) * 8) - cos(radians(preview.alpha)) * 8, preview.y - (cos(radians(preview.alpha)) * 8) + sin(radians(preview.alpha)) * 8
        print(self.x1, self.y1)
        self.x2, self.y2 = preview.x + cos(radians(preview.alpha)) * 16, preview.y + sin(radians(preview.alpha)) * 16
        print(self.x2, self.y2)
        triangle = pygame.draw.polygon(screen, (255, 255, 255), ((self.x0, self.y0), (self.x1, self.y1), (self.x2, self.y2)))
        pygame.display.update(triangle, self.rocket_rect)


pygame.init()

running = True
pygame.key.set_repeat(250, 100)


screen = pygame.display.set_mode((1200, 600), RESIZABLE)
preview = Preview()
rocket = Rocket()
preview.refresh()
rocket.draw()

while running:
    for event in pygame.event.get():

            if event.type==QUIT: #la croix en haut à gauche
                running=False

            elif event.type==KEYDOWN:   #appui sur une touche

                if event.key==K_ESCAPE:
                    running=False

                elif event.key == K_SPACE:
                    preview.vx += cos(radians(preview.alpha)) * 10
                    preview.vy += sin(radians(preview.alpha)) * 10

                elif event.key == K_UP:
                    preview.alpha += 1

                elif event.key == K_DOWN:
                    preview.alpha -= 1
    time.sleep(0.1)


pygame.quit()