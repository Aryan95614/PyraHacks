import pygame, os, sys

# code you have to write, its just making game loop
win = pygame.display.set_mode((512, 512))

gameover = False

image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'cat.png')), (64, 64))
image_Rect = image.get_rect()
image_Rect.x = 650
image_Rect.y = 450
dx = 0

Clock = pygame.time.Clock()
def getMousePos():
    return pygame.mouse.get_pos()


while not gameover:
    win.fill((0, 0, 0))
    Clock.tick(60)
    win.blit(image, image_Rect)
    x, y = getMousePos()
    keys = pygame.key.get_pressed()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()

    if x > image_Rect.x:
        image_Rect.x += 4
    if x < image_Rect.x:
        image_Rect.x -= 4
    if y > image_Rect.y:
        image_Rect.y += 4
    if y < image_Rect.y:
        image_Rect.y -= 4

    if x == image_Rect.x and y == image_Rect.y:
        sys.exit()

    pygame.display.update()
