from src.tools.Downloaders import AudioDownloaderManager
from src.tools.MediaPlayer import GenericAudioPlayer
from src.tools.MediaTools import MediaChecker, PlaylistPicker

class MediaManager():

    def __init__(self, downloader=AudioDownloaderManager, mediaPlayer=GenericAudioPlayer, mediaChecker=MediaChecker, playlistPicker=PlaylistPicker) -> None:
        self.downloader = downloader()
        self.mediaPlayer = mediaPlayer()
        self.mediaChecker = mediaChecker
        self.playlistPicker = playlistPicker()

    def play(self, music_url):
        musicPath = self.getValidMedia(music_url)
        self.mediaPlayer.play(musicPath)


    def stop(self):
        self.mediaPlayer.stop()

    def resume(self):
        self.mediaPlayer.resume()

    def pause(self):
        self.mediaPlayer.pause()
    
    def goTo(self, timestamp):
        self.mediaPlayer.goTo(timestamp)

    def getValidMedia(self, data):
        # TODO get valid media of the player ( for don't download if it's unnecessary )
        if self.mediaChecker.isFileExist(data):
            # Play sound
            print("path : ", data)
            return data 
        else:
            # Try to download
            if self.mediaChecker.isUrl(data):
                platform = self.mediaChecker.getPlatformFromUrl(data)
                if platform != None:
                    path = self.downloader.download(data, platform)
                    return path
                else:
                    print("Error : wrong platform")
            else:
                print("Media is not valid")