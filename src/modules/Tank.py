import math
import pygame

from src.modules.Bullet import Bullet
from src.modules.Coordinate import Coordinate
from src.modules.Dimension import Dimension
from src.modules.Element import Element
from src.modules.Screen import Screen
from src.modules.Speed import Speed


class Tank(Element):
    def __init__(
        self,
        coordinate: Coordinate,
        dimension: Dimension,
        image_path: str,
    ):
        super().__init__(coordinate, dimension, image_path)
        self.initial_angle = 90
        self.image = pygame.image.load(image_path)
        self.img_rect = self.image.get_rect(center=(coordinate.x, coordinate.y))
        self.dx = 0
        self.dy = 0
        self.angle = 0

    def rotate(self):
        x, y = pygame.mouse.get_pos()
        self.dx = x - self.img_rect.centerx
        self.dy = y - self.img_rect.centery
        self.angle = math.degrees(math.atan2(-self.dy, self.dx)) - self.initial_angle
        rotated_img = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_img.get_rect(center=self.img_rect.center)

        return rotated_img, rotated_rect

    def fire(self, speed: Speed, bullet_image_path: str) -> Bullet:
        return Bullet(
            Coordinate(self.coordinate.x, self.coordinate.y),
            Dimension(16, 16),
            Speed(speed.x_speed, speed.y_speed),
            self.angle,
            (self.dx, self.dy),
            bullet_image_path,
        )

    def draw(self, screen: Screen):
        rotated, rect = self.rotate()
        screen.surface.blit(rotated, rect.topleft)
