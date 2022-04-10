class Config:
    TITLE = (
        "Custom Space Invaders - Gabriel Da Silva, Gabriel Dos Santos e Melinne Diniz"
    )
    SCREEN_WIDTH = 800  # TODO: Define screen size
    SCREEN_HEIGHT = 600  # TODO: Define screen size
    POINTS = 1

    FONT_FAMILY = 'src/fonts/PressStart2P.ttf'
    
    COLORS = {
        "white": (255, 255, 255)
    }

    IMAGE = {
        "tank": 'src/img/tank2.png',
        "aim": 'src/img/sight2.png',
        "bg": 'src/img/background.png',
        "shot": 'src/img/shot2.png',
        "bomb1": 'src/img/bomb1.png',
        "bomb2": 'src/img/bomb2.png',
        "bomb3": 'src/img/bomb3.png',
        "bomb4": 'src/img/bomb4.png',
        "explosion1": 'src/img/explosion1.png',
        "explosion2": 'src/img/explosion2.png',
        "explosion3": 'src/img/explosion3.png',
        "explosion4": 'src/img/explosion4.png',
        "explosion5": 'src/img/explosion5.png',
        "explosion6": 'src/img/explosion6.png',
        "explosion7": 'src/img/explosion7.png',
        "explosion8": 'src/img/explosion8.png',
    }

    SOUND = {
        'shot': '',
        'collision': ''
    }
