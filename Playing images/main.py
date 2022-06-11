from pygame import mixer
import pygame
import os, sys

gameover = False

image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'spaceship (5).png')), (128, 128))
image_rect = image.get_rect()

Clock = pygame.time.Clock()
win = pygame.display.set_mode((800, 800))
dx = 250
dy = 250


while not gameover:
    win.fill((0, 50, 0))
    keys = pygame.key.get_pressed()
    Clock.tick(60)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_a]:
          dx += -5
        if keys[pygame.K_d]:
          dx += 5
        if keys[pygame.K_s]:
          dy += 5
        if keys[pygame.K_w]:
          dy += -5


    win.blit(image, (dx, dy))
    pygame.display.update()
