import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)


class Sound:
    def __init__(self):
        self.current_sound = None

    def channel(self, num):
        name = pygame.mixer.Channel(num)
        return name

    def play(self, channel: int, sound: str, vol: float):
        self.current_sound = pygame.mixer.Sound(sound)
        self.channel(channel).set_volume(vol)
        self.channel(channel).play(self.current_sound)
