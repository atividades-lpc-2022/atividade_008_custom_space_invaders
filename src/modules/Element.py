import pygame

from modules.Coordinate import Coordinate
from modules.Dimension import Dimension


class Element(pygame.sprite.Sprite):
    def __init__(self, coordinate: Coordinate, dimension: Dimension):
        pygame.sprite.Sprite.__init__(self)
        self.coordinate = coordinate
        self.dimension = dimension
