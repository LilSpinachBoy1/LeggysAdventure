"""
MODULE FOR ALL VISUAL OUTPUTS:
- Class for tiles within tilemaps
- Class for player sprite
"""
import pygame
import os
from pygame.locals import *

PATH_TO_SNAIL = os.getcwd() + "/Assets/SN_idle.png"


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_style, image, map_coords: tuple, screen_size: tuple, tilemap_size: tuple):
        super().__init__()
        # Store the tile style in order to filter out air tiles later
        self.tile_style = tile_style

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
    def __init__(self, start_pos: tuple, screen_size: tuple, tilemap_data, tilemap, scale: int):
        super().__init__()

        # Load the image and scale it
        self.image = pygame.transform.scale(pygame.image.load(PATH_TO_SNAIL), (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos

        # Store params in the object
        self.screen_size = screen_size
        self.tilemap_data = tilemap_data
        self.tilemap = tilemap
        self.scale = scale

        # Store version of tilemap which does not contain air blocks
        self.tilemap_no_air = []
        for tile in self.tilemap:
            if tile.tile_style != 0:
                self.tilemap_no_air.append(tile)

        # Store constants
        self.SPEED = 4
        self.GRAVITY = 7

    # noinspection PyTypeChecker
    def movement_and_collisions(self):
        keys = pygame.key.get_pressed()
        initial_pos = self.rect.copy()  # Create the rect to simulate the movement
        # Do x movement
        if keys[K_a]:
            self.rect.x -= self.SPEED
        if keys[K_d]:
            self.rect.x += self.SPEED

        # Do y movement
        self.rect.y += self.GRAVITY

        # Check for collisions within the tilemap
        is_collision = pygame.sprite.spritecollideany(self, self.tilemap_no_air)
        while is_collision:
            # These statements set the amount that needs to be added to the rect to move it back towards the initial position
            if self.rect.x < initial_pos.x:
                x_direction = 1
            elif self.rect.x > initial_pos.x:
                x_direction = -1
            else:
                x_direction = 0

            if self.rect.y < initial_pos.y:
                y_direction = 1
            elif self.rect.y > initial_pos.y:
                y_direction = -1
            else:
                y_direction = 0

            # Move the rect back towards the initial position
            self.rect.x += x_direction
            self.rect.y += y_direction

            # Check for collisions again
            is_collision = pygame.sprite.spritecollideany(self, self.tilemap_no_air)

    def process(self, screen):
        self.movement_and_collisions()
        screen.blit(self.image, self.rect)
