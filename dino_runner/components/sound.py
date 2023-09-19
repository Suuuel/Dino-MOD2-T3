import random
import pygame

from dino_runner.utils.constants import SOUND, JUMP_SOUND, DEATH_SOUND, EGGS_DINO

class Music:
    def __init__(self):
        pygame.mixer.init()

    def play_music(self):
        self.musics = random.choice(SOUND)
        pygame.mixer.music.load(self.musics)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1)

    def play_sound(self, sound, volume):
        self.sons = pygame.mixer.Sound(sound)
        self.sons.set_volume(volume)
        self.sons.play()

    def music_Jump():
        jump = pygame.mixer.Sound(JUMP_SOUND)
        jump.play()

    def music_death():
        death = pygame.mixer.Sound(DEATH_SOUND)
        death.play()
    
    def music_power_up():
        eggs = pygame.mixer.Sound(EGGS_DINO)
        eggs.play()
        
    def stop_music():
        pygame.mixer.music.stop()
      