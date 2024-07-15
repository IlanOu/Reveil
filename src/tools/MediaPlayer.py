import os
from src.actions.ActionProtocol import *
from src.tools.Downloaders import YoutubeDownloader

from just_playback import Playback

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
    
    def gotTo(self, timestamp):
        print("Error the subclass as not instancied this method")

class GenericAudioPlayer(AudioPlayerProtocol):

    def __init__(self):
        self.playback = Playback()

    def play(self, music_data):
        self.playback.load_file(music_data)
        self.playback.play()

    def stop(self):
        self.playback.stop()

    def resume(self):
        self.playback.resume()

    def pause(self):
        self.playback.pause()

    def gotTo(self, timestamp):
        pass

