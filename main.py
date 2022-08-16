import spotipy
from spotipy.oauth2 import SpotifyOAuth
from youtube_search import YoutubeSearch
from pytube import YouTube
import os


client_id = "your_client_id"
client_secret = "your_client_secret"
red_uri = "https://0.0.0.0:8888/callback"
scope = "user-library-read,playlist-read-private"


def search_vid(x):
    results = YoutubeSearch(x, max_results=1).to_dict()
    return "https://www.youtube.com"+results[0]["url_suffix"]


def download_mp3(pl, x):
    yt = YouTube(x)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="./Music/"+pl)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print("Song successfully downloaded.\n")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope, client_secret=client_secret, client_id=client_id, redirect_uri=red_uri))
results = sp.user_playlists(sp.me()["id"])
for idx, item in enumerate(results["items"]):
    print(idx, " - ", item["name"])
print(idx+1, " -  Download from URL")
n = -1
while (n > idx+1 or n < 0):
    n = int(input("\n\nSelect a playlist: "))
if (n > idx):
    link = input("Enter url: ")
    tmp = link.replace("https://open.spotify.com/playlist/", "").split("?")[0]
    results2 = sp.playlist_items(playlist_id=tmp)
else:
    results2 = sp.playlist_items(playlist_id=results["items"][n]["id"])
for idx, item in enumerate(results2["items"]):
    print(idx, "> Downloading -> ", item["track"]["artists"][0]
          ["name"], ", ", item["track"]["name"])
    url = search_vid(item["track"]["artists"][0]
                     ["name"] + ", " + item["track"]["name"])
    download_mp3(results["items"][n]["name"], url)

print("Playlist downloaded! enjoy :)")
