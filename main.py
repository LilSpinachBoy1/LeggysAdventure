import pygame
from pygame.locals import *
import sys
from Scripts import level_manager as l_m
from Scripts import visuals as vis
from Scripts import utils as ut

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
print(level1.start_coords)
# Create player
player = vis.Player(level1.start_coords, WINDOW_SIZE, level1.level_data, level1.tilemap_sprite_group, 100)

# Create game class
class Game:
    def __init__(self):
        self.scene = "level_1"

    def menu(self):
        pass

    def level_1(self):
        # Create text object
        title = ut.Text("Leggy's Big Adventure!", 50, (50, 50), WINDOW)

        running = True
        # Game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Check for key presses
            pressed = pygame.key.get_pressed()
            if pressed[K_ESCAPE]:
                self.scene = "menu"
                running = False

            # Draw level
            WINDOW.fill(PASTEL_BLUE)
            level1.output(WINDOW)
            player.process(WINDOW)
            title.out()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

    def run_game(self):
        if self.scene == "menu":
            self.menu()
        elif self.scene == "level_1":
            self.level_1()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run_game()
