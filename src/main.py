import pygame

from src.game import Game


class Main:
    def __init__(self, game: Game):
        self.game = game

    def init(self):
        self.game.loop()
