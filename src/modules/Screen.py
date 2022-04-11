import pygame
from src.modules.Dimension import Dimension


class Screen:
    def __init__(self, title: str, dimension: Dimension, image_path: str, icon: str):
        self.image_path = image_path
        self.dimension = dimension
        self.surface = pygame.display.set_mode((dimension.width, dimension.height))
        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load(icon))

    def change_background(self, new_image_path: str):
        self.image_path = new_image_path

    def draw(self):
        self.surface.blit(pygame.image.load(self.image_path), (0, 0))
