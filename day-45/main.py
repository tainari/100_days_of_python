import csv

from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
# x = soup.find(name="div", class_="entity-info-items__list")
movies = soup.find_all(name="h3", class_="title")
titles = []
ranks = []
for movie in movies:
    rank_and_title = movie.text
    rank = int(rank_and_title.strip().split(")")[0].split(":")[0])
    ranks.append(rank)
    title = rank_and_title.split(")")
    if len(title) == 1:
        title = title[0].split(":")[1].strip()
    else:
        title = title[1].strip()
    titles.append(title)

ranks.reverse()
titles.reverse()
ranks_and_titles = zip(ranks, titles)
with open("movies.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(ranks_and_titles)

# content = soup.prettify()
# with open("movies.html", "w", encoding="utf-8") as f:
#     f.write(content)
# for y in x:
#     print(f"Title: {y.get_text()}; Link: {y.get('href')}")