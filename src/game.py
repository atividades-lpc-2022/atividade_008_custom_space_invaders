import pygame
import random

from config import Config
from modules.Aim import Aim
from modules.Brick import Brick
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.Explosion import Explosion
from modules.HUD import HUD
from modules.Life import Life
from modules.Score import Score
from modules.Screen import Screen
from modules.Speed import Speed
from modules.Tank import Tank
from modules.Bullet import Bullet
from modules.Sound import Sound


class Game:
    pygame.display.set_icon(pygame.image.load('src\img\icon.png'))
    
    def __init__(self, config: Config):
        self.config = config
        self.screen = Screen(
            config.TITLE,
            Dimension(config.SCREEN_WIDTH, config.SCREEN_HEIGHT),
            self.config.IMAGE["bg"],
        )
        self.tank = Tank(
            Coordinate(400, 515), Dimension(59, 63), self.config.IMAGE["tank"]
        )
        self.bricks: list[Brick] = []
        self.bullets: list[Bullet] = []
        self.explosions: list[Explosion] = []
        self.hud = HUD(Coordinate(0, 0), Dimension(self.config.SCREEN_WIDTH, 50))
        self.aim = Aim(Coordinate(0, 0), Dimension(0, 0), self.config.IMAGE["aim"])
        self.life = Life(
            100,
            self.config.FONT_FAMILY,
            32,
            Coordinate(self.config.SCREEN_WIDTH * 0.2, 30),
            100,
        )
        self.score = Score(
            0,
            self.config.FONT_FAMILY,
            32,
            Coordinate(self.config.SCREEN_WIDTH * 0.8, 30),
        )
        self.is_running = True
        self.sound = Sound()
        self.last_tick = pygame.time.get_ticks()
        self.cooldown = 3000

    def __stop__(self):
        self.is_running = False

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__stop__()
            if event.type == pygame.MOUSEBUTTONDOWN and len(self.bullets) < 4:
                bullet = self.tank.fire(Speed(6, 6), self.config.IMAGE["shot"])
                self.bullets.append(bullet)

    def process(self):
        bombs = ["bomb1", "bomb2", "bomb3", "bomb4"]
        now = pygame.time.get_ticks()
        bomb_hits = random.randint(0, 3)

        if now - self.last_tick >= self.cooldown:
            self.last_tick = now
            brick = Brick(
                Coordinate(random.randint(20, Config.SCREEN_WIDTH - 20), 0),
                Dimension(16, 32),
                Config.IMAGE[bombs[bomb_hits]],
                Speed(0, 0.2 + (0.01 * self.score.value)),
                bomb_hits + 1,
                (bomb_hits + 1) * 5,
            )
            self.cooldown -= 10
            self.bricks.append(brick)

        for explosion in self.explosions:
            if explosion.frame == 8:
                self.explosions.remove(explosion)

        for brick in self.bricks:
            for bullet in self.bullets:
                if bullet.collide(brick):
                    self.score.update(self.config.POINTS)
                    self.bullets.remove(bullet)
                    brick.update_hits(-1)
                    if brick.hits <= 0:
                        explosion = brick.explode(self.config.IMAGE["explosion1"])
                        self.explosions.append(explosion)
                        self.bricks.remove(brick)
                    else:
                        brick.update_sprite(Config.IMAGE[bombs[brick.hits - 1]])

        for brick in self.bricks:
            bottom_collision = (
                brick.coordinate.y + brick.dimension.height
                >= self.screen.dimension.height
            )
            if bottom_collision:
                explosion = brick.explode(self.config.IMAGE["explosion1"])
                self.explosions.append(explosion)
                self.life.update(-brick.damage)
                self.bricks.remove(brick)

        if self.life.value <= 0:
            # TODO: Game over scene
            self.__stop__()

        for bullet in self.bullets:
            bullet.update()
            if (
                bullet.coordinate.x < 5
                or bullet.coordinate.x > self.screen.dimension.width
                or bullet.coordinate.y < 5
                or bullet.coordinate.y > self.screen.dimension.height
            ):
                self.bullets.remove(bullet)

    def draw(self):
        self.screen.draw()
        self.hud.draw(self.screen, [self.score, self.life])
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
        for explosion in self.explosions:
            explosion.draw(self.screen)
        self.tank.draw(self.screen)
        self.aim.draw(self.screen)

    def loop(self):
        pygame.init()
        clock = pygame.time.Clock()
        while self.is_running:
            self.input()
            self.process()
            self.draw()
            pygame.display.update()
            clock.tick(60)
