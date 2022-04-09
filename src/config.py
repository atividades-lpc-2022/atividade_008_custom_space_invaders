import pygame

class Config:
    TITLE = (
        "Custom Space Invaders - Gabriel Da Silva, Gabriel Dos Santos e Melinne Diniz"
    )
    SCREEN_WIDTH = 800  # TODO: Define screen size
    SCREEN_HEIGHT = 600  # TODO: Define screen size
    TOLERANCE = 5 # valor prox de 0 para x, y da bullet sumir

    IMAGE = {
        "tank": pygame.image.load('src/img/tank2.png'),
        "aim": pygame.image.load('src/img/sight2.png'),
        "bg": pygame.image.load('src/img/background.png'),
        "shot": pygame.image.load('src/img/shot2.png'),
        "missile": pygame.image.load('src/img/missile2.png')
    }



