import pygame
import math
import time
from pygame.locals import *

class Earth:
    def __init__(self):
        self.mass = 6 * (10 ** 24)
        self.radius = 6371
        self.x = int(width / 2)
        self.y = int(height / 2)
        self.vx = 0
        self.vy = 0
        self.vecteur_directeur = 0
        self.gravity_y = 0
        self.gravity_x = 0
        self.g = 0
        

    def draw(self):
        pygame.draw.circle(screen, (19, 14, 209), (self.x, self.y), int(self.radius * echelle))

    def calcul_vitesse(self):
        self.gravity_x = self.g * self.vecteur_directeur[0] / (self.vecteur_directeur[0] + self.vecteur_directeur[1]) / self.mass * echelle
        self.gravity_y = self.g * self.vecteur_directeur[1] / (self.vecteur_directeur[0] + self.vecteur_directeur[1]) / self.mass * echelle
        self.x += self.gravity_x
        self.y += self.gravity_y
        pygame.draw.circle(screen, (19, 14, 209), (int(self.x), int(self.y)), int(self.radius * echelle))


class Moon:
    def __init__(self):
        self.mass = 7.3 * (10 ** 22)
        self.radius = 1737
        self.earth_distance = 3.84 * (10 ** 5)
        self.g = 0
        self.x = int(earth.x + self.earth_distance * echelle)
        self.y = int(earth.y)
        self.vx = 0
        self.vy = 0
        self.vitesse = 3672
        self.vecteur_directeur = 0
        self.gravity_x = 0
        self.gravity_y = 0
        self.velocity_x = 0
        self.velocity_y = 0
    
    def set_up(self):
        self.g = G * ((earth.mass * self.mass) / ((self.earth_distance * (10 ** 3)) ** 2)) * echelle
        earth.g = self.g
        pygame.draw.circle(screen, (100, 100, 100), (self.x, self.y), int(self.radius * echelle))

    def calcul_vitesse(self):
        self.vecteur_directeur = (earth.x - self.x, earth.y - self.y)
        self.earth_distance = math.sqrt(self.vecteur_directeur[0] ** 2 + self.vecteur_directeur[1] ** 2)
        earth.vecteur_directeur = self.vecteur_directeur
        self.g = G * ((earth.mass * self.mass) / (self.earth_distance * (10 ** 3) ** 2)) * echelle
        earth.g = self.g
        self.gravity_x = -(self.g * self.vecteur_directeur[0] / (self.vecteur_directeur[0] + self.vecteur_directeur[1]) / self.mass * echelle)
        self.gravity_y = -(self.g * self.vecteur_directeur[1] / (self.vecteur_directeur[0] + self.vecteur_directeur[1]) / self.mass * echelle)
        self.velocity_x = self.vitesse * ((self.vecteur_directeur[0] - self.vecteur_directeur[0] + self.vecteur_directeur[1]) / (self.vecteur_directeur[0] + self.vecteur_directeur[1])) * echelle
        self.velocity_y = self.vitesse * ((self.vecteur_directeur[1] - self.vecteur_directeur[1] + self.vecteur_directeur[0]) / (self.vecteur_directeur[0] + self.vecteur_directeur[1])) * echelle
        print(self.velocity_x, self.velocity_y)
        self.x += self.gravity_x
        self.y += self.gravity_y
        pygame.draw.circle(screen, (100, 100, 100), (int(self.x), int(self.y)), int(self.radius * echelle))


echelle = 1 / 700
G = 6.67408 * (10 ** -11)  # Gravitational Constant
running = True
width = 1440
height = 900

pygame.init()

screen = pygame.display.set_mode((width, height), RESIZABLE)

earth = Earth()
moon = Moon()
moon.set_up()

while running:
    screen.fill((0, 0, 0))
    moon.calcul_vitesse()
    earth.calcul_vitesse()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    time.sleep(0.01)

pygame.quit()