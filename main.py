# Example file showing a circle moving on screen
from threading import Condition

import pygame

from projectile import fire_bullet

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_SPEED = 500
PLAYER_WIDTH = 40

Condition = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

print("test")

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.circle(screen, "Blue", player_pos, PLAYER_WIDTH)

    keys = pygame.key.get_pressed()
  # if keys[pygame.K_z]:
  #      player_pos.y -= PLAYER_SPEED * dt
  # if keys[pygame.K_s]:
  #     player_pos.y += PLAYER_SPEED * dt
    if keys[pygame.K_q]:
        player_pos.x -= PLAYER_SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += PLAYER_SPEED * dt
    if keys[pygame.K_SPACE]:
        fire_bullet(player_pos.x,player_pos.y)

    while Condition == 0:
        player_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT - PLAYER_WIDTH - 20)
        Condition = Condition + 1

    r = PLAYER_WIDTH
    player_pos.x = max(r, min(SCREEN_WIDTH - r, player_pos.x))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

