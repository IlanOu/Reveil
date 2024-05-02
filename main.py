import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from pytube import YouTube, Search
import random
from dotenv import load_dotenv
import os
import re
import urllib.parse


# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class SpotifyPlaylistDownloader:
    def __init__(self):
        self.client_id = os.environ.get('SPOTIFY_CLIENT_ID')
        self.client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.sp = self.setup_spotify_client()

    def setup_spotify_client(self):
        scope = "playlist-read-private"
        try:
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                        client_secret=self.client_secret,
                                                        redirect_uri="http://google.com",
                                                        scope=scope))
            return sp
        except spotipy.exceptions.SpotifyException as e:
            print(f"Erreur d'authentification Spotify : {e}")
            return None

    def get_playlist_tracks(self, playlist_id):
        if self.sp is None:
            print("Erreur d'authentification Spotify. Impossible d'accéder à la playlist.")
            return []

        try:
            playlist = self.sp.playlist(playlist_id)
            return [track['track']['name'] for track in playlist['tracks']['items']]
        except spotipy.exceptions.SpotifyException as e:
            print(f"Erreur lors de l'accès à la playlist : {e}")
            return []

    def download_random_track(self, track_names):
        random_track = random.choice(track_names)
        downloader = YouTubeDownloader()
        downloader.download_track(random_track)

class YouTubeDownloader:
    def __init__(self, output_path="./"):
        self.output_path = output_path

    def download_track(self, track_name):
        # try:
        # Construire l'URL YouTube à partir du nom de la piste
        query = urllib.parse.quote(track_name)
        url = f"https://www.youtube.com/results?search_query={query}"

        print(url)

        s = Search(track_name)
        print(s)

        # Utiliser pytube pour télécharger la vidéo à partir de l'URL
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=self.output_path)

        base, ext = os.path.splitext(out_file)
        new_file = f"{base}.mp3"
        os.rename(out_file, new_file)
        print(f"La piste '{track_name}' a été téléchargée.")
        # except Exception as e:
        #     print(f"Erreur lors du téléchargement de '{track_name}' : {e}")

# Utilisation
downloader = SpotifyPlaylistDownloader()
# playlist_url = input("Entrez l'URL de la playlist Spotify : ")
playlist_id = "37i9dQZF1EIfEjKERoVwUX"
track_names = downloader.get_playlist_tracks(playlist_id)
downloader.download_random_track(track_names)