import pygame
from game import LiminalGame

if __name__ == "__main__":
    pygame.init()
    game = LiminalGame()
    game.run()
    pygame.quit()