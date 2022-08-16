# spotify_playlist_downloader

This is a small script i made to download playlists from spotfiy (the songs are downloaded from youtube not spotify, dont get too excited).
I also made a script to download youtube playlists as mp3, the playlist needs to be public for the script to work, you can use the playlist url or a video inside it.

## Installation
### Register application (for spotify only)
1. Go to:  	[Spotify dev dashboard](https://developer.spotify.com/dashboard/applications)
2. Create new app
3. Get the client_id and client_secret and put them in main.py (in vars)
4. Go to edit settings and add this redirect URI: "https://0.0.0.0:8888/callback"
### Install packages
1. run the following commands in the same dir:
```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```
### Some issues and fixes
the script hasn't been tested, it was just a small script for fun, so if you found some issues or have some ideas let me know.
also i faced some problems with some packages, if you do aswell, just make sure all the packages causing the error are updated by using -U on pip
for ex: if urllib3 caused an error just do `python -m pip install -U urllib3`
