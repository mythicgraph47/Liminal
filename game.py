import pygame

#initialzie
pygame.init()

#window
screen = pygame.display.set_mode((800, 600))

#title and icon
title = pygame.display.set_caption("Larping Invaders")
icon = pygame.image.load("dumbbell.png")
pygame.display.set_icon(icon)

#player
playerIMG = pygame.image.load("spaceship.png")
playerIMG = pygame.transform.scale(playerIMG, (64, 64))
playerX = 470
playerY = 380
playerX_change = 0

#playermain
def player(x, y):
    screen.blit(playerIMG, (x, y))

#game loop
running = True
while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)

    pygame.display.update()