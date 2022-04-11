from config import Config
from game import Game


class Main:
    def __init__(self, game: Game):
        self.game = game

    def init(self):
        self.game.loop()


main = Main(Game(Config()))
main.init()