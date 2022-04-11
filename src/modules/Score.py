from src.modules.Coordinate import Coordinate
from src.modules.HUDElement import HUDElement


class Score(HUDElement):
    def __init__(
        self, value: int, font_path: str, font_size: int, coordinate: Coordinate
    ):
        super().__init__("SCORE", value, font_path, font_size, coordinate)

    def reset(self):
        self.value = 0
