import pygame
import rooms

class LiminalGame:
    def __init__(self):

        #declaring globals
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("True Liminality")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("couriernew", 20, bold=True)
        self.big_Font = pygame.font.SysFont("couriernew", 40, bold=True)

        #game state
        self.running = True
        self.room_list = rooms.get_rooms()
        self.current_room_idx = 0
        self.fragments_needed = 3
        self.fragments_collected = 0
    #running
    def run(self):
        self.running = True
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.screen.fill((0, 0, 0))

            pygame.display.update()

            self.clock.tick(60)
