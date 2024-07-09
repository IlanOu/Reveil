import os
from src.actions.ActionProtocol import *
from src.tools.Downloaders import YoutubeDownloader

from just_playback import Playback

# protocol
class MusicPlayerProtocol(ActionPermission):

    def play(self, music_url):
        print("Error the subclass as not instancied this method")

    def stop(self):
        print("Error the subclass as not instancied this method")

    def resume(self):
        print("Error the subclass as not instancied this method")

    def pause(self):
        print("Error the subclass as not instancied this method")

class YoutubeMusicPlayer(MusicPlayerProtocol):

    def __init__(self):
        self.downloader = YoutubeDownloader()
        self.playback = Playback()

    def downloadMusic(self, music_data):
        pathOfmusic = self.downloader.downloadFromUnknowSource(music_data)
        return pathOfmusic

    def play(self, music_data):
        if os.path.isfile(music_data) == False:
            music_path = self.downloadMusic(music_data)
        else:
            music_path = music_data
        self.playback.load_file(music_path)
        self.playback.play()

    def stop(self):
        self.playback.stop()

    def resume(self):
        self.playback.resume()

    def pause(self):
        self.playback.pause()

