from pytubefix import YouTube
from src.base.Enumerator import *
import os
from moviepy.editor import *

class DownloaderProtocol():
    def downloadFromUrl(self, url): print("Error : class as not instancied this method")
    def downloadFromName(self, name): print("Error : subclass as not instancied this method")
    def downloadFromUnknowSource(self, data): pass

class YoutubeDownloader(DownloaderProtocol):

    def __init__(self, pathAudioFolder = "assets/audiosDownloaded/") -> None:
        self.pathAudioFolder = pathAudioFolder

    def downloadFromUrl(self, url):
        try:

            yt = YouTube(url) # , use_oauth=False, allow_oauth_cache=True
            stream = yt.streams.get_highest_resolution() #.filter(only_audio=True).first()
            # print(dir(yt))
            downloaded_file = self.pathAudioFolder + yt.title + '.mp4'
            mp3_file = self.pathAudioFolder + yt.title + '.mp3'
        
            if os.path.exists(mp3_file):
                print("Le fichier existe déjà")
                return mp3_file
            else:
                print('Téléchargement de la musique...')
                stream.download(output_path=self.pathAudioFolder)
                print('Téléchargement de la musique terminé.')

                try:
                    print('Convertion de la musique...')
                    video = VideoFileClip(downloaded_file)
                    video.audio.write_audiofile(mp3_file)
                    print('Convertion de la musique terminé.')
                    return mp3_file
                except Exception as e:
                    print('Convertion erreur : ', str(e))

        except Exception as e:
            print('Youtube download erreur : ', str(e))

    def downloadFromUnknowSource(self, data):
        pass # TODO check if url or name


class SpotifyDownloader(DownloaderProtocol):

    def __init__(self, pathAudioFolder = "assets/audiosDownloaded/") -> None:
        self.pathAudioFolder = pathAudioFolder

    def downloadFromUrl(self, url):
        try:
           pass
        except Exception as e:
            pass


# ---------------------------------------------------------------------------- #
#                                 class Manager                                #
# ---------------------------------------------------------------------------- #
class AudioDownloaderManager():

    def __init__(self, savePath = "assets/audiosDownloaded/") -> None:
        self.savePath = savePath

    def changeSavePath(self, newPath):
        self.savePath = newPath
    
    def download(self, audioUrl, platform):

        match(platform):
            case PLATFORM.YOUTUBE:
                return YoutubeDownloader(self.savePath).downloadFromUrl(audioUrl)
            case PLATFORM.SPOTIFY:
                return SpotifyDownloader(self.savePath).downloadFromName(audioUrl)
            case _:
                print("Platform is not available")
                return None

if __name__ == "__main__":
    AudioDownloaderManager("assets/audiosDownloaded/").download("https://youtu.be/9bZkp7q19f0", PLATFORM.YOUTUBE)
    