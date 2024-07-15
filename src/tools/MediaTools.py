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



if __name__ == "__main__":
    MediaChecker.getPlatformFromUrl("https://www.youtube.com/watch?v=K8Gc5ys5Ba8")