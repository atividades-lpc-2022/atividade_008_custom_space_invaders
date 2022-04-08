from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element


class HUDElement(Element):
    def __init__(
        self, value: int, font_path: str, font_size: int, coordinate: Coordinate
    ):
        super().__init__(
            coordinate, Dimension(coordinate.x + font_size, coordinate.y + font_size)
        )
        self.value = value
        self.font = font_path
        self.font_size = font_size
