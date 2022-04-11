import pygame
import random

from src.config import Config
from src.modules.Aim import Aim
from src.modules.Brick import Brick
from src.modules.Coordinate import Coordinate
from src.modules.Dimension import Dimension
from src.modules.Explosion import Explosion
from src.modules.HUD import HUD
from src.modules.Life import Life
from src.modules.Score import Score
from src.modules.Screen import Screen
from src.modules.Speed import Speed
from src.modules.Tank import Tank
from src.modules.Bullet import Bullet
from src.modules.Sound import Sound



class Game:
    def __init__(self, config: Config):
        self.config = config
        self.screen = Screen(
            config.TITLE,
            Dimension(config.SCREEN_WIDTH, config.SCREEN_HEIGHT),
            self.config.IMAGE["home"],
            self.config.IMAGE["icon"],
        )
        self.tank = Tank(
            Coordinate(400, 515), Dimension(59, 63), self.config.IMAGE["tank"]
        )
        self.bricks: list[Brick] = []
        self.bullets: list[Bullet] = []
        self.explosions: list[Explosion] = []
        self.hud = HUD()
        self.aim = Aim(Coordinate(0, 0), Dimension(0, 0), self.config.IMAGE["aim"])
        self.life = Life(
            "HP",
            100,
            self.config.FONT_FAMILY,
            32,
            Coordinate(self.config.SCREEN_WIDTH * 0.2, 30),
            100,
        )
        self.score = Score(
            "SCORE",
            0,
            self.config.FONT_FAMILY,
            32,
            Coordinate(self.config.SCREEN_WIDTH * 0.8, 30),
        )
        self.final_score = Score(
            "SCORE",
            self.score.value,
            self.config.FONT_FAMILY,
            32,
            Coordinate(self.config.SCREEN_WIDTH * 0.5, self.config.SCREEN_HEIGHT * 0.5),
        )
        self.high_score = Score(
            "HIGHSCORE",
            self.config.get_high_score(),
            self.config.FONT_FAMILY,
            32,
            Coordinate(self.config.SCREEN_WIDTH * 0.5, self.config.SCREEN_HEIGHT * 0.6),
            (217, 212, 82)
        )
        self.scene = self.config.SCENE["home"]
        self.is_running = True
        self.sound = Sound()
        self.last_tick = pygame.time.get_ticks()
        self.cooldown = 3000

    def __stop__(self):
        self.is_running = False

    def __reset__(self):
        self.score.reset()
        self.life.reset()
        self.bricks = []
        self.bullets = []
        self.screen.change_background(self.config.IMAGE["home"])

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__stop__()
            if (
                self.scene == self.config.SCENE["game"]
                and event.type == pygame.MOUSEBUTTONDOWN
                and len(self.bullets) < 4
            ):
                bullet = self.tank.fire(Speed(6, 6), self.config.IMAGE["shot"])
                self.bullets.append(bullet)
                self.sound.play(0, self.config.SOUND["shot"], 1.0)
            if (
                self.scene == self.config.SCENE["gameover"]
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.__reset__()
                self.scene = self.config.SCENE["home"]

    def process(self):
        if self.life.value <= 0:
            if self.config.get_high_score() < self.score.value:
                self.config.set_high_score(self.score.value)
            self.screen.change_background(self.config.IMAGE["gameover"])
            self.hud = HUD()
            self.final_score.value = self.score.value
            self.scene = self.config.SCENE["gameover"]

        if self.scene == self.config.SCENE["game"]:
            bombs = ["bomb1", "bomb2", "bomb3", "bomb4"]
            now = pygame.time.get_ticks()
            bomb_hits = random.randint(0, 3)

            if now - self.last_tick >= self.cooldown:
                self.last_tick = now
                brick = Brick(
                    Coordinate(random.randint(20, Config.SCREEN_WIDTH - 20), 0),
                    Dimension(16, 32),
                    Config.IMAGE[bombs[bomb_hits]],
                    Speed(0, 0.5 + (0.01 * self.score.value) - (0.1 * bomb_hits)),
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
                        if brick.hits > 0:
                            self.sound.play(1, self.config.SOUND["hit"], 0.4)
                        if brick.hits <= 0:
                            self.sound.play(2, self.config.SOUND["explosion_air"], 0.4)
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
                    self.sound.play(3, self.config.SOUND["explosion"], 0.4)

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
        if self.scene == self.config.SCENE["game"]:
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
        elif self.scene == self.config.SCENE["gameover"]:
            self.screen.draw()
            self.hud.draw(self.screen, [self.final_score, self.high_score])

    def loop(self):
        pygame.init()
        if self.life.value > 0: self.sound.music(self.config.MUSIC['music_loop'])
        clock = pygame.time.Clock()
        while self.is_running:
            self.input()
            self.process()
            self.draw()
            pygame.display.update()
            clock.tick(60)
