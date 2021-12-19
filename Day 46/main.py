from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="4aec07fd115942dc8601a97d453ba99c",
        client_secret= "e79ebd8206004b489e00115c4073bfd9",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user = input("which year do you want to travel to? Type the date in this rormat YYYY-MM-DD: ")
web = requests.get(f"https://www.billboard.com/charts/hot-100/{user}/")
soup = BeautifulSoup(web.text,"html.parser")
songs = soup.find_all(name="li",class_="lrv-u-width-100p")
songs_list = []
song_uris = []
for song in songs:
    test = song.find(name="h3",class_="c-title")
    if test == None:
        pass
    else:
        songs_list.append(test.string)

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{2006}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{user} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)