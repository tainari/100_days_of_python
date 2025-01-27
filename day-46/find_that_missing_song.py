####################################################################################
##
##   I have been looking for a song I used to run to for ages and I CANNOT figure
##   figure out what it is; I just remember a rap part and a scream in the middle.
##   Decided to loop over all top songs from 2013-2015 to see if I could find it.
##   It didn't work :(
##
####################################################################################

import csv
import datetime, json, requests, spotipy, time

from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

search_date_dt = datetime.datetime.strptime("2013-01-01", "%Y-%m-%d")
END_DATE = datetime.datetime.strptime("2015-10-01","%Y-%m-%d")
while search_date_dt <= END_DATE:
    search_date = search_date_dt.strftime("%Y-%m-%d")
    print(f"Starting week containing {search_date}...")
    SCRAPE_URL = f"https://www.billboard.com/charts/hot-100/{search_date}"
    response = requests.get(SCRAPE_URL, headers=header)
    response_text = response.text
    soup = BeautifulSoup(response_text, "html.parser")
    ## GET TITLES
    ## note that the top title has a slightly different class because it is styled differently.
    top_title = soup.find(name="h3", class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150").text.strip()
    next_99_titles = [title.text.strip() for title in soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
    all_titles = [top_title] + next_99_titles
    ## GET ARTISTS' NAMES
    ## same issue as above
    top_artist = soup.find(name="p", class_="c-tagline a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150").text.strip()
    next_99_artists = [artist.text.strip() for artist in soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]
    ## Stitch em together and put them in a stew
    all_artists = [top_artist] + next_99_artists
    artists_and_titles = zip(all_artists, all_titles)
    with open("songs.csv","a") as f:
        writer = csv.writer(f)
        writer.writerows(artists_and_titles)
    search_date_dt = search_date_dt + datetime.timedelta(days=7)
    time.sleep(10)
