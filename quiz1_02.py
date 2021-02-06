# quiz1_02.py

import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PYGAME2')

d_img = pygame.image.load('images/dig.png')
moles = []
for x_pos in range(3):
    for y_pos in range(3):
        mole_pos = (x_pos * 200 + 10, y_pos * 200 + 10)
        moles.append(mole_pos)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for one_pos in moles:
        screen.blit(d_img, one_pos)

    pygame.display.update()

pygame.quit()
