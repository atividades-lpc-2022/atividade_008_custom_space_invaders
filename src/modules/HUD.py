from typing import Sequence
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.HUDElement import HUDElement
from modules.Screen import Screen


class HUD(Element):
    def __init__(self, coordinate: Coordinate, dimension: Dimension):
        super().__init__(coordinate, dimension)

    def __draw_hud_element__(self, element: HUDElement):
        print("[HUD > HUD Element] Drawing...")

    def draw(self, screen: Screen, elements: Sequence[HUDElement]):
        print("[HUD] Drawing...")
        for element in elements:
            self.__draw_hud_element__(element)
