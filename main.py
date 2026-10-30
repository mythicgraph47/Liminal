import pygame

#globals
r = 0.5

#initialzie
pygame.init()


#title and icon
title = pygame.display.set_caption("Larping Invaders")
icon = pygame.image.load("dumbbell.png")
pygame.display.set_icon(icon)

#screen
screen = pygame.display.set_mode((800, 600))

#player
playerIMG = pygame.image.load("spaceship.png")
playerIMG = pygame.transform.scale(playerIMG, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerIMG, (x, y))

   
#gameloop
running = True
while running:

    screen.fill((0, 0, 0))
    

    #event manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

         #keyboard event manager
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")

            if event.key == pygame.K_LEFT:
               playerX_change -= 0.3

            if event.key == pygame.K_RIGHT:
               playerX_change += 0.3

        if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              playerX_change = 0
              print("A keystroke has been released")

    player(playerX, playerY)
    playerX += playerX_change


    #boundary
    if playerX_change >= 800:
        playerX = 800
    elif playerX_change <= 0
    playerX = 0
    

   
    pygame.display.update()



