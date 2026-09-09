import pygame
import random
import os

WIDTH, HEIGHT = 1280, 720

# general setup
pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("games deuh tawp ang chi kha!!!")
icon_surface = pygame.image.load(os.path.join('images', 'icon', 'cropped_icon.jpg'), 'cropped_icon').convert_alpha()
pygame.display.set_icon(icon_surface)


on_action = True

while on_action:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            on_action = False
        

    # draw the game
    display_surface.fill('cornsilk1')
    pygame.draw.line(display_surface, 'red', (20, 30), (70, 50), 5)
    pygame.draw.line(display_surface, 'red', (70, 50), (70, 100), 5)
    pygame.draw.line(display_surface, (200, 200, 0), (10, 10), (100, 100), 10)
    pygame.draw.arc(display_surface, (200, 100, 200), pygame.Rect(10, 100, 500, 500), 0.1, 1, 30)
    pygame.draw.polygon(display_surface, (100, 100, 0), [(100, 100), (200, 300), (500, 600), (700, 700)], 20)
    pygame.display.flip()

pygame.quit()