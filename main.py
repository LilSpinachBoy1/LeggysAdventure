import pygame
import sys
from Scripts import level_manager as l_m

pygame.init()

# Create window
WINDOW_SIZE = (800, 800)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Leggy's Big Adventure!")

# Load Level
level1 = l_m.Level(1)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw level
    WINDOW.fill((255, 255, 255))
    level1.output(WINDOW)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

