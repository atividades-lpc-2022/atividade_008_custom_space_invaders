from modules.Coordinate import Coordinate
from modules.HUDElement import HUDElement


class Life(HUDElement):
    def __init__(
        self,
        value: int,
        font_path: str,
        font_size: int,
        coordinate: Coordinate,
        max_life: int,
    ):
        super().__init__("HP", value, font_path, font_size, coordinate)
        self.max_life = max_life

    def reset(self):
        self.value = self.max_life
