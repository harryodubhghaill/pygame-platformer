import pygame
from tiles import Tiles

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data