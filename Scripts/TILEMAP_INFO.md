# Tilemap Info
This file contains information about the tilemap used in the game.
## The tilemap and screen
The tilemap is 16x16, meaning that when paired with the standard 800x800 screen, each tile is 50 pixels squared.
This is a useful value, and provides flexibility with creating levels
## Creating levels
Levels will be stored as simple txt files, containing a 16x16 grid of integers, which will be read and converted to an array.
Each type of tile has a corresponding code, which is as follows:
- 0: Empty tile
- 1: Mud tile (i.e. Brown)
- 2: Grass tile (i.e. Green and brown)

## Accessing tiles
When a Level object is created, it creates a dictionary of tiles, with the key corresponding to each tile's code (see creating levels above).
## Debugging a level
If there are issues with the loading of a level, run level_manager.py with the level number at the end of the file to get a debug report that might help.