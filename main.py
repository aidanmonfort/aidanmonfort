import random

import pygame

from Dino import *
from Backround import *
from Blocks import *

grav = -.2
level = 1
pygame.init()
pygame.display.set_caption("Dinosaur Game")
window = pygame.display.set_mode((550, 550))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
dinosaur = Dino(grav, screen)
back = Backround(screen, 0)
obst = []
running = True

def checkInput():
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        dinosaur.jump()

def spawnObstacles():
    global obst, level, screen, grav, dinosaur
    for i in range(1, 7):
        choice = random.randint(0, 2)
        if choice == 0:
            obst.append(Rock(screen, level, (i * pygame.Surface.get_width(screen)/1.5),
                         pygame.Surface.get_height(screen) * (5/6)))
        else:
            obst.append(Cactus(screen, level, (i * pygame.Surface.get_width(screen)/1.5),
                         pygame.Surface.get_height(screen) * (5/6)))

    level += 1
    grav += -.025

def checkCollisions():
    global obst, dinosaur, running
    for Obstacle in obst:
        if pygame.Rect.colliderect(Obstacle.getCollisionRectangle(), dinosaur.getCollisionRect()):
            running = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    checkInput()
    dinosaur.update(screen)
    back.update()
    for Obstacle in obst:
        Obstacle.update()
        if Obstacle.x < -20:
            obst.remove(Obstacle)

    checkCollisions()
    screen.fill((0,0,0))
    back.draw(screen)
    dinosaur.draw(screen)
    for Obstacle in obst:
        Obstacle.draw(screen)

    if len(obst) == 0:
        dinosaur.grav = grav
        spawnObstacles()

    pygame.display.flip()
    clock.tick(60)

