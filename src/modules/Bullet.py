from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen
from modules.Speed import Speed


class Bullet(Element):
    def __init__(
        self, coordinate: Coordinate, dimension: Dimension, speed: Speed, angle: float
    ):
        super().__init__(coordinate, dimension)
        self.speed = speed
        self.angle = angle

    def draw(self, screen: Screen):
        print("[Bullet] Drawing...")
