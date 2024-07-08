from pytube import YouTube
import os


class YoutubeDownloader():

    def __init__(self, pathAudioFolder = "/assets/audiosDownloaded/") -> None:
        self.pathAudioFolder = pathAudioFolder

    def downloadFromUrl(self, url):
        try:
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
            stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

            # print(dir(yt))
            downloaded_file = self.pathAudioFolder + '/' + yt.title + '.mp4'
            mp3_file = self.pathAudioFolder + '/' + yt.title + '.mp3'
        
            if os.path.exists(mp3_file):
                print("Le fichier existe déjà")
            else:
                print('Téléchargement de la musique...')
                stream.download(output_path=self.pathAudioFolder)
                os.rename(downloaded_file, mp3_file)
                print('Téléchargement de la musique terminé.')  

        except Exception as e:
            print('Une erreur s\'est produite : ', str(e))


class SpotifyDownloader():

    def __init__(self, pathAudioFolder = "/assets/audiosDownloaded/") -> None:
        self.pathAudioFolder = pathAudioFolder

    def downloadFromUrl(self, url):
        try:
           pass
        except Exception as e:
            pass

if __name__ == "__main__":
    YoutubeDownloader().downloadFromUrl("https://youtu.be/9bZkp7q19f0")