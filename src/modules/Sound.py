from pygame import mixer


mixer.init(frequency=44100, size=-16, channels=7, buffer=512)


class Sound:
    def __init__(self):
        self.current_sound = ""

    def __channel__(self, num: int):
        name = mixer.Channel(num)
        return name

    def play(self, channel: int, sound: str, vol: float):
        self.current_sound = mixer.Sound(sound)
        self.__channel__(channel).set_volume(vol)
        self.__channel__(channel).play(self.current_sound)
    
    def music(self, music: str):
        mixer.music.load(music)
        mixer.music.play(-1)
