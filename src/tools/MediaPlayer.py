import os
from src.actions.ActionProtocol import *
from src.tools.Downloaders import YoutubeDownloader

import pygame
from pygame import mixer
import time

# protocol
class AudioPlayerProtocol(ActionPermission):

    def play(self, music_url):
        print("Error the subclass as not instancied this method")

    def stop(self):
        print("Error the subclass as not instancied this method")

    def resume(self):
        print("Error the subclass as not instancied this method")

    def pause(self):
        print("Error the subclass as not instancied this method")
    
    def goTo(self, timestamp):
        print("Error the subclass as not instancied this method")

class GenericAudioPlayer(AudioPlayerProtocol):

    def __init__(self):
        self.playback = mixer
        self.playback.init()

    def play(self, music_data):
        # Set Volume to 1
        print(self.playback.music.get_volume())
        self.playback.music.set_volume(1)
        # Load song
        try:
            self.playback.music.load(music_data)  # Remplacez par le chemin de votre fichier
            print("Music file loaded successfully.")
        except pygame.error as e:
            print(f"Error loading music file: {e}")

        # play song
        try:
            self.playback.music.play()
        except pygame.error as e:
            print(f"Error playing music: {e}")
        # Attendre la fin de la musique pour éviter que le programme ne se termine immédiatement
        while self.playback.music.get_busy():
            pygame.time.Clock().tick(10)

    def stop(self):
        self.playback.music.stop()

    def resume(self):
        self.playback.music.resume()

    def pause(self):
        self.playback.music.pause()

    def goTo(self, timestamp):
        pass

class SonosAudioPlayer(AudioPlayerProtocol):

    def __init__(self):
        import soco
        self.device = soco.discovery.any_soco()

    def play(self, music_url):
        self.device.play()

    def stop(self):
        self.device.stop()

    def resume(self):
        print("Error the subclass as not instancied this method")

    def pause(self):
        print("Error the subclass as not instancied this method")
    
    def goTo(self, timestamp):
        print("Error the subclass as not instancied this method")