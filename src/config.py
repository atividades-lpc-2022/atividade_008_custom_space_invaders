import json


class Config:
    TITLE = (
        "Imminent Doomsday - Gabriel Da Silva, Gabriel Dos Santos e Melinne Diniz"
    )
    SCREEN_WIDTH = 800  # TODO: Define screen size
    SCREEN_HEIGHT = 600  # TODO: Define screen size
    POINTS = 1

    FONT_FAMILY = "src/fonts/PressStart2P.ttf"
    LOCAL_DATA_PATH = "src/local_data.json"

    COLORS = {"white": (255, 255, 255)}

    IMAGE = {
        "icon": "src/img/icon.png",
        "tank": "src/img/tank2.png",
        "aim": "src/img/sight2.png",
        "bg": "src/img/background.png",
        "shot": "src/img/shot2.png",
        "bomb1": "src/img/bomb1.png",
        "bomb2": "src/img/bomb2.png",
        "bomb3": "src/img/bomb3.png",
        "bomb4": "src/img/bomb4.png",
        "explosion1": "src/img/explosion1.png",
        "explosion2": "src/img/explosion2.png",
        "explosion3": "src/img/explosion3.png",
        "explosion4": "src/img/explosion4.png",
        "explosion5": "src/img/explosion5.png",
        "explosion6": "src/img/explosion6.png",
        "explosion7": "src/img/explosion7.png",
        "explosion8": "src/img/explosion8.png",
    }

    SOUND = {
        "hit": "src/sound/hit.ogg", 
        "explosion_air": "src/sound/explode_air.ogg",
        "explosion": "src/sound/explode_floor.ogg",
        "shot": "src/sound/shot.ogg", 
        "game_over": "src/sound/GameOver.ogg"
    }

    MUSIC = {
        "music_loop": "src/sound/wargames_defcon_track5.ogg",
    }

    def __get_local_data__(self) -> dict:
        with open(self.LOCAL_DATA_PATH, 'r') as local_data_file:
            local_data = json.load(local_data_file)
        return local_data

    def get_high_score(self) -> int:
        local_data = self.__get_local_data__()
        return local_data['high_score']

    def set_high_score(self, new_high_score: int):
        local_data = self.__get_local_data__()
        local_data['high_score'] = new_high_score
        
        new_local_data = json.dumps(local_data, indent = 4)
        
        with open(self.LOCAL_DATA_PATH, 'w') as local_data_file:
            local_data_file.write(new_local_data)
