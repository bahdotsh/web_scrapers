import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/"

header = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
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
