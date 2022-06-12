import pygame, sys, os

pygame.init()

win = pygame.display.set_mode((800, 800))
image = pygame.transform.scale( pygame.image.load(os.path.join('assets', 'shooter.png')),(280, 280))
image_rect = image.get_rect()
image_rect.x = 50
image_rect.y = 250

gameover = False

class laser():
    def __init__(self, x, y):
        self.image = pygame.transform.scale( pygame.image.load(os.path.join('assets', 'bullet.png')),(128, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move = False

    def draw(self, win):
        self.rect.x += 1 if self.move else 0
        if self.rect.x == 672:
            self.rect.x = 100
            self.move = False
        win.blit(self.image, self.rect)

Laser = [laser(100, 288), laser(100, 288)]
while not gameover:
    win.fill((0, 50, 0))

    Laser[0].draw(win)
    win.blit(image, image_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Laser[0].move = True


    pygame.display.update()