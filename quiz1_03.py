# quiz1_03.py

import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(SCREEN_SIZE)

h_img = pygame.image.load('images/hammer.png')
h_pos = h_img.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2)

pygame.key.set_repeat(5, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                h_pos.left -= 5
            elif event.key == pygame.K_RIGHT:
                h_pos.left += 5
            if event.key == pygame.K_UP:
                h_pos.top -= 5
            elif event.key == pygame.K_DOWN:
                h_pos.top += 5

        if h_pos.right < 0:
            h_pos.left = SCREEN_WIDTH
        elif h_pos.left > SCREEN_WIDTH:
            h_pos.right = 0
        if h_pos.bottom < 0:
            h_pos.top = SCREEN_HEIGHT
        elif h_pos.top > SCREEN_HEIGHT:
            h_pos.bottom = 0

        screen.fill(BLACK)
        screen.blit(h_img, h_pos)
        pygame.display.update()

pygame.quit()