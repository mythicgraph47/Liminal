import pygame
import random


#game init
pygame.init()

#window
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("background.png")

#title and icon
title = pygame.display.set_caption("Larping Invaders")
icon = pygame.image.load("dumbbell.png")
pygame.display.set_icon(icon)

#player
playerIMG = pygame.image.load("spaceship.png")
playerIMG = pygame.transform.scale(playerIMG, (64, 64))
playerX = 355
playerY = 470
playerX_change = 0

def player(x, y):
    screen.blit(playerIMG, (x, y))

#enemy
enemyIMG = pygame.image.load("enemy.png")
enemyIMG = pygame.transform.scale(enemyIMG, (64, 64))
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 100)
enemyX_change = 0.3
enemyY_change = 40

def enemy(x, y):
    screen.blit(enemyIMG, (x, y))

#Bullet
bulletIMG = pygame.image.load("bullet.png")
bulletIMG = pygame.transform.scale(bulletIMG, (44, 44))
bulletX = 0
bulletY = 0
bulletY_change = 0

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))
           
#gameloop
running = True
while running:
    #background 
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print("A key has been pressed.")

            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3
                print("Left Key.")
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.3
                print("Left Key.")
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("A keystroke has been released")


    player(playerX, playerY)
    playerX += playerX_change


    #player
    if playerX <= 0:
        playerX_change = 0

    elif playerX >= 736:
        playerX = 736


    #enemy
    enemy(enemyX, enemyY)
    enemyX += enemyX_change

    
    if enemyX <= 0:
        enemyX = 0
        enemyX_change *= -1
        enemyY += enemyY_change

    elif enemyX >= 736:
        enemyX = 736
        enemyX_change *= -1
        enemyY += enemyY_change


    #Bullet
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change
    
    pygame.display.update()
