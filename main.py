import pygame
from pygame.locals import *
from random import randint
from math import sin, cos, pi


class SnowFlake:
    def __init__(self):
        self.x = randint(0, 715)
        self.y = -5
        self.angle = randint(135, 225)
        self.falling = True


screen = pygame.display.set_mode((600, 600))
running = True

snow_flakes = list()
while running:
    pygame.time.Clock().tick(60)
    screen.fill((130, 185, 255))
    ground = pygame.draw.rect(screen, (220, 220, 220), (0, 560, 600, 40))

    if randint(0, 9) == 5:
        snow_flakes.append(SnowFlake())

    while True:
        try:
            for num, snow_flake in enumerate(snow_flakes):
                snow_hitbox = pygame.draw.rect(screen, (255, 255, 255), (snow_flake.x, snow_flake.y, 5, 5))
                
                if snow_flake.falling:
                    old_x = snow_flake.x
                    old_y = snow_flake.y
                    
                    snow_flake.x += sin(snow_flake.angle * (pi/180))
                    snow_flake.y -= cos(snow_flake.angle * (pi/180))
                    
                    old_angle = snow_flake.angle
                    while True:
                        snow_flake.angle += randint(-5, 5)
                        if snow_flake.angle in range(135, 226):
                            break
                        snow_flake.angle = old_angle

                    if snow_hitbox.colliderect(ground):
                        snow_flake.falling = False
                        snow_flake.x = old_x
                        snow_flake.y = old_y

                    for n, flake in enumerate(snow_flakes):
                        if snow_hitbox.colliderect(pygame.Rect(flake.x, flake.y, 5, 5)) and n != num and not flake.falling and snow_flake.falling:
                            snow_flake.y += 2
                            snow_flake.falling = False
                            break

                if snow_flake.y >= 600:
                    snow_flake.y = -5
                    snow_flake.x = randint(0, 595)
            break
        except:
            pass


    pygame.display.flip()

    for ev in pygame.event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_END:
                running = False
            elif ev.key == K_HOME:
                snow_flakes.clear()
