import pygame
import random

def draw_vignette(surface, player_x, player_y, radius=250):
    """Draws a dark overlay with a transparent circle around the player."""
    vignette = pygame.Surface((surface.get_width(), surface.get_height()), pygame.SRCALPHA)
    # Fill entire screen with semi-transparent black
    vignette.fill((0, 0, 0, 180))
    # "Erase" a circle around the player (making it transparent)
    pygame.draw.circle(vignette, (0, 0, 0, 0), (int(player_x), int(player_y)), radius)
    surface.blit(vignette, (0, 0))

def draw_static(surface, intensity=5):
    """Draws random white/gray pixels to simulate VHS noise."""
    width, height = surface.get_width(), surface.get_height()
    for _ in range(intensity):
        x = random.randint(0, width)
        y = random.randint(0, height)
        pygame.draw.rect(surface, (120, 120, 120), (x, y, 2, 2))

def render_glitch_text(surface, font, text, x, y, color=(200, 200, 200)):
    """Renders text with a red/blue offset to look glitchy."""
    # Red shadow offset
    shadow_red = font.render(text, True, (100, 0, 0))
    surface.blit(shadow_red, (x + 2, y))
    
    # Blue shadow offset
    shadow_blue = font.render(text, True, (0, 0, 100))
    surface.blit(shadow_blue, (x - 2, y))
    
    # Main text
    main_text = font.render(text, True, color)
    surface.blit(main_text, (x, y))