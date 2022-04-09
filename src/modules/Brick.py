from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen
from modules.Speed import Speed


class Brick(Element):
    def __init__(
        self,
        coordinate: Coordinate,
        dimension: Dimension,
        level: int,
        image_path: str,
        speed: Speed,
        hits: int,
        damage: int,
    ):
        super().__init__(coordinate, dimension)
        self.level = level
        self.image = image_path
        self.speed = speed
        self.hits = hits
        self.damage = damage

    def draw(self, screen: Screen):
        # print("[Brick] Drawing..")
        pass
