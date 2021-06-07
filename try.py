import pygame
import math
import sys
from pygame.locals import *
from pygame.time import Clock

class Planet:
    def __init__(self, x, y, vx, vy, radius, color, id):
        self.x = x
        self.y = y
        self.radius = radius
        self.id = id
        self.volume = radius ** 3
        self.mass = math.pi * (self.radius ** 2) * MASS_AREA_RATIO
        self.last_pos = (x, y)
        self.velocity = [vx, vy]
        self.color = color
        print(self.x, self.y)

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        for planet in planets:
            if self.id != planet.id:
                dx = planet.x - self.x
                dy = planet.y - self.y
                angle = math.atan2(dy, dx)  # Calculate angle between planets
                d = math.sqrt((dx ** 2) + (dy ** 2))  # Calculate distance
                if d == 0:
                    d = 0.000001  # Prevent division by zero error
                f = (
                    G * self.mass * planet.mass / (d ** 2)
                )  # Calculate gravitational force

                self.velocity[0] += (math.cos(angle) * f) / self.mass
                self.velocity[1] += (math.sin(angle) * f) / self.mass

    def draw(self):
        pygame.draw.circle(
            display, self.color, (int(self.x), int(self.y)), int(self.radius)
        )
        # pygame.draw.rect(display, (255, 255, 255), self.rect)


def draw():
    # display.fill((25, 25, 25))

    for planet in planets:
        planet.draw()
    
    screen.blit(display, (0,0))

    pygame.display.update()


pygame.init()
clock = pygame.time.Clock()

width = 1440
height = 820
WINDOW_SIZE = (width, height)
screen = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(WINDOW_SIZE)

G = 6.67408 * (10 ** -11)  # Gravitational Constant
MASS_AREA_RATIO = 2 * (10 ** 9)  # mass in kilograms to area in pixels
echelle = 1/800
earth_distance = 3.84 * (10 ** 5) * echelle
planets = []
planet_id = 0
planets.append(Planet(int(width / 2), height / 2, 0, 0, 6371 * echelle, (19, 14, 209), planet_id))
planet_id += 1
planets.append(Planet(int(width / 2 + earth_distance), height / 2, 0, 0.235, 1737 * echelle, (100, 100, 100), planet_id))
planet_id += 1

while True:
    clock.tick(480)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
    
    for planet in planets:
        planet.update()
    draw()