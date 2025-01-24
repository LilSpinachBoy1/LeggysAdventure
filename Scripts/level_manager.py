"""
SCRIPT TO COVER VARIOUS ASPECTS OF LEVEL MANAGEMENT, INCLUDING:
- Read level data from txt files
- Pass level data to the main game
- Load file assets for levels
"""
import pygame
pygame.init()

# CREATE CONSTANTS
TILE_SIZE = 50  # This accommodates for a 16x16 tilemap, see 'TILEMAP_INFO.md' for more
PATH_TO_TILEMAP = "../Assets/TILEMAP/"
PATH_TO_LEVELS = "../Levels/"


# Create class to manage levels
# WHAT THIS NEEDS TO DO:
# - Load level data from txt files
# - Convert level data to array
# - Load tile assets for levels
# - Map tiles to rects and give each their respective coordinates
# Easy peasy right?
class Level:
    def __init__(self, level_num):
        # Get level data from file
        self.level_num = level_num
        self.level_data = self.load_level_data()

        # Load tile assets
        self.tiles = {
            0: pygame.image.load(PATH_TO_TILEMAP + "0.png"),
            1: pygame.image.load(PATH_TO_TILEMAP + "1.png"),
            2: pygame.image.load(PATH_TO_TILEMAP + "2.png"),
        }

    def load_level_data(self) -> list:
        try:
            file_path = PATH_TO_LEVELS + f"level_{self.level_num}.txt"
            level_data = []
            with open(file_path, "r") as file:
                for line in file:
                    level_data.append(line.strip().split(" "))
            return level_data
        except FileNotFoundError:
            print(f"Level {self.level_num} not found.")


# TESTING
if __name__ == "__main__":
    test_level = Level(1)
    print("LEVEL DEBUG REPORT:")
    print(f"Level Number: {test_level.level_num}")
    print(f"Num of rows: {len(test_level.level_data)}           Pass? {len(test_level.level_data) == 16}")
    print(f"Num of columns: {len(test_level.level_data[0])}        Pass? {len(test_level.level_data[0]) == 16}")
    print("Raw data:")
    for row in test_level.level_data:
        print(" ".join(row))
