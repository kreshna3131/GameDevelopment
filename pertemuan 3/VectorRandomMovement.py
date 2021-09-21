import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, startpos, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.image = pygame.image.load("bola.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect(
            center=(round(self.pos.x), round(self.pos.y)))

    def reflect(self, NV):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))

    def update(self):
        self.pos += self.dir * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)


pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

all_groups = pygame.sprite.Group()
start, velocity, direction = (250, 250), 5, (random.random(), random.random())
ball = Ball(start, velocity, direction)
all_groups.add(ball)

GREY = (128, 128, 128)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_groups.update()

    if ball.rect.left <= 100:
        ball.reflect((1, 0))
    if ball.rect.left >= 300:
        ball.reflect((-1, 0))
    if ball.rect.left <= 100:
        ball.reflect((0, 1))
    if ball.rect.left >= 300:
        ball.reflect((0, -1))

    window.fill(GREY)
    pygame.draw.rect(window, (255, 0, 0), (100, 100, 300, 300), 1)
    all_groups.draw(window)
    pygame.display.flip()

pygame.quit()