import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.HUDElement import HUDElement
from modules.Screen import Screen


class HUD:
    def __init__(self, coordinate: Coordinate, dimension: Dimension):
        self.coordinate = coordinate
        self.dimension = dimension
        
    def __draw_hud_element__(self, screen: Screen, element: HUDElement):
        font = pygame.font.Font(element.font_path, element.font_size)
        text = font.render(f'{element.title}: {element.value}', True, pygame.Color(255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (element.coordinate.x, element.coordinate.y)
        screen.surface.blit(text, text_rect)

    def draw(self, screen: Screen, elements: list[HUDElement]):
        for element in elements:
            self.__draw_hud_element__(screen, element)
