import pygame

from modules.Coordinate import Coordinate
from modules.Dimension import Dimension


class Element(pygame.sprite.Sprite):
    def __init__(self, coordinate: Coordinate, dimension: Dimension, image_path: str):
        pygame.sprite.Sprite.__init__(self)
        self.coordinate = coordinate
        self.dimension = dimension
        self.image_path = image_path

    def collide(self, element: "Element"):
        is_colliding = pygame.sprite.collide_rect(self, element)
        return is_colliding
