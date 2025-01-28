import datetime, json, requests, spotipy
from spotipy.oauth2 import SpotifyOAuth

from bs4 import BeautifulSoup

DEBUG = True

with open("../info.json") as f:
    info = json.load(f)
    SPOTIFY_SECRET = info["spotify_secret"]
    SPOTIFY_ID = info["spotify_id"]
    SPOTIPY_REDIRECT_URI = info["spotify_redirect_uri"]

from utils import is_bad_date

search_date = datetime.date.today().strftime("%Y-%m-%d")
bad_format = True
while bad_format:
    search_date = input("Which date do you want to travel to? Input format: YYYY-MM-DD: ")
    if search_date[0] == "q":
        quit()
    bad_format = is_bad_date(search_date)
    if bad_format:
        print("Sorry, that date is invalid. Please try again.")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

SCRAPE_URL = f"https://www.billboard.com/charts/hot-100/{search_date}"

response = requests.get(SCRAPE_URL, headers=header)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
## GET TITLES
## note that the top title has a slightly different class because it is styled differently.
top_title = soup.find(name="h3", class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150").text.strip()
next_99_titles = [title.text.strip() for title in soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
all_titles = [top_title] + next_99_titles
## GET ARTIST NAMES
## same issue as above
top_artist = soup.find(name="p", class_="c-tagline a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150").text.strip()
next_99_artists = [artist.text.strip() for artist in soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]
all_artists = [top_artist] + next_99_artists
all_tracks = zip(all_titles, all_artists)

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                    client_secret=SPOTIFY_SECRET,
                                                    scope="playlist-modify-private",
                                                    cache_path="./token.txt",
                                                    redirect_uri=SPOTIPY_REDIRECT_URI,
                                                    show_dialog=True,
                                                    username="tainari"))
user_id = spotify.me()['id']

# find all songs
all_uris = []
for title, artist in all_tracks:
    query = f"{artist}+{title}"
    results = spotify.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        uri = results["tracks"]["items"][0]["uri"]
        all_uris.append(uri)

# make a playlist! :)
playlist_name = f"{search_date} Billboard 100"
playlist = spotify.user_playlist_create(user=user_id, name=playlist_name,public=False, description=f"{search_date} Billboard 100 - auto-generated!")
playlist_id = playlist['id']

spotify.playlist_add_items(playlist_id, all_uris)