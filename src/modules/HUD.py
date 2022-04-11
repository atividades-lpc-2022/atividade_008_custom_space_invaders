from src.modules.HUDElement import HUDElement
from src.modules.Screen import Screen


class HUD:
    def draw(self, screen: Screen, elements: list[HUDElement]):
        for element in elements:
            element.draw(screen)
