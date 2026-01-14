
import pygame
from pygame.math import Vector2

from main import screen

# on ne voit pas le projectile sur l'écran
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"

def fire_bullet (x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10)) # pour que la balle soit tirée du centre de la boule


    if bullet_state == "fire":
        fire_bullet(x,y)
        y -= bulletY_change


