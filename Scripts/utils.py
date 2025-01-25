"""
MODULE FOR GENERAL UTILITIES AND FUNCTIONS:
- Text class
- Button class
"""
import pygame
import os
pygame.init()

PATH_TO_FONT = os.getcwd() + "/Assets/Fonts/"

class Text:
    def __init__(self, text: str, size: int, coords: (int, int), surf: pygame.Surface, colour: (int, int, int) = (0, 0, 0), font: str = "ExtraBeige-2vGeW.ttf") -> None:
        """ Initialises a text object

        :param text: The text to be displayed
        :param size: The size of the text
        :param coords: The position of the text, passed in as a percentage, to be converted to actual pixel values
        :param surf: The surface to render the text to
        :param colour: The colour of the text, passed as an RGB value
        :param font: The font to use, just the file name, as the file path will be attached bellow
        """
        # Error handling: ensure font can be found and created
        try:
            self.surface = surf
            self.colour = colour
            self.font_addr = PATH_TO_FONT + font  # Create full font address
            self.font_obj = pygame.font.Font(self.font_addr, size)  # Create an object of the target font

            # Create the text object and get the rect of it
            self.text_obj = self.font_obj.render(text, True, colour)
            self.text_rect = self.text_obj.get_rect()
            self.coords = coords
            self.text_rect.topleft = self.coords

        except FileNotFoundError as e:
            print(f"ERROR: Unable to find font for text...\n{e}")

    def update_text(self, new_text: str) -> None:
        self.text_obj = self.font_obj.render(new_text, True, self.colour)
        self.text_rect = self.text_obj.get_rect()

    def out(self):
        self.surface.blit(self.text_obj, self.text_rect)
