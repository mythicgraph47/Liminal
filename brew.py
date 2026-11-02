import pygame
import random
import main
import rooms
import game

def draw_vignette(surface, playerX, playerY, radius = 200):

    width = surface.get_width()
    height = surface.get_height()

def buzzing(surface, intensity = 6):

    width = surface.get_width()
    height = surface.get_height()

    for z in range(intensity):
        x = random.randint(0, width)
        y = random.radnint(0, height)

        #sq
        pygame.draw.rect(surface, (120, 120, 120), (x, y, 2)


def glitching_Text(surface, font, text, x, y, color = [200, 200, 200]):
    shadow = font.render(text, True, (100, 0, 0))

    surface.blit(shadow, (x + 2, y))


    main_text font.render(text, true, color)
    surface.blit(main_text, (x, y))