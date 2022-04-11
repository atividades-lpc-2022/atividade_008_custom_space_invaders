import pygame
from src.modules.Screen import Screen
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
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        self.coordinate = coordinate
        self.value = value
        self.font_path = font_path
        self.font_size = font_size
        self.title = title
        self.color = color

    def update(self, value: int = 1):
        self.value += value

    def draw(self, screen: Screen):
        font = pygame.font.Font(self.font_path, self.font_size)
        text = font.render(
            f"{self.title}: {self.value}", True, pygame.Color(*self.color)
        )
        text_rect = text.get_rect()
        text_rect.center = (self.coordinate.x, self.coordinate.y)
        screen.surface.blit(text, text_rect)
