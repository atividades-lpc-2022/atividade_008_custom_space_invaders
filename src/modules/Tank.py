import pygame, math

from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Element import Element
from modules.Screen import Screen
from modules.Bullet import Bullet
from modules.Speed import Speed


class Tank(Element):
    def __init__(
        self,
        coordinate: Coordinate,
        dimension: Dimension,
        image_path,
    ):
        super().__init__(coordinate, dimension)
        self.initial_angle = 90
        self.image = image_path
        self.img_rect = self.image.get_rect(center = (coordinate.x, coordinate.y))
        self.initial_angle = 90
        self.mx = 0
        self.my = 0
        self.dx = 0
        self.dy = 0
        self.angle = 0

    def rotate(self):
        self.mx, self.my = pygame.mouse.get_pos()
        self.dx = self.mx - self.img_rect.centerx 
        self.dy = self.my - self.img_rect.centery
        self.angle = math.degrees(math.atan2(-self.dy, self.dx)) - self.initial_angle
        rotated_img = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_img.get_rect(center = self.img_rect.center)
        
        return rotated_img, rotated_rect

    def fire(self, target: Element, speed: Speed) -> Bullet:
        return Bullet(self.coordinate, Dimension(16, 16), speed, self.angle, (self.dx, self.dy))

    def draw(self, screen: Screen):
        rotated, rect = self.rotate()
        screen.surface.blit(rotated, rect.topleft)
