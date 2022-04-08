import pygame

class Config:
    TITLE = (
        "Custom Space Invaders - Gabriel Da Silva, Gabriel Dos Santos e Melinne Diniz"
    )
    SCREEN_WIDTH = 800  # TODO: Define screen size
    SCREEN_HEIGHT = 800  # TODO: Define screen size


    IMAGE = {
        "tank": pygame.image.load('img/tank2.png'),
        "aim": pygame.image.load('img/sight2.png'),
        "bg": pygame.image.load('img/background.png'),
        "shot": pygame.image.load('img/shot2.png'),
        "missile": pygame.image.load('img/missile2.png')
    }



