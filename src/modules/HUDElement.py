from src.modules.Coordinate import Coordinate
from src.modules.Dimension import Dimension
from src.modules.Element import Element


class HUDElement:
    def __init__(
        self,
        title: str,
        value: int,
        font_path: str,
        font_size: int,
        coordinate: Coordinate,
    ):
        self.coordinate = coordinate
        self.value = value
        self.font_path = font_path
        self.font_size = font_size
        self.title = title

    def update(self, value: int = 1):
        self.value += value
