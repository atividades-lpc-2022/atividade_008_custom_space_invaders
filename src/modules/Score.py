from modules.Coordinate import Coordinate
from modules.HUDElement import HUDElement


class Score(HUDElement):
    def __init__(self, value: int, font: str, font_size: int, coordinate: Coordinate):
        super().__init__(value, font, font_size, coordinate)

    def reset(self):
        self.value = 0
