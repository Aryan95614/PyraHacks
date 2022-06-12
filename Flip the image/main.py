import pygame, os, sys


win = pygame.display.set_mode((512, 512))

gameover = False

image = pygame.image.load(os.path.join('assets', 'geometric.png'))
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
            image = pygame.transform.flip(image, True, False)
        if keys[pygame.K_d]:
            x -= 1
            image = pygame.transform.flip(image, False, True)

    pygame.display.update()
