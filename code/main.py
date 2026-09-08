import pygame

WIDTH, HEIGHT = 1280, 720

# general setup
pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

on_action = True

while on_action:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            on_action = False

    # draw the game
    pygame.display.flip()

pygame.quit()