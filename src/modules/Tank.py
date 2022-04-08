from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen
from modules.Bullet import Bullet
from modules.Speed import Speed


class Tank(Element):
    def __init__(
        self,
        coordinate: Coordinate,
        dimension: Dimension,
        angle: float,
        image_path: str,
    ):
        super().__init__(coordinate, dimension)
        self.angle = angle
        self.image = image_path

    def fire(self, target: Element, speed: Speed) -> Bullet:
        # Calculate angle from target coordinates
        return Bullet(self.coordinate, self.dimension, speed, self.angle)

    def draw(self, screen: Screen):
        print("[Tank] Drawing...")
