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
TEXT_AQUA = (0, 68, 85)

# Create window
WINDOW_SIZE = (800, 800)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Leggy's Big Adventure!")
FPS = 120

# Create game class
class Game:
    def __init__(self):
        self.scene = "menu"

    def menu(self):
        # Create functions for buttons
        quit_func = lambda: pygame.event.post(pygame.event.Event(QUIT))

        # Create UI elements
        title_text = ut.Text("Leggy's Big Adventure!", 55, (53, 50), WINDOW, TEXT_AQUA)
        quit_button = ut.Button(quit_func, "Quit", 30, (350, 400), WINDOW, TEXT_AQUA, WHITE, BLACK, 10)

        # Create player and tilemap elements
        level = l_m.Level(0)
        player = vis.Player(level.start_coords, WINDOW_SIZE, level.level_data, level.tilemap_sprite_group, 100)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pressed = pygame.key.get_pressed()
            if pressed[K_q]:
                pygame.event.post(pygame.event.Event(QUIT))
            elif pressed[K_1]:
                self.scene = "level_1"
                running = False

            WINDOW.fill(PASTEL_BLUE)
            level.output(WINDOW)
            player.process(WINDOW)
            title_text.out()
            quit_button.out()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

        # Delete level and player objects
        del level
        del player

    def level_1(self):
        # Load Level
        level1 = l_m.Level(1)
        # Create player
        player = vis.Player(level1.start_coords, WINDOW_SIZE, level1.level_data, level1.tilemap_sprite_group, 100)
        # Create text object
        title = ut.Text("Get to the cheese!", 50, (150, 50), WINDOW, TEXT_AQUA)

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

        # Delete level and player objects
        del level1
        del player

    def run_game(self):
        while True:
            if self.scene == "menu":
                self.menu()
            elif self.scene == "level_1":
                self.level_1()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run_game()
