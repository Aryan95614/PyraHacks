import pygame, os, sys

# code you have to write, its just making game loop
win = pygame.display.set_mode((512, 512))

gameover = False

image = pygame.image.load(os.path.join('assets', 'anatomy.png'))
x = 0

while not gameover:
    win.fill((0, 0, 0))
    win.blit(image, ((0-x), 0+x))
    keys = pygame.key.get_pressed()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_a]:
            x += 1
            image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'anatomy.png')), (512 + x, 512 + x))
        if keys[pygame.K_d]:
            x -= 1
            image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'anatomy.png')), (512 + x, 512 + x))

    pygame.display.update()
