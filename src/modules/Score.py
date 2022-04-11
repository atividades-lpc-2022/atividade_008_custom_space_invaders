from src.modules.Coordinate import Coordinate
from src.modules.HUDElement import HUDElement


class Score(HUDElement):
    def __init__(
        self,
        title: str,
        value: int,
        font_path: str,
        font_size: int,
        coordinate: Coordinate,
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        super().__init__(title, value, font_path, font_size, coordinate, color)

    def reset(self):
        self.value = 0
