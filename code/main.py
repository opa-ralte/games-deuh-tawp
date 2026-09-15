import pygame
import random
import os

WIDTH, HEIGHT = 1280, 720

class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load(os.path.join('images', 'mapuia.png'), 'mapuia').convert_alpha()
        self.rect = self.image.get_frect(center = (WIDTH/2, HEIGHT/2))
        self.dir = pygame.math.Vector2(0, 0)
        self.speed = 300.0

    def update(self, dt):
        keys = pygame.key.get_pressed()
        keys_just_pressed = pygame.key.get_just_pressed()
        self.dir.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.dir.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.dir = self.dir.normalize() if self.dir else self.dir
        self.rect.center += self.dir * self.speed * dt
        if keys_just_pressed[pygame.K_SPACE]:
            print("fire lazer")

class Lenin(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load(os.path.join('images', 'lenin.png'), 'lenin').convert_alpha()
        self.rect = self.image.get_frect(bottomright = (WIDTH - 10, HEIGHT - 10))
        self.dir = pygame.math.Vector2(0, -1)
        self.speed = 300.0

    def bounce_vertically(self, dt):
        # making lenin bounce vertically
        if self.rect.top < 0:
            self.rect.top = 1
            self.dir.y = 1
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.dir.y = -1
        self.rect.center += self.dir * self.speed * dt

class Stars(pygame.sprite.Sprite):
    def __init__(self, group, surf):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(center = (random.randint(0, WIDTH-10), random.randint(0, HEIGHT-10)))
    
# general setup
pygame.init()
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("games deuh tawp ang chi kha!!!")
icon_surface = pygame.image.load(os.path.join('images', 'icon', 'cropped_icon.jpg'), 'cropped_icon').convert()
pygame.display.set_icon(icon_surface)

# sprite group setup
all_sprites = pygame.sprite.Group()

# stars objects setup
star_surf = pygame.image.load(os.path.join('images', 'siar.png'), 'siar').convert_alpha()
for i in range(20):
    Stars(all_sprites, star_surf)
    
# lenin object setup
lenin = Lenin(all_sprites)

# mapuia object setup
mapuia = Player(all_sprites)

on_action = True
clock = pygame.time.Clock()

while on_action:
    dt = clock.tick(60) / 1000
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            on_action = False
        
    # mapuia movement control 🎮
    mapuia.update(dt)

    # lenin movement
    lenin.bounce_vertically(dt)

    display_surface.fill('midnightblue')

    all_sprites.draw(display_surface)
    pygame.display.flip()

pygame.quit()