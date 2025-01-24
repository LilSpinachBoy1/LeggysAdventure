import pygame
import sys
from Scripts import level_manager as l_m
from Scripts import visuals as vis

pygame.init()

# Colour constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PASTEL_BLUE = (0, 204, 255)

# Create window
WINDOW_SIZE = (800, 800)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Leggy's Big Adventure!")
FPS = 120

# Load Level
level1 = l_m.Level(1)

# Create player
player = vis.Player((350, 400), WINDOW_SIZE, level1.level_data, level1.tilemap_sprite_group, 100)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw level
    WINDOW.fill(PASTEL_BLUE)
    level1.output(WINDOW)
    player.process(WINDOW)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

