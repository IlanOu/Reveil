import os
from src.base.Enumerator import *

class MediaChecker():

    @staticmethod
    def isFileExist(filePath:str):
        if os.path.isfile(filePath):
            return True
        else:
            return False
    
    @staticmethod
    def isUrl(url:str):
        if url[:4] == "http":
            return True
        else:
            return False
    
    @staticmethod
    def getPlatformFromUrl(url:str):
        if PLATFORM.YOUTUBE.lower() in url:
            return PLATFORM.YOUTUBE
        elif PLATFORM.SPOTIFY.lower() in url:
            return PLATFORM.SPOTIFY
        else:
            print("Error : no platform match with the url")
            return None


class PlaylistPicker():

    def __init__(self) -> None:
        pass

    def getRandomUrl(self, urlPlaylist, platform):
        match(platform):
            case PLATFORM.YOUTUBE:
                YoutubePlaylistPicker().getRandomUrl(urlPlaylist)
            case PLATFORM.SPOTIFY:
                SpotifyPlaylistPicker().getRandomUrl(urlPlaylist)
            case _:
                print("Platform is not available")

    def getAllUrl(self, urlPlaylist, platform):
        match(platform):
            case PLATFORM.YOUTUBE:
                YoutubePlaylistPicker().getAllUrl(urlPlaylist)
            case PLATFORM.SPOTIFY:
                SpotifyPlaylistPicker().getAllUrl(urlPlaylist)
            case _:
                print("Platform is not available")

# ------------------------- Playlist picker platform ------------------------- #
# Protocol
class PlaylistPickerProtocol():

    def getRandomUrl(self, urlPlaylist, platform):
        pass

    def getAllUrl(self, urlPlaylist, platform):
        pass

# Platform Picker
class YoutubePlaylistPicker(PlaylistPickerProtocol):

    def __init__(self) -> None:
        pass

    def getRandomUrl(self, urlPlaylist, platform):
        pass

    def getAllUrl(self, urlPlaylist, platform):
        pass

class SpotifyPlaylistPicker(PlaylistPickerProtocol):

    def __init__(self) -> None:
        pass

    def getRandomUrl(self, urlPlaylist, platform):
        pass

    def getAllUrl(self, urlPlaylist, platform):
        pass


if __name__ == "__main__":
    MediaChecker.getPlatformFromUrl("https://www.youtube.com/watch?v=K8Gc5ys5Ba8")