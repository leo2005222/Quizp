# quiz1_01.py

import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PYGAME')

d_img = pygame.image.load("images/dig.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    screen.blit(d_img, (10, 10))
    pygame.display.update()

pygame.quit()
