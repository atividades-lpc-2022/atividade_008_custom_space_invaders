from src.game import Game


class Main:
    def __init__(self, game: Game):
        self.game = game

    def run(self):
        self.game.loop()
