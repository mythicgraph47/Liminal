import pygame
import rooms
import random
import brew

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

        #player
        self.player_rect = pygame.Rect(300, 500, 40, 40)
        self.player_speed = 4
        self.playerX_change = 0
        self.playerY_change = 0

        #fragements / shards
        self.spawn_fragment()

    def spawn_fragments(self):
        self.fragmentX = random.randint(50, self.width - 50)
        self.fragmentY = -50
        self.fragment_speed = random.uniform(2, 7)
        self.fragment_rect = pygame.Rect(self.fragmentX, self.fragmentY, 30, 30)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                print('key has been pressed')

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.playerX_change -= self.player_speed
                    print("left movement")
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.playerX_change += self.player_speed
                    print("right movement")
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.playerY_change -= self.player_speed
                    print("up movement")
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.playerY_change += self.player_speed
                    print("down movement")

            if event.type == pygame.KEYUP:
                self.playerX_change = 0
                self.playerY_change = 0

    def update(self):
        current_room = self.room_list[self.current_room_idx]

            #player move
        self.player_rect.x += self.playerX_change
        self.player_rect.y += self.playerY_change


            #shards move

        self.fragmentY += self.fragment_speeds
        self.fragment_rect.y = self.fragmentX
        self.fragment_rect.x = self.fragmentY

        if self.fragmentY >= self.height:
            self.spawn_fragments()

        if self.player_rect.collidedict(self.fragment_rect):
            self.fragments_collected += 1
            self.spawn_fragments()

                if self.fragments_collected >= self.fragments_needed:
                self.fragments_collected = 0
                self.current_room_idx += 1

            if self.current_room_idx >= len(self.room_list):
                self.current_room_idx = 0


    def draw(self):
        current_room = self.room_list[self.current_room_idx]

        #background
        self.screen.fill(current_room["background_color"])

        #walls
        for wall in current_room["walls"]:
            pygame.draw.rect(self.screen, current_room["wall_color"], wall)
        #shards/fragments
        points = [
            (self.fragmentX, self.fragmentY + 30),
            (self.fragmentX + 45, self.fragmentY + 45),
            (self.fragmentX + 20, self.fragmentY)
        ]
        pygame.draw.rect(self.screen, (150, 20,20), points)

        #player
        pygame.draw.rect(self.screen, (220, 220, 220), self.player_rect)

        #effects
        brew.draw_vignette(self.screen, self.player_rect.centerx)
        brew.buzzing(self.screen, intensity=8)

        #ui
        ui_text = f"FRAGMENTS: {self.fragments_collected} / {self.fragments_needed}"

        brew.render_glitch_text(self.screen, self.font, ui_text, 20, 20)

        room_text = f"LOCATION: {current_room["name"]}"

        brew.glitching_Text(self.screen, self.font, room_text, 20, 50, (100, 100, 100))

        atmosphere_text = current_room["vibe"]
        atmosphere_surface = self.font.render(atmosphere_text, true, (50, 50, 50))
        self.screen.blit(atmosphere_surface, 
                         (self.width - atmosphere_surface.get_width()
                                              
                                              - 20,
                                                self.height - 40))
        

        pygame.display.flip()





    #running
    def run(self):
        self.running = True
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.screen.fill((0, 0, 0))
            self.handle_events()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)
