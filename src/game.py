from typing import Sequence

import pygame

from config import Config
from modules.Aim import Aim
from modules.Brick import Brick
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.HUD import HUD
from modules.Life import Life
from modules.Score import Score
from modules.Screen import Screen
from modules.Speed import Speed
from modules.Tank import Tank
from modules.Bullet import Bullet


class Game:
    def __init__(self, config: Config):
        self.config = config
        self.screen = Screen(
            config.TITLE, Dimension(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        )
        self.tank = Tank(Coordinate(400, 515), Dimension(59, 63), self.config.IMAGE['tank'])
        self.bricks: Sequence[Brick] = []
        self.bullets: Sequence[Bullet] = []
        self.hud = HUD(Coordinate(0, 0), Dimension(0, 0))
        self.aim = Aim(Coordinate(0, 0), Dimension(0, 0), self.config.IMAGE['aim'])
        self.score = Score(0, None, 32, Coordinate(0, 0))
        self.life = Life(100, None, 32, Coordinate(0, 0), 100)
        
        self.is_running = True

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = self.tank.fire(None, Speed(4, 4))
                self.bullets.append(bullet)
                print(f'{self.bullets}')
                

    def process(self):
        for b in self.bullets[:]:
            b.update()
            if b.coordinate[0] < 5 or b.coordinate[0] > self.screen.dimension.width \
                or b.coordinate[1] < 5 or b.coordinate[1] > self.screen.dimension.height:
                self.bullets.remove(b)
            
            
    def draw(self):
        self.screen.draw(self.config.IMAGE['bg'])
        self.hud.draw(self.screen, [self.life, self.score])
        self.aim.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        self.tank.draw(self.screen)

        for brick in self.bricks:
            brick.draw(self.screen)

    def loop(self):
        pygame.init()
        clock = pygame.time.Clock()

        while self.is_running:
            self.input()
            self.process()
            self.draw()

            pygame.display.update()
            clock.tick(60)
