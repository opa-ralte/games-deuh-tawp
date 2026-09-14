import pygame
import random
import os

WIDTH, HEIGHT = 1280, 720

# general setup
pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("games deuh tawp ang chi kha!!!")
icon_surface = pygame.image.load(os.path.join('images', 'icon', 'cropped_icon.jpg'), 'cropped_icon').convert()
pygame.display.set_icon(icon_surface)

# mapuia setup
mapuia_surface = pygame.image.load(os.path.join('images', 'mapuia.png'), 'mapuia').convert_alpha()
mapuia_rect = mapuia_surface.get_frect(center = (WIDTH/2, HEIGHT/2))
mapuia_direction = pygame.math.Vector2(1, 2)
mapuia_speed = 100.0

# lenin setup  
lenin_surface = pygame.image.load(os.path.join('images', 'lenin.png'), 'lenin').convert_alpha()
lenin_rect = lenin_surface.get_frect(bottomright = (WIDTH - 10, HEIGHT - 10))
lenin_x = WIDTH//2
lenin_y = HEIGHT//2
lenin_direction = 1.0

# background lovely dovely setup
siar_surface = pygame.image.load(os.path.join('images', 'siar.png'), 'siar').convert_alpha()
siar_rect = siar_surface.get_frect(center = (10, 10))


on_action = True
clock = pygame.time.Clock()

while on_action:
    dt = clock.tick(6) / 1000
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            on_action = False
        

    # draw the game
    display_surface.fill('midnightblue')
        
    # pygame.draw.line(display_surface, 'red', (20, 30), (70, 50), 5)
    # pygame.draw.line(display_surface, 'red', (70, 50), (70, 100), 5)
    # pygame.draw.line(display_surface, (200, 200, 0), (10, 10), (100, 100), 10)
    # pygame.draw.arc(display_surface, (200, 100, 200), pygame.Rect(10, 100, 500, 500), 0.1, 1, 30)
    # pygame.draw.polygon(display_surface, (100, 100, 0), [(100, 100), (200, 300), (500, 600), (700, 700)], 20)

    # making lenin bounce vertically
    lenin_rect.y -= 0.5 * lenin_direction
    if lenin_rect.centery < 0 and lenin_direction == 1.0:
        lenin_direction = -1.0
    elif lenin_rect.centery > HEIGHT-20 and lenin_direction == -1.0:
        lenin_direction = 1.0

    display_surface.blit(lenin_surface, lenin_rect)

    keys = pygame.key.get_pressed()

    mapuia_rect.center += mapuia_direction * mapuia_speed * dt

    # the dvd animation...
    if mapuia_rect.top < 0:
        mapuia_direction.y *= -1
    if mapuia_rect.bottom > HEIGHT:
        mapuia_direction.y *= -1
    if mapuia_rect.left < 0:
        mapuia_direction.x *= -1
    if mapuia_rect.right > WIDTH:
        mapuia_direction.x *= -1

    # if keys[pygame.K_a]:
    #     mapuia_direction = (-1, 0)
    #     mapuia_rect.center = mapuia_direction * mapuia_speed * dt

    # if keys[pygame.K_d]:
    #     mapuia_direction = (1, 0)
    #     mapuia_rect.center = mapuia_direction * mapuia_speed * dt

    # if keys[pygame.K_w]:
    #     mapuia_direction = (0, -1)
    #     mapuia_rect.center -= mapuia_direction * mapuia_speed * dt

    # if keys[pygame.K_s]:
    #     mapuia_direction = (0, 1)
    #     mapuia_rect.center += mapuia_direction * mapuia_speed * dt
    
    display_surface.blit(mapuia_surface, mapuia_rect)
    
    pygame.display.flip()

pygame.quit()