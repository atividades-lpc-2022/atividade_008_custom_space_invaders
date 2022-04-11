import math
import pygame

from src.modules.Coordinate import Coordinate
from src.modules.Dimension import Dimension
from src.modules.Element import Element
from src.modules.Screen import Screen
from src.modules.Speed import Speed


class Bullet(Element):
    def __init__(
        self,
        coordinate: Coordinate,
        dimension: Dimension,
        speed: Speed,
        angle: float,
        direct: tuple,
        image_path: str,
    ):
        super().__init__(coordinate, dimension, image_path)
        self.speed = speed
        self.angle = angle
        self.image = pygame.image.load(image_path)
        self.euclidean = math.hypot(direct[0], direct[1])
        if self.euclidean == 0.0:
            self.dir = (0, 0)
        else:
            self.dir = (direct[0] / self.euclidean, direct[1] / self.euclidean)
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()

    def update(self):
        self.coordinate.x = self.coordinate.x + self.dir[0] * self.speed.x_speed
        self.coordinate.y = self.coordinate.y + self.dir[1] * self.speed.y_speed

    def draw(self, screen: Screen):
        self.rect = self.image.get_rect(center=(self.coordinate.x, self.coordinate.y))
        screen.surface.blit(self.image, self.rect)
