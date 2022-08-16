from pytube import Playlist
import os

def download_playlist(x):
    p = Playlist(x)
    for vid in p.videos:
        print("Downloading ->",vid.title)
        video = vid.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="./Music/"+p.title)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Song successfully downloaded.\n")

url = input("Playlist URL: ")
download_playlist(url)
print("Playlist downloaded! have fun :)")