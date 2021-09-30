import pygame
from pygame import Surface, image
from pygame import surface
from pygame.locals import *

pygame.init()

black = (0, 0, 0)
silver = (226,226,226)
white = (255, 255, 255)
graydeep = (172, 172, 172)
blue = (51, 153, 255)
brown = (204, 102, 0)
orange = (233,119,0)
grayy = (75,75,75)

# background_color = (224, 224, 224)
(width, height) = (801, 681)

screen = pygame.display.set_mode((width, height))
screen.fill(white)

# body rumah
pygame.draw.rect(screen, blue, (201, 260, 400, 270))
# cerobong asap
pygame.draw.rect(screen, grayy, (521, 155, 50, 30))
pygame.draw.rect(screen, grayy, (530, 165, 30, 50))
# atap
pygame.draw.lines(screen, orange, True, [(170, 250), (390,179), (630, 250)], 40)
pygame.draw.rect(screen, orange, (281, 200, 230, 50))
# border rumah
pygame.draw.rect(screen, black, (601, 270, 2, 250))
pygame.draw.rect(screen, black, (201, 270, 2, 250))
pygame.draw.rect(screen, black, (201, 270, 400, 2))
# border atap
pygame.draw.rect(screen, black, (171, 270, 460, 2))
pygame.draw.rect(screen, black, (171, 230, 2, 40))
pygame.draw.rect(screen, black, (631, 232, 2, 40))
pygame.draw.line(screen, black, (390, 158), (632, 232), 2)
pygame.draw.line(screen, black, (389, 159), (172, 230), 2)
# alas rumah
pygame.draw.rect(screen, silver, (176, 520, 450, 20))
# border alas rumah
pygame.draw.rect(screen, black, (176, 520, 450, 2))
pygame.draw.rect(screen, black, (176, 540, 450, 2))
pygame.draw.rect(screen, black, (176, 520, 2, 20))
pygame.draw.rect(screen, black, (625, 520, 2, 22))
# pintu
pygame.draw.rect(screen, brown, (351, 360, 100, 170))
# border pintu
pygame.draw.rect(screen, black, (351, 360, 2, 170))
pygame.draw.rect(screen, black, (451, 360, 2, 170))
pygame.draw.rect(screen, black, (351, 360, 100, 2))
# alas pintu
pygame.draw.rect(screen, graydeep, (346, 530, 110, 10))
# gagang pintu
pygame.draw.circle(screen, black, (437, 460), 5, 20)
# jendela kiri
pygame.draw.rect(screen, white, (231, 370, 80, 80))
pygame.draw.rect(screen, black, (231, 370, 5, 80))
pygame.draw.rect(screen, black, (311, 370, 5, 80))
pygame.draw.rect(screen, black, (231, 370, 80, 5))
pygame.draw.rect(screen, black, (231, 445, 80, 5))
pygame.draw.rect(screen, black, (231, 409, 80, 5))
pygame.draw.rect(screen, black, (271, 370, 5, 80))
# jendela kanan
pygame.draw.rect(screen, white, (486, 370, 80, 80))
pygame.draw.rect(screen, black, (481, 370, 5, 80))
pygame.draw.rect(screen, black, (521, 370, 5, 80))
pygame.draw.rect(screen, black, (561, 370, 5, 80))
pygame.draw.rect(screen, black, (481, 370, 80, 5))
pygame.draw.rect(screen, black, (481, 409, 80, 5))
pygame.draw.rect(screen, black, (481, 445, 80, 5))
# tiang bendera
pygame.draw.rect(screen, graydeep, (111, 535, 30, 5))
pygame.draw.rect(screen, graydeep, (116, 530, 20, 5))
pygame.draw.rect(screen, graydeep, (124, 335, 5, 200))

Image = pygame.image.load('bendera.jpg')
Pos = (60,340)
screen.blit(Image, Pos)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()