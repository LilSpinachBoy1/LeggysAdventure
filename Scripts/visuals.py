"""
MODULE FOR ALL VISUAL OUTPUTS:
- Class for tiles within tilemaps
- Class for player sprite
"""
import pygame
from pygame.locals import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, map_coords: tuple, screen_size: tuple, tilemap_size: tuple):
        super().__init__()

        # Get image and associated rect
        self.image = image
        self.rect = self.image.get_rect()
        self.map_x, self.map_y = map_coords

        # Get details for finding absolute coordinates on the screen
        self.screen_size = screen_size
        self.tilemap_size = tilemap_size

        # Set the position of the tile
        self.rect.topleft = self.get_absolute_coords()

    def get_absolute_coords(self) -> tuple:
        tile_size = self.screen_size[0] / self.tilemap_size[0]  # Work out the size of each tile
        abs_x = self.map_x * tile_size  # Find the real coordinate of the x plane
        abs_y = self.map_y * tile_size  # Find the real coordinate of the y plane
        return abs_x, abs_y  # Return the absolute coordinates

    def output(self, screen):
        screen.blit(self.image, self.rect)


# WHAT THIS NEEDS TO DO
# - Load an image for the player
# - Scale the image to a set size
# - MOVEMENT AND COLLISIONS:
#   - Move the player sprite
#   - Check for collisions
#     - Make a new rect for where the player would move to with current movement
#     - Check if this rect collides with any other rects
#     - If it does, reduce the movement by one
#     - Repeat until there is no collision
#     - Do movement
# - Output the player sprite to the screen
class Player(pygame.sprite.Sprite):
    def __init__(self, image, map_coords: tuple, screen_size: tuple, tilemap_size: tuple):
        super().__init__()
