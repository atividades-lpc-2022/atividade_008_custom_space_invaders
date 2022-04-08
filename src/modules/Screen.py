import pygame
from modules.Dimension import Dimension


class Screen:
    def __init__(self, title: str, dimension: Dimension):
        self.dimension = dimension
        self.surface = pygame.display.set_mode((dimension.width, dimension.height))
        pygame.display.set_caption(title)

    def draw(self):
        self.surface.fill(pygame.Color(0, 0, 0))
        print("[Screen] Drawing...")
