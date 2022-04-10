import pygame
from modules.Dimension import Dimension


class Screen:
    def __init__(self, title: str, dimension: Dimension, image_path: str):
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.dimension = dimension
        self.surface = pygame.display.set_mode((dimension.width, dimension.height))
        pygame.display.set_caption(title)

    def draw(self):
        self.surface.blit(self.image, (0, 0))
