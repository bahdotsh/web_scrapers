# A scraper to get the movies listed 8.5 and above on imdb
from urllib.request import urlopen as uop
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/"


uClient = uop(URL)
page = uClient.read()
uClient.close()


soup = BeautifulSoup(page, 'html.parser')


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
