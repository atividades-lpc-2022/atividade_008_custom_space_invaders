from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen


class Aim(Element):
    def __init__(self, coordinate: Coordinate, dimension: Dimension, image_path: str):
        super().__init__(coordinate, dimension)
        self.image = image_path

    def draw(self, screen: Screen):
        print("[Aim] Drawing...")
