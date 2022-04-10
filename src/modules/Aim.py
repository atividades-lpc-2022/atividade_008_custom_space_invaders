import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen


class Aim(Element):
    def __init__(self, coordinate: Coordinate, dimension: Dimension, image_path: str):
        super().__init__(coordinate, dimension, image_path)
        self.image = pygame.image.load(image_path)

    def draw(self, screen: Screen):
        pygame.mouse.set_visible(False)
        x, y = pygame.mouse.get_pos()
        self.coordinate.x = x - self.dimension.width / 2
        self.coordinate.y = y - self.dimension.height / 2
        screen.surface.blit(
            self.image,
            (self.coordinate.x, self.coordinate.y),            
        )
