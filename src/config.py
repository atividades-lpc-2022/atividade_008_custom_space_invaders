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
        "bomb4": 'src/img/bomb4.png'
    }

    SOUND = {
        'shot': '',
        'collision': ''
    }
