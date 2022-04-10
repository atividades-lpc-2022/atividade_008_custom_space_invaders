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
            config.TITLE,
            Dimension(config.SCREEN_WIDTH, config.SCREEN_HEIGHT),
            self.config.IMAGE['bg']
        )
        self.tank = Tank(Coordinate(400, 515), Dimension(59, 63), self.config.IMAGE['tank'])
        self.bricks: list[Brick] = []
        self.bullets: list[Bullet] = []
        self.hud = HUD(Coordinate(0, 0), Dimension(self.config.SCREEN_WIDTH, 50))
        self.aim = Aim(Coordinate(0, 0), Dimension(0, 0), self.config.IMAGE['aim'])
        self.life = Life(100, self.config.FONT_FAMILY, 32, Coordinate(self.config.SCREEN_WIDTH * 0.2, 30), 100)
        self.score = Score(0, self.config.FONT_FAMILY, 32, Coordinate(self.config.SCREEN_WIDTH * 0.8, 30))
        self.is_running = True

    def __stop__(self):
        self.is_running = False

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__stop__()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(self.bullets) < 4:
                    bullet = self.tank.fire(Speed(6, 6), self.config.IMAGE['shot'])
                    self.bullets.append(bullet)

    def process(self):
        for brick in self.bricks:
            for bullet in self.bullets:
                if bullet.collide(brick):
                    self.score.update(self.config.POINTS)
                    self.bullets.remove(bullet)
                    brick.update_hits(-1)
                    if brick.hits <= 0:
                        self.bricks.remove(brick)

        for brick in self.bricks:
            bottom_collision = brick.coordinate.y + brick.dimension.height == self.screen.dimension.height
            if bottom_collision:
                self.life.update(-brick.damage)
                self.bricks.remove(brick)

        if self.life.value <= 0:
            # TODO: Game over scene
            self.__stop__()

        for bullet in self.bullets:
            bullet.update()
            if bullet.coordinate.x < 5 or bullet.coordinate.x > self.screen.dimension.width or \
                    bullet.coordinate.y < 5 or bullet.coordinate.y > self.screen.dimension.height:
                self.bullets.remove(bullet)

    def draw(self):
        self.screen.draw()
        self.hud.draw(self.screen, [self.score, self.life])
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
