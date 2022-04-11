from src.config import Config
from src.game import Game
from src.main import Main

main = Main(Game(Config()))
main.run()
