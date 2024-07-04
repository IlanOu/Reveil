from src.actions.ActionProtocol import *

class YoutubeMusicPlayer(MusicPlayerProtocol):

    def __init__(self):
        pass

    def downloadMusic(self, music_url):
        print("I download the song : " + music_url + ". please wait ...")

    def play(self, music_url):
        self.downloadMusic(self, music_url)
        print(f"Je joue la musique : {music_url}")

    def stop(self):
        print("J'ai stoppé la musique !")