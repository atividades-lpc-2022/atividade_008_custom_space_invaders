from src.modules.Coordinate import Coordinate
from src.modules.HUDElement import HUDElement


class Life(HUDElement):
    def __init__(
        self,
        title: str,
        value: int,
        font_path: str,
        font_size: int,
        coordinate: Coordinate,
        max_life: int,
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        super().__init__(title, value, font_path, font_size, coordinate, color)
        self.max_life = max_life

    def reset(self):
        self.value = self.max_life
