import pygame
from src.modules.Coordinate import Coordinate
from src.modules.Dimension import Dimension
from src.modules.Element import Element
from src.modules.Screen import Screen


class Explosion(Element):
    def __init__(
        self,
        coordinate: Coordinate,
        dimension: Dimension,
        image_path: str,
        cooldown: int,
    ):
        super().__init__(coordinate, dimension, image_path)
        self.image = pygame.image.load(image_path)
        self.frame = 1
        self.last_tick = pygame.time.get_ticks()
        self.cooldown = cooldown

    def draw(self, screen: Screen):
        now = pygame.time.get_ticks()
        if now - self.last_tick >= self.cooldown:
            screen.surface.blit(
                self.image,
                self.image.get_rect(center=(self.coordinate.x, self.coordinate.y)),
            )
            self.last_tick = now
            self.frame += 1
            self.image_path = str(self.image_path).replace(
                f"{self.frame - 1}.png", f"{self.frame}.png"
            )
            self.image = pygame.image.load(self.image_path)
