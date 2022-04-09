import math, pygame

from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen
from modules.Speed import Speed
from config import Config as cf


class Bullet(Element):
    def __init__(
        self, coordinate: Coordinate, dimension: Dimension, speed: Speed, angle: float, direct: tuple
    ):
        super().__init__(coordinate, dimension)
        self.coordinate = (coordinate.x, coordinate.y)
        self.speed = speed.get_speed()
        self.angle = angle
        self.euclidean = math.hypot(direct[0], direct[1])
        self.dir = (direct[0]/self.euclidean, direct[1]/self.euclidean)
        self.image = pygame.transform.rotate(cf.IMAGE['shot'], self.angle)


    def update(self):
        self.coordinate = (self.coordinate[0]+self.dir[0]*self.speed[0], \
            self.coordinate[1]+self.dir[1]*self.speed[1])
        # print(f'C: {self.coordinate[0]} + D: {self.dir[0]} * {self.speed[0]} = ')

    def draw(self, screen: Screen):
        rect = self.image.get_rect(center = self.coordinate)
        screen.surface.blit(self.image, rect)
