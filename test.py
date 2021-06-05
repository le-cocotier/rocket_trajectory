import pygame
import time
from math import *
from pygame.locals import *


class Preview:
  def __init__(self):
    self.x = 8
    self.y = 8
    self.alpha = 90
    self.masse = 220000
    self.dt = 0.05
    self.t = 0
    self.g = 9.8
    self.vx = 0
    self.vy = 0

  def new_coo(self):
    if self.y >= 8:
      self.t += self.dt
      self.calcul_vitesse()
      self.x += round(self.vx * self.dt, 2)
      self.y += round(self.vy * self.dt, 2)
    else:
      self.y = 8
      self.vx, self.vy = 0, 0
    
    pygame.display.flip()

  def calcul_vitesse(self):
    if self.y > 8:
      self.vy += self.g * -1/2

  def refresh(self):
      screen.fill((0, 0, 0))
      self.new_coo()


class Rocket:
    def __init__(self):
        self.x0, self.y0 = 0, 0
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0

    def draw(self):
        screen.fill((0, 0, 0))
        self.x0, self.y0 = preview.x + sin(radians(preview.alpha)) * 8 - cos(radians(preview.alpha)) * 8, preview.y - cos(radians(preview.alpha)) * 8 - (sin(radians(preview.alpha)) * 8)
        self.x1, self.y1 = preview.x - (sin(radians(preview.alpha)) * 8) - cos(radians(preview.alpha)) * 8, preview.y + (cos(radians(preview.alpha)) * 8) - sin(radians(preview.alpha)) * 8
        self.x2, self.y2 = preview.x + cos(radians(preview.alpha)) * 16, preview.y + sin(radians(preview.alpha)) * 16
        pygame.draw.polygon(screen, (255, 255, 255), ((self.x0, self.y0), (self.x1, self.y1), (self.x2, self.y2)))


pygame.init()

running = True
pygame.key.set_repeat(250, 100)


screen = pygame.display.set_mode((1200, 600), RESIZABLE)
preview = Preview()
rocket = Rocket()
preview.refresh()
rocket.draw()

while running:
  preview.new_coo()
  rocket.draw()
  for event in pygame.event.get():
    if event.type==QUIT: #la croix en haut à gauche
      running=False

    elif event.type==KEYDOWN:   #appui sur une touche

      if event.key==K_ESCAPE:
        running=False

      if event.key == K_SPACE:
        preview.vx += cos(radians(preview.alpha)) * 20
        preview.vy += sin(radians(preview.alpha)) * 20

      if event.key == K_UP:
        preview.alpha += 5

      if event.key == K_DOWN:
        preview.alpha -= 5
  print(preview.alpha)
  time.sleep(0.05)


pygame.quit()