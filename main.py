import pygame
from pygame.locals import *
import random

######### SPACECHIP CLASS #########

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.image = pygame.image.load('assets\\small.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


    def update(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]:
            if self.rect.x <= 0:
                self.rect.x = 0
                return
            self.rect.x -= self.speed

        if pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]:
            if self.rect.x >= SCREEN_WIDTH - self.rect.w:
                self.rect.x = SCREEN_WIDTH - self.rect.w
            self.rect.x += self.speed

######### END SPACECHIP CLASS #########



pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 650

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
BACKGROUND = pygame.image.load('assets\\bg.png').convert()
clock = pygame.time.Clock()
clock.tick(30)

running = True
spaceship = Spaceship(200,550,1)
ship = pygame.sprite.Group()
ship.add(spaceship)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("GOODBYE!")
            running = False

    screen.blit(BACKGROUND, (0, 0))
    ship.update()
    ship.draw(screen)

    pygame.display.flip()

pygame.quit()

