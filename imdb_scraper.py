# A scraper to get the movies listed 8.5 and above on imdb

import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/"

# user your user-agent here
header = {
    "User-Agent": 
}

page = requests.get(URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')


movies = soup.find("table", {"class": "chart full-width"}).find_all("tr")


for movie in movies:
    try:
        name = movie.find("td", {"class": "titleColumn"})
        rating = movie.find("td", {"class": "ratingColumn imdbRating"})
        if(float(rating.get_text()) > 8.5):
            print(name.get_text().strip())
            print(rating.get_text())
    except AttributeError:
        print("none")
