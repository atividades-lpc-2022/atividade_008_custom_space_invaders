import pygame
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen
from modules.Speed import Speed


class Brick(Element):
    def __init__(
        self,
        coordinate: Coordinate,
        dimension: Dimension,
        image_path: str,
        speed: Speed,
        hits: int,
        damage: int,
    ):
        super().__init__(coordinate, dimension, image_path)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.hits = hits
        self.damage = damage
        
        
    def update_hits(self, hits: int = 1):
        self.hits += hits
        
    def update_sprite(self, image_path):
        self.image = pygame.image.load(image_path)
        

    def draw(self, screen: Screen):
        self.coordinate.y += self.speed.y_speed
        self.rect = self.image.get_rect(center=(self.coordinate.x, self.coordinate.y))
        screen.surface.blit(self.image, self.rect)
